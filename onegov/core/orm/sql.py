""" Provides experimental SQL queries with "benefits".

Raw SQL queries can be directly executed by SQLAlchemy, but there is some
boilerplate involved and the written SQL code exists as a bit of a black box
that is only reusable with even more boilerplate.

On top of it the written SQL query has one way of passing arguments for
SQLAlchemy, another for PSQL and yet another for Navicat.

This module uses a somewhat opinonated way of writing SQL queries to solve
these problems to a degree.

Query Form
==========

SQL queries written for this module have the following form::

    SET vars.table_name = 'table_name';
    SELECT table_name, column_name
      FROM information_schema.columns
     WHERE table_name = current_setting('vars.table_name')::text;

This query can be executed using PSQL and Navicat, by replacing 'table_name'
with the actual table name and running it::

    SET vars.table_name = 'pg_user';
    SELECT table_name, column_name
      FROM information_schema.columns
     WHERE table_name = current_setting('vars.table_name')::text;

As such, the statement can be reused verbatim, with the exception of the
SET command at the head of the statement.

Arguments
=========

Internally, this SET command is used to create a function that creates a
bound query. The query above could be used as follows::

    table_columns = SQLQuery('... statement from above ...')
    session.execute(table_columns(table_name='pg_user'))

SQLAlchemy
==========

The result of ``queries.table_columns`` is a bound sqlalchemy statemnt that
may be reused in other queries, if the columns are specified::

    from sqlalchemy import Text, select

    stmt = table_columns(table_name='pg_user').columns(
        table_name=Text,
        column_name=Text
    ).alias('table_name')

    session.execute(
        select(stmt.c.table_name).where(stmt.c.column_name == 'passwd')
    )

In this way we can write a general query that we can customize and use in
conjunction with other queries.

Default Arguments
=================

Sometimes we want to use arguments with a default value. We can do this using
a comment which will be eval'd into Python::

    SET vars.table_name = 'table_name' -- ('pg_user', );
    SELECT table_name, column_name
      FROM information_schema.columns
     WHERE table_name IN current_setting('vars.table_name');

The resulting query function doesn't require the table_name parameter. So
both of these forms are possible::

    session.execute(table_columns())
    session.execute(table_columns(table_name=('pg_foobar', )))

Arrays
======

To use arrays as values, you need to cast them as follows::

    SET vars.tables = 'tables';

    SELECT * FROM foo WHERE table IN (
        SELECT unnest(current_setting('vars.states')::text[])
    )

In your editor, you can use the values as follows::

    SET vars.tables = '{foo,bar}';

The SELECT unnest expression will automatically be replaced when handing
the query over to SQLAlchemy.

"""

import re

from cached_property import cached_property
from onegov.core import utils
from pathlib import Path
from sqlalchemy import text


VARIABLE_EX = re.compile(
    r"""
        \s*SET\svars\.(?P<name>[a-z0-9_]+)\s
        =\s:?'[^']*';
        ?(\s--\s(?P<default>.*)|)  # optional defaults
    """,
    re.IGNORECASE | re.VERBOSE)


UNNEST_EX = re.compile(
    r"""
        \(
            SELECT\sunnest\(current_setting\('vars\.
            (?P<name>[a-z0-9_]+)
            '\)::(text|int)\[\]\)
        \)
    """,
    re.IGNORECASE | re.VERBOSE
)


TRANSFORM_EX = re.compile(
    r"""
        current_setting\('vars\.
        (?P<name>[a-z0-9_]+)
        '\)
    """,
    re.IGNORECASE | re.VERBOSE
)


class SQLQuery(object):
    """ Uses a raw SQL query and returns metadata and variations of it. """

    def __init__(self, query):
        self.query = query

    @classmethod
    def from_path(cls, path, module=None):
        path = Path(path)

        if not path.is_absolute():
            assert module, "A module is required for relative paths"
            path = Path(utils.module_path_root(module)) / path

        with path.open('r') as f:
            return cls(f.read())

    @cached_property
    def definitions(self):
        """ Returns the variable definitions together with line numbers. """

        matches = (
            (ix, VARIABLE_EX.match(l))
            for ix, l in enumerate(self.query.splitlines())
        )

        return tuple((ix, m) for ix, m in matches if m)

    @cached_property
    def arguments(self):
        """ Returns the arguments required by the query. If the key has a
        corresponding value, it is an unevaluated default value.

        """
        return dict(
            (m.group('name'), m.group('default'))
            for ix, m in self.definitions
        )

    @cached_property
    def body(self):
        """ Returns the query without the variable defintions on top. """

        header_end = self.definitions[-1][0] if self.definitions else -1
        return '\n'.join(self.query.splitlines()[header_end + 1:])

    @cached_property
    def as_statement(self):
        """ Returns the query as bound SQLAlchemy statement. """

        body = self.body

        # unnest array expressions
        body = UNNEST_EX.sub(":\g<name>", body)

        # change setting calls to paramters
        body = TRANSFORM_EX.sub(":\g<name>", body)

        # escape postgres type casts for sqlalchemy
        body = body.replace('::', '\:\:')

        return text(body.rstrip(' \n;'))

    def __call__(self, **args):
        for key, default in self.arguments.items():
            if key not in args and default:
                args[key] = eval(default)

        for key in args:
            if key not in self.arguments:
                msg = "query got an unexpected keyword argument: '{}'"
                raise TypeError(msg.format(key))

        for key, default in self.arguments.items():
            if key not in args:
                msg = "query is missing 1 required keyword argument: '{}'"
                raise TypeError(msg.format(key))

        return self.as_statement.bindparams(**args)
