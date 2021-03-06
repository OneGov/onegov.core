Changelog
---------
0.85.1 (2019-08-08)
~~~~~~~~~~~~~~~~~~~

- Adds missing dependency.
  [href]

0.85.0 (2019-08-08)
~~~~~~~~~~~~~~~~~~~

- Vendors in htmldiff, an html diffing library.
  [href]

0.84.0 (2019-07-22)
~~~~~~~~~~~~~~~~~~~

- Linkify supports link generation for phone numbers.
  [dadadamotha]

0.83.0 (2019-07-17)
~~~~~~~~~~~~~~~~~~~

- Fixes field label translation being too eager.
  [href]

- Automatically generates csrf/identity tokens in development.
  [href]

0.82.0 (2019-07-01)
~~~~~~~~~~~~~~~~~~~

- Rewrites parts of the cronjobs system.

  The cronjobs system now supports running every minute (not just every 5) and
  it is possible to have overlapping cronjobs (though not encouraged).

  Errors inside the cronjob-threads are now also reported using Sentry.
  [href]

0.81.0 (2019-06-19)
~~~~~~~~~~~~~~~~~~~

- Adds public and secret metadata to all OneGov instances.
  [href]

0.80.2 (2019-06-12)
~~~~~~~~~~~~~~~~~~~

- Increases resilience of date converter.
  [href]

0.80.1 (2019-05-28)
~~~~~~~~~~~~~~~~~~~

- Ignores SQLAlchemy function registration warnings.
  [href]

- Adds the ability to define multiple onegov.core upgrade entry points.
  [href]

0.80.0 (2019-05-03)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to override the same site cookie policy.
  [href]

- Turns CSVFile into an iterator.
  [href]

0.79.2 (2019-05-01)
~~~~~~~~~~~~~~~~~~~

- Drops legacy sentry parameter.
  [msom]

0.79.1 (2019-04-30)
~~~~~~~~~~~~~~~~~~~

- Adds sentry configuration setup.
  [msom]

0.79.0 (2019-04-30)
~~~~~~~~~~~~~~~~~~~

- Enables sentry in CLI commands.
  [msom]

0.78.3 (2019-04-26)
~~~~~~~~~~~~~~~~~~~

- Fixes transfer not working in certain cases.
  [href]

- Improves CSV handling.
  [msom]

0.78.2 (2019-04-23)
~~~~~~~~~~~~~~~~~~~

- Improves CSV handling.
  [msom]

0.78.1 (2019-04-17)
~~~~~~~~~~~~~~~~~~~

- Improves onegov-core transfer command.
  [href]

- Fixes is_uuid falsely identifying certain strings as UUID.
  [href]

0.78.0 (2019-02-01)
~~~~~~~~~~~~~~~~~~~

- Adds the user group ID to the identity policy.
  [msom]

0.77.0 (2019-01-30)
~~~~~~~~~~~~~~~~~~~

- Exclude redis 3.1.0.
  [href]

- Moves the elements to the core (from onegov.org).
  [msom]

0.76.0 (2019-01-23)
~~~~~~~~~~~~~~~~~~~

- Adds an utility function to turn strings with newlines into paragraphs.
  [href]

- Removes unused active history on association proxy.
  [href]

0.75.1 (2019-01-21)
~~~~~~~~~~~~~~~~~~~

- Fixes association proxy not working properly with some polymorphic classes.
  [href]

0.75.0 (2019-01-11)
~~~~~~~~~~~~~~~~~~~

- Adds request reference to form.meta.
  [href]

0.74.5 (2019-01-03)
~~~~~~~~~~~~~~~~~~~

- Uses SameSite=Lax on all session cookies.
  [href]

0.74.4 (2018-12-17)
~~~~~~~~~~~~~~~~~~~

- Adds a padding option to number formatting.
  [msom]

0.74.3 (2018-11-23)
~~~~~~~~~~~~~~~~~~~

- Adds a roots property to adjacency lists.
  [msom]

0.74.2 (2018-10-18)
~~~~~~~~~~~~~~~~~~~

- Fixes macro rendering failing with latest chameleon release.
  [href]

0.74.1 (2018-10-17)
~~~~~~~~~~~~~~~~~~~

- Adds weekday short format.
  [href]

0.74.0 (2018-10-16)
~~~~~~~~~~~~~~~~~~~

- Allows multiple associations per model.
  [msom]

0.73.1 (2018-10-11)
~~~~~~~~~~~~~~~~~~~

- Fixes core upgrade failing if no elasticsearch is used.
  [href]

0.73.0 (2018-10-08)
~~~~~~~~~~~~~~~~~~~

- Moves the yubikey related functions to the core (from onegov.user).

  In the future, it might make sense to move this to a onegov.otp package. In
  any case, onegov.user is not the right place as the integraiton happens in
  onegov.core as it is and the user model should not be a prerequisite for
  yubikeys.

  [href]

0.72.5 (2018-10-04)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to parse isodate strings through the layout class.
  [href]

0.72.4 (2018-10-04)
~~~~~~~~~~~~~~~~~~~

- Adds support for bleach 3.0.0.
  [href]

0.72.3 (2018-09-27)
~~~~~~~~~~~~~~~~~~~

- Stops search reindexing when adding a new column during upgrades.
  [href]

0.72.2 (2018-09-20)
~~~~~~~~~~~~~~~~~~~

- Only loads a minimal set of values during column upgrades with defaults to
  avoid triggering missing column errors.
  [href]

0.72.1 (2018-09-20)
~~~~~~~~~~~~~~~~~~~

- Fixes Windows newlines causing a badly rendered markdown.
  [href]

0.72.0 (2018-09-12)
~~~~~~~~~~~~~~~~~~~

- Adds a markdown renderer that accepts untrusted markdown.
  [href]

0.71.6 (2018-08-31)
~~~~~~~~~~~~~~~~~~~

- Fixes form translations resulting in a RecursionError.
  [href]

0.71.5 (2018-08-30)
~~~~~~~~~~~~~~~~~~~

- Adds an unaccent expression.
  [msom]

0.71.4 (2018-08-27)
~~~~~~~~~~~~~~~~~~~

- Caches layouts number formatting options.
  [msom]

- Checks for recursive translation fallback chains.
  [msom]

0.71.3 (2018-08-16)
~~~~~~~~~~~~~~~~~~~

- Also clones the pluralization function of a translation.
  [msom]

0.71.2 (2018-08-16)
~~~~~~~~~~~~~~~~~~~

- Allows to override wtforms translations.
  [msom]

0.71.1 (2018-08-15)
~~~~~~~~~~~~~~~~~~~

- Improves the speed of e-mail sending through smtp.
  [href]

0.71.0 (2018-06-27)
~~~~~~~~~~~~~~~~~~~

- Changes the upgrade order to take the source code order into account.
  [href]

0.70.6 (2018-06-15)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to version static files to cache them forever.
  [href]

0.70.5 (2018-06-04)
~~~~~~~~~~~~~~~~~~~

- Adds compatibility with WTForms 2.2.
  [href]

0.70.4 (2018-05-31)
~~~~~~~~~~~~~~~~~~~

- Enables class-methods as form directive inputs.
  [href]

- Adds the ability to run a cronjob every hour.
  [href]

0.70.3 (2018-05-29)
~~~~~~~~~~~~~~~~~~~

- Adds support for excel boolean cells.
  [msom]

- Adds compatibility with babel 2.6.
  [msom]

0.70.2 (2018-05-25)
~~~~~~~~~~~~~~~~~~~

- Adds another missing database connection error.
  [href]

0.70.1 (2018-05-25)
~~~~~~~~~~~~~~~~~~~

- Catches additional datbase connection errors.
  [href]

0.70.0 (2018-05-24)
~~~~~~~~~~~~~~~~~~~

- Catches database connection errors, returning a 503 when that happens.

  This allows for live postgres restarts.

  [href]

0.69.1 (2018-05-21)
~~~~~~~~~~~~~~~~~~~

- Adds a json encoder/decoder for morepath query parameters.
  [href]

0.69.0 (2018-05-15)
~~~~~~~~~~~~~~~~~~~

- Removes memcached in favor of redis.
  [href]

- Removes distributed locking in favor of local locking.

  Distributed locking might be reintroduced in the future.

  [href]

0.68.2 (2018-05-10)
~~~~~~~~~~~~~~~~~~~

- Fixes a long-standing issues where cached entries would be in a detached
  state when they were accessed.
  [href]

- Fixes conversion of excel date cells.
  [msom]

0.68.1 (2018-05-01)
~~~~~~~~~~~~~~~~~~~

- Increases the connection recycle time to one hour.
  [href]

0.68.0 (2018-04-30)
~~~~~~~~~~~~~~~~~~~

- Closes database connections after they become stale.

  This should help lower the memory usage of servers with many tennantes.
  [href]

0.67.2 (2018-04-27)
~~~~~~~~~~~~~~~~~~~

- Fixes the default locale negotiator.
  [msom]

- Fixes a rare race-condition with request messages.
  [href]

- Changes the way session managers are bound to the application.

  This fixes #21 by introducing a global session manager reference.
  [href]

0.67.1 (2018-04-06)
~~~~~~~~~~~~~~~~~~~

- Switches to simplejson from rapidjson to close down a memory leak.
  [href]

0.67.0 (2018-04-02)
~~~~~~~~~~~~~~~~~~~

- Replaces python-memcached with libmc.
  [href]

0.66.0 (2018-03-22)
~~~~~~~~~~~~~~~~~~~

- Removes hipchat method.
  [href]

0.65.2 (2018-03-20)
~~~~~~~~~~~~~~~~~~~

- Caches selectables loaded by path.
  [href]

- Changes the object_src of the default content security policy to self. This
  allows PDF viewers of browser to work properly.
  [msom]

0.65.1 (2018-03-14)
~~~~~~~~~~~~~~~~~~~

- Adds a mail macros lookup property.
  [href]

0.65.0 (2018-03-06)
~~~~~~~~~~~~~~~~~~~

- Splits all e-mails into transactional/marketing pools. By default, e-mails
  are sent through the marketing pool.
  [href]

0.64.0 (2018-03-05)
~~~~~~~~~~~~~~~~~~~

- Adds a function to send zulip messages.
  [msom]

0.63.1 (2018-02-28)
~~~~~~~~~~~~~~~~~~~

- Adds mailgun support for reply-to.
  [href]

0.63.0 (2018-02-26)
~~~~~~~~~~~~~~~~~~~

- Enables the 'btree_gist' extension for postgres.
  [href]

0.62.2 (2018-02-26)
~~~~~~~~~~~~~~~~~~~

- Uses the better supported sqlalchemy>=1.2.3 notation now that 1.2.3+ is out.
  [href]

0.62.1 (2018-02-22)
~~~~~~~~~~~~~~~~~~~

- Fixes core upgrades no longer working.
  [href]

0.62.0 (2018-02-22)
~~~~~~~~~~~~~~~~~~~

- Adds request.session, a shortcut to the session through the request.
  [href]

0.61.2 (2018-02-19)
~~~~~~~~~~~~~~~~~~~

- Excludes SQLAlchemy 1.2.3 from supported versions as it has a major bug.
  [href]

0.61.1 (2018-02-19)
~~~~~~~~~~~~~~~~~~~

- Fixes non-nullable columns upgrade failing in certain cases.
  [href]

0.61.0 (2018-02-16)
~~~~~~~~~~~~~~~~~~~

- Fixes columns with dots not working as selectable statements.
  [href]

- Adds support for arrays in selectable statements.
  [href]

0.60.2 (2018-02-12)
~~~~~~~~~~~~~~~~~~~

- Hides psycopg2 warning.
  [href]

0.60.1 (2018-02-07)
~~~~~~~~~~~~~~~~~~~

- Limits the content security policy reporting to 1/1000 requests by default.
  [href]

0.60.0 (2018-02-06)
~~~~~~~~~~~~~~~~~~~

- Implements a default content security policy.
  [href]

0.59.0 (2018-01-26)
~~~~~~~~~~~~~~~~~~~

- Enables the 'unaccent' extension for postgres.
  [href]

0.58.2 (2018-01-17)
~~~~~~~~~~~~~~~~~~~

- Categorises e-mails as 'onegov' for mailjet monitoring.
  [href]

0.58.1 (2018-01-09)
~~~~~~~~~~~~~~~~~~~

- Adds supports for date/time CLDR skeleton patterns.
  [msom]

0.58.0 (2018-01-03)
~~~~~~~~~~~~~~~~~~~

- Replaces the dictionary based property with a more complete and easier
  to use implementation (backwards compatible).
  [href]

- Adds the ability to pass extra properties to "add_by_form".
  [href]

0.57.0 (2017-12-29)
~~~~~~~~~~~~~~~~~~~

- Adds an 'add_by_form' method to generic collections.
  [href]

- Adds the ability to add additional serializers for JSON.
  [href]

- Now requires Python 3.6+.
  [href]

0.56.0 (2017-12-22)
~~~~~~~~~~~~~~~~~~~

- Switches default json implementation to rapidjson.
  [href]

0.55.1 (2017-12-20)
~~~~~~~~~~~~~~~~~~~

- Fixes empty dicts not working with new non-nullable columns.
  [href]

0.55.0 (2017-12-19)
~~~~~~~~~~~~~~~~~~~

- Adds a convenience method to add a new columns with defaults during upgrades.
  [href]

0.54.4 (2017-12-14)
~~~~~~~~~~~~~~~~~~~

- Allows to specify extra mail headers.
  [msom]

0.54.3 (2017-12-11)
~~~~~~~~~~~~~~~~~~~

- Fixes composition of mails with attachments.
  [msom]

- Adds the ability to turn raw SQL statements into SQLAlchemy selectables.
  [href]

0.54.2 (2017-12-11)
~~~~~~~~~~~~~~~~~~~

- Allows more flexibility when adding attachments to mails.
  [msom]

0.54.1 (2017-12-04)
~~~~~~~~~~~~~~~~~~~

- Generalises the html to plaintext function to be useable outside mail.
  [href]

0.54.0 (2017-12-01)
~~~~~~~~~~~~~~~~~~~

- Switches the data type of all JSON columns from TEXT to JSONB.
  [href]

0.53.6 (2017-11-23)
~~~~~~~~~~~~~~~~~~~

- Cuts down on cli debug output when the postgres server is down.
  [href]

0.53.5 (2017-11-23)
~~~~~~~~~~~~~~~~~~~

- Checks the default values of dictionary based properties.
  [msom]

0.53.4 (2017-11-23)
~~~~~~~~~~~~~~~~~~~

- Allows to set a default to dictionary based properties.
  [msom]

0.53.3 (2017-11-22)
~~~~~~~~~~~~~~~~~~~

- Fixes schema order being undeterministic.
  [href]

0.53.2 (2017-11-14)
~~~~~~~~~~~~~~~~~~~

- Adds support for applications that limit the Public permission.
  [href]

0.53.1 (2017-11-09)
~~~~~~~~~~~~~~~~~~~

- Enables <pre> and <span> tags in sanitized html.
  [href]

0.53.0 (2017-11-07)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to get the local time from the layout.
  [href]

- Adds the ability to specify a custom rowtype for CSVFile objects.
  [href]

- Adds support for slashes in csv headers.
  [href]

- Improves detection of CSV dialects.
  [href]

0.52.1 (2017-10-23)
~~~~~~~~~~~~~~~~~~~

- Improves the safe_format utility and adds a way to extract its keys.
  [href]

0.52.0 (2017-10-23)
~~~~~~~~~~~~~~~~~~~

- Adds a safe_format utility function for user-provided format strings.
  [href]

0.51.1 (2017-10-19)
~~~~~~~~~~~~~~~~~~~

- Replaces the builtin lru_cache with fastchache's faster version.
  [href]

- Adds the ability to print exceptions during development.
  [href]

0.51.0 (2017-10-09)
~~~~~~~~~~~~~~~~~~~

- Adds proper many-to-many support for associable tables by removing the PK.
  [href]

- Moves identity management functions.
  [msom]

0.50.0 (2017-10-04)
~~~~~~~~~~~~~~~~~~~

- Adds helper functions for identity management.
  [msom]

0.49.0 (2017-09-28)
~~~~~~~~~~~~~~~~~~~

- Adds a generic redirect model for internal redirects.
  [href]

0.48.2 (2017-09-22)
~~~~~~~~~~~~~~~~~~~

- Fixes associable not disabling cascades completely.
  [href]

0.48.1 (2017-09-22)
~~~~~~~~~~~~~~~~~~~

- Fixes the associated table names for associable models.
  [href]

- Sets the language in the ORM after the transaction has begun, not before.
  [href]

0.48.0 (2017-09-12)
~~~~~~~~~~~~~~~~~~~

- Adds generic associations to the ORM library.

  See ``associable.py`` for more information. This feature should be
  considered experimental.
  [href]

0.47.0 (2017-09-08)
~~~~~~~~~~~~~~~~~~~

- Adds a helper method to express binary data in a dictionary.
  [href]

0.46.0 (2017-08-31)
~~~~~~~~~~~~~~~~~~~

- Adds a toggle function for sets to utils.
  [href]

0.45.0 (2017-08-25)
~~~~~~~~~~~~~~~~~~~

- Adds support for decimal values to JSON.
  [href]

- Forces the memory cache backend to use Dill to force the same codepath for
  memcached/memcached-less data (now everything is always pickled).

  This lets us catch pickling bugs during testing that we might otherwise
  miss.
  [href]

0.44.0 (2017-08-10)
~~~~~~~~~~~~~~~~~~~

- No longer limits the number of overflow connections in the queue pool.

  This is mainly useful for cronjob threads which need one connection each and
  who will now only be limited by the connection limit of the database.
  [href]

0.43.3 (2017-07-10)
~~~~~~~~~~~~~~~~~~~

- Skips dill version 0.2.7 as this version leads to recursion errors.
  [href]

- Enables a css minifier by default.
  [href]

0.43.2 (2017-07-07)
~~~~~~~~~~~~~~~~~~~

- Adds missing permission checking helper.
  [msom]

0.43.1 (2017-07-07)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to force an update on all timestamp based models.
  [href]

- Renames is_email_template to suppress_global_variables in the render_template
  function.
  [href]

0.43.0 (2017-07-03)
~~~~~~~~~~~~~~~~~~~

- Orders independent upgrade tasks by their module dependencies.

  This acts as a sane default for module upgrades. For example, if
  onegov.ticket depends on onegov.user, all user tasks will be executed first.
  Once the ticket tasks are run, the user tables are therefore up to date.

  This change only affects the order of tasks which do not define no
  explicit dependencies.

- Adds a datetime query argument converter.
  [href]

0.42.2 (2017-06-28)
~~~~~~~~~~~~~~~~~~~

- Allows to deal with CSV containing duplicate columns.
  [msom]

0.42.1 (2017-06-28)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to manually define the csv encoding.
  [msom]

0.42.0 (2017-06-28)
~~~~~~~~~~~~~~~~~~~

- Tightens the security of identity_secret and csrf_secret.

  Before, the identity_secret was shared between tennants (application ids).
  As a result certain signing methods would generate tokens which would work
  between multiple tennants. Fortunately this wasn't an avenue for serious
  exploits.

  With this change it is now much harder to use the identity/csrf secret
  insecurely. By default those tokens are now bound to the tennant.
  [href]

0.41.1 (2017-06-23)
~~~~~~~~~~~~~~~~~~~

- Fixes pagination of empty collections throwing ZeroDivisionError errors.
  [msom]

0.41.0 (2017-06-22)
~~~~~~~~~~~~~~~~~~~

- Allows to configure the used locales.
  [msom]

0.40.6 (2017-06-19)
~~~~~~~~~~~~~~~~~~~

- Fixes translations of multiple applications affecting each other within the
  same process.
  [href]

0.40.5 (2017-06-07)
~~~~~~~~~~~~~~~~~~~

- Adds a data property function.
  [href]

- Adds the ability to override the csrf salt.
  [href]

0.40.4 (2017-05-12)
~~~~~~~~~~~~~~~~~~~

- Fixes macro caching being too agressive.
  [href]

0.40.3 (2017-05-12)
~~~~~~~~~~~~~~~~~~~

- Improves performance for pages with a lot of generated links.
  [href]

0.40.2 (2017-05-04)
~~~~~~~~~~~~~~~~~~~

- Moves the chunks function into the utils module.
  [href]

0.40.1 (2017-05-04)
~~~~~~~~~~~~~~~~~~~

- Fixes translating messages with no present locale throwing an error. The
  message is new returned untranslated, if the locale is not present (fallback
  to English).
  [msom]

0.40.0 (2017-04-27)
~~~~~~~~~~~~~~~~~~~

- Fixes has_table not working with schemas.
  [href]

- Fixes filestorage returning an url for local paths.
  [href]

- Adds a lowercase text type for SQLAlchemy.
  [href]

0.39.0 (2017-04-07)
~~~~~~~~~~~~~~~~~~~

- Configures logging for CLI.
  [msom]

0.38.7 (2017-04-05)
~~~~~~~~~~~~~~~~~~~

- Puts the English fallback on translated forms at the back.
  [msom]

0.38.6 (2017-04-05)
~~~~~~~~~~~~~~~~~~~

- Uses English als default fallback on translated forms.
  [msom]

0.38.5 (2017-04-05)
~~~~~~~~~~~~~~~~~~~

- Fixes (builtin) translations of WTForms.
  [msom]

0.38.4 (2017-03-23)
~~~~~~~~~~~~~~~~~~~

- Fixes slashes not being stripped from the subpath in module_path.
  [href]

- Supports newlines in Excel outputs on all platforms.
  [href]

0.38.3 (2017-03-20)
~~~~~~~~~~~~~~~~~~~

- Adds compatibility with Morepath 0.18.
  [href]

0.38.2 (2017-03-17)
~~~~~~~~~~~~~~~~~~~

- Improves the performance of some code hotspots.
  [href]

- Adds the ability to directly provide a filestorage object.
  [href]

- Improves the performance of the csv parser.
  [href]

0.38.1 (2017-03-10)
~~~~~~~~~~~~~~~~~~~

- Fixes orm cache entries being stale under certain conditions.
  [href]

0.38.0 (2017-03-09)
~~~~~~~~~~~~~~~~~~~

- Integrates the latest bleach release.
  [href]

0.37.0 (2017-03-01)
~~~~~~~~~~~~~~~~~~~

- Adds a function to send hipchat notifications.
  [msom]

0.36.2 (2017-02-15)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to influence the batch query in pagination classes.
  [href]

- Fixes file-urls pointing to directories resulting in a 503 instead of a 404.
  [href]

0.36.1 (2017-02-03)
~~~~~~~~~~~~~~~~~~~

- Fixes an edge case where the orm cache would discard pending changes.
  [href]

0.36.0 (2017-02-03)
~~~~~~~~~~~~~~~~~~~

- Adds an experimental cache descriptor to greatly ease the use of cached
  orm objects/queries.
  [href]

0.35.2 (2017-01-18)
~~~~~~~~~~~~~~~~~~~

- Adds a temporary workaround for an arrow translation typo.
  [href]

0.35.1 (2016-12-23)
~~~~~~~~~~~~~~~~~~~

- Upgrade to Morepath 0.17.
  [href]

0.35.0 (2016-12-09)
~~~~~~~~~~~~~~~~~~~

- Adds support for PyFilesystem 2.x and Chameleon 3.x.
  [href]

0.34.0 (2016-12-09)
~~~~~~~~~~~~~~~~~~~

- Disallow cookies in svg resources.
  [href]

- Temporarily pin older versions of chameleon and fs.
  [msom]

0.33.0 (2016-12-06)
~~~~~~~~~~~~~~~~~~~

- Adds the model to the form object created by the form directive.
  [href]

- Adds the ability to recompile themes using shift+f5 in the browser.
  This option has to be enabled using the 'allow_shift_f5_compile' flag.
  [href]

- By default, ignore custom global template variables in e-mail templates.
  [href]

0.32.0 (2016-11-07)
~~~~~~~~~~~~~~~~~~~

- Adds has_table to UpgradeContext.
  [msom]

- Adds a FileDataManager.
  [msom]

0.31.1 (2016-10-28)
~~~~~~~~~~~~~~~~~~~

- Fixes url permission check not working for anonymous users.
  [href]

- Adds a default path argument converter for booleans.
  [href]

0.31.0 (2016-10-27)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to check if the current user may view an url.
  [href]

- Make sure has_permission works with overriden rules.
  [href]

0.30.3 (2016-10-26)
~~~~~~~~~~~~~~~~~~~

- Automatically sets the width of excel columns in the export.
  [href]

0.30.2 (2016-10-20)
~~~~~~~~~~~~~~~~~~~

- Prevents bulk updates/deletes on aggregated models.
  [href]

0.30.1 (2016-10-17)
~~~~~~~~~~~~~~~~~~~

- Improves the performance of the unique hstore keys utility function.
  [href]

- Improves the performance of pagination collections by speeding up the count.
  [href]

0.30.0 (2016-10-11)
~~~~~~~~~~~~~~~~~~~

- Adds a convenient and safe way to define return-to url parameters.
  [href]

- Fixes request.url not having the same semantics as webob.request.url.
  [href]

- Adds the ability to query form class associated with a model.
  [href]

0.29.3 (2016-10-07)
~~~~~~~~~~~~~~~~~~~

- Gets SQLAlchemy-Utils' aggregates decorator to work with the session manager.
  [href]

0.29.2 (2016-10-06)
~~~~~~~~~~~~~~~~~~~

- Forms handled through the form directive may now define a `on_request`
  method, which is called after the request has been bound to the form and
  before the view is handled.
  [href]

- Adds an utility function to remove repeated spaces.
  [href]

0.29.1 (2016-10-04)
~~~~~~~~~~~~~~~~~~~

- Adds compatibility with Morepath 0.16.
  [href]

0.29.0 (2016-10-04)
~~~~~~~~~~~~~~~~~~~

- Introduces a generic collection meant to share common functionalty.
  [href]

0.28.0 (2016-09-28)
~~~~~~~~~~~~~~~~~~~

- Moves the html sanitizer to its own module and introduce an svg sanitizer.
  [href]

0.27.2 (2016-09-26)
~~~~~~~~~~~~~~~~~~~

- Fixes get_unique_hstore_keys failing if the hstore is set to None.
  [href]

0.27.1 (2016-09-23)
~~~~~~~~~~~~~~~~~~~

- Adds an utility function to fetch unique hstore keys from a table.
  [href]

0.27.0 (2016-09-21)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to override a specific macro in child applications.
  [href]

- Supports a wider range of objects which may be cached. Uses 'dill' to
  accomplish this.
  [href]

- Removes the runtime bound cache again as it's not that useful.
  [href]

0.26.0 (2016-09-09)
~~~~~~~~~~~~~~~~~~~

- Adds a runtime bound cache, not shared between processes and able to
  accept any kind of object to cache (no pickling).
  [href]

0.25.1 (2016-09-01)
~~~~~~~~~~~~~~~~~~~

- Adds a uuid morepath converter.
  [href]

- Fixes variable directive resulting in overwrites instead of merges.
  [href]

0.25.0 (2016-08-26)
~~~~~~~~~~~~~~~~~~~

- Introduces a member role, which is close to an anonymous user in terms
  of access, but allows to differentiate between ananymous and registered
  users.
  [href]

0.24.0 (2016-08-24)
~~~~~~~~~~~~~~~~~~~

- Adds a template variable directive, which gives applications the ability
  to inject their own global variables into templates.
  [href]

- Fixes formatting date failing if the date is None.
  [msom]

0.23.0 (2016-08-23)
~~~~~~~~~~~~~~~~~~~

- Adds a static directory directive, which gives applications the ability
  to define their own static directory and for inherited applications to
  append a path to the list of static directory paths.
  [href]

- Moves two often used helpers to the base layout.
  [href]

- Adds a HTML5 (RFC3339) date converter for Morepath.
  [href]

0.22.1 (2016-07-28)
~~~~~~~~~~~~~~~~~~~

- Adds compatibility with Morepath 0.15.
  [href]

0.22.0 (2016-07-14)
~~~~~~~~~~~~~~~~~~~

- Adds an utility function to search for orm models.
  [href]

- Explicitly prohibit unsynchronized bulk updates with a helpful assertion.
  [href]

- Exports the random token length constant.
  [href]

0.21.3 (2016-07-06)
~~~~~~~~~~~~~~~~~~~

- Adds compatibility with python-magic 0.4.12.
  [msom]

0.21.2 (2016-06-06)
~~~~~~~~~~~~~~~~~~~

- Disable debug output when running cli commands.
  [href]

- Adds the ability to manually define the csv dialect.
  [href]

- Adds the ability to access csv files without any known headers.
  [href]

0.21.1 (2016-05-31)
~~~~~~~~~~~~~~~~~~~

- No longer print the selector when running a command.
  [href]

- Use a single connection during cli commands.
  [href]

- Adds the ability to configure the connection pool of the session manager.
  [href]

- Stops cronjobs from being activated during cli commands.
  [href]

0.21.0 (2016-05-30)
~~~~~~~~~~~~~~~~~~~

- Introduces a simpler way to write cli commands.
  [href]

0.20.2 (2016-05-13)
~~~~~~~~~~~~~~~~~~~

- Adds support for transforming lists if *irregular* dicts to csv and xlsx.
  [href]

0.20.1 (2016-04-29)
~~~~~~~~~~~~~~~~~~~

- Removes escaping characters from plaintext e-mails.
  [href]

0.20.0 (2016-04-11)
~~~~~~~~~~~~~~~~~~~

- Switch to new more.webassets release.
  [href]

0.19.0 (2016-04-06)
~~~~~~~~~~~~~~~~~~~

- Adds Morepath 0.13 compatibility.
  [href]

0.18.2 (2016-04-05)
~~~~~~~~~~~~~~~~~~~

- Fixes meta/content failing if the dictionary is None.
  [href]

0.18.1 (2016-04-01)
~~~~~~~~~~~~~~~~~~~

- Adds a custom datauri filter to work aorund an issue with webassets.
  [href]

0.18.0 (2016-03-24)
~~~~~~~~~~~~~~~~~~~

- Adds helper methods for accessing meta/content dicts through properties.
  [href]

0.17.2 (2016-02-15)
~~~~~~~~~~~~~~~~~~~

- Improves CSV handling.
  [msom]

- Ensures that the sendmail limit is an integer.
  [href]

0.17.1 (2016-02-11)
~~~~~~~~~~~~~~~~~~~

- Fixes certain form translations being stuck on the first request's locale.
  [href]

0.17.0 (2016-02-08)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to limit the number of emails to be processed in one go.
  [href]

- Allows to optionally pick the sheet when converting excel files to CSV.
  [msom]

0.16.1 (2016-02-02)
~~~~~~~~~~~~~~~~~~~

- Fixes connection pool exhaustion occuring when upgrading many tennants.
  [href]

0.16.0 (2016-01-28)
~~~~~~~~~~~~~~~~~~~

- Adds a method to lookup the polymorphic class of any polymorphic identity.
  [href]

0.15.2 (2016-01-27)
~~~~~~~~~~~~~~~~~~~

- Fixes wrong exception being caught for undelivarable e-mails.
  [href]

0.15.1 (2016-01-26)
~~~~~~~~~~~~~~~~~~~

- Removes undeliverable e-mails from the maildir queue.
  [href]

0.15.0 (2016-01-20)
~~~~~~~~~~~~~~~~~~~

- Exclude dots from normalized urls.
  [href]

0.14.0 (2016-01-20)
~~~~~~~~~~~~~~~~~~~

- Caches the result of po file compiles.
  [href]

0.13.4 (2016-01-18)
~~~~~~~~~~~~~~~~~~~

- Slightly improves normalize_for_url for German.
  [href]

0.13.3 (2016-01-18)
~~~~~~~~~~~~~~~~~~~

- Stops the form directive from chocking up if no form is returned.
  [href]

0.13.2 (2016-01-07)
~~~~~~~~~~~~~~~~~~~

- Stops cronjobs sometimes running twice in one minute.
  [href]

0.13.1 (2016-01-05)
~~~~~~~~~~~~~~~~~~~

- Fixes cronjobs not working with more than one process.
  [href]

0.13.0 (2015-12-31)
~~~~~~~~~~~~~~~~~~~

- Adds a cronjob directive to specify tasks which have to run at an exact time.
  [href]

- Adds a distributed lock mechanism using postgres.
  [href]

0.12.3 (2015-12-21)
~~~~~~~~~~~~~~~~~~~

- Fixes incorrect year in date format. Before the week's year was used instead
  of the date's year. This lead to incorrect output when formatting a date.
  [href]

0.12.2 (2015-12-18)
~~~~~~~~~~~~~~~~~~~

- Ensures a proper cleanup of the existing db schemas before completeing the
  transfer command.
  [href]

0.12.1 (2015-12-17)
~~~~~~~~~~~~~~~~~~~

- Fixes broken dependency.
  [href]

0.12.0 (2015-12-16)
~~~~~~~~~~~~~~~~~~~

- Includes a plain text alternative in all HTML E-Mails.
  [href]

0.11.2 (2015-12-15)
~~~~~~~~~~~~~~~~~~~

- Fixes cache expiration time having no effect.
  [href]

0.11.1 (2015-12-15)
~~~~~~~~~~~~~~~~~~~

- Fixes site locale creating many instead of one locale cookie.
  [href]

0.11.0 (2015-12-15)
~~~~~~~~~~~~~~~~~~~

- Adds a site locale model and renames 'languages' to 'locales'.
  [href]

0.10.0 (2015-12-14)
~~~~~~~~~~~~~~~~~~~

- Integrates localized database fields.

  Use ``onegov.core.orm.translation_hybrid`` together with sqlalchemy utils:
  http://sqlalchemy-utils.readthedocs.org/en/latest/internationalization.html

- Shares the session_manager with all ORM mapped instances which may access
  it through ``self.session_manager``.

  This is a plumbing feature to enable integration of localized database
  fields.
  [href]

- Adds a method to automatically scan all morepath dependencies. It is not
  guaranteed to always work and should only be relied upon for testing and
  upgrades.
  [href]

0.9.0 (2015-12-10)
~~~~~~~~~~~~~~~~~~~

- Adds a method which takes a list of dicts and turns it into a csv string.
  [href]

- Adds a method which takes a list of dicts and turns it into a xlsx.
  [href]

0.8.1 (2015-12-08)
~~~~~~~~~~~~~~~~~~~

- Attaches the current request to each form instance, allowing for
  validation logic on the form which talks to the database.
  [href]

0.8.0 (2015-11-20)
~~~~~~~~~~~~~~~~~~~

- Adds a random password generator (for pronouncable passwords).
  [href]

- Adds yubikey_client_id and yubikey_secret_key to configuration.
  [href]

0.7.5 (2015-10-26)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to convert xls/xlsx files to csv.
  [href]

- Fixes empty lines in csv tripping up the parser in unexpected ways.
  [href]

0.7.4 (2015-10-21)
~~~~~~~~~~~~~~~~~~~

- Adjacency lists are now always ordered by the value in their 'order' column.

  When adding new items to a parent, A-Z is enforced between the children, as
  long as the children are already sorted A-Z. Once this holds no longer true,
  no sorting will be imposed on the unsorted children until they are sorted
  again.
  [href]

- Adds missing space to long date formats.
  [href]

0.7.3 (2015-10-15)
~~~~~~~~~~~~~~~~~~~

- Fix being unable to load languages not conforming to our exact format.
  [href]

0.7.2 (2015-10-15)
~~~~~~~~~~~~~~~~~~~

- Improves i18n support, removing bugs, adding support for de_CH and the like.
  [href]

- The format_number function now uses the locale specific grouping/decimal
  separators.
  [href]

0.7.1 (2015-10-13)
~~~~~~~~~~~~~~~~~~~

- The csv encoding detection function will now either look for cp1152 or utf-8.
  [href]

0.7.0 (2015-10-12)
~~~~~~~~~~~~~~~~~~~

- Drops Python 2 support!
  [href]

- Adds a csv module which helps with importing flawed csv files.
  [href]

0.6.2 (2015-10-07)
~~~~~~~~~~~~~~~~~~~

- Adds an is_subpath function.
  [href]

0.6.1 (2015-10-05)
~~~~~~~~~~~~~~~~~~~

- Adds a relative_url utility function.
  [href]

- Merges multiple translations into one for faster lookups.
  [href]

0.6.0 (2015-10-02)
~~~~~~~~~~~~~~~~~~~

- Allows more than one translation directory to be set by the application. This
  enables us to use translations defined in packages outside the app. For
  example, onegov.form now keeps its own translations. Onegov.town and
  onegov.election_day simply point to onegov.form's translations to have
  them included.
  [href]

0.5.1 (2015-09-11)
~~~~~~~~~~~~~~~~~~~

- Adds an utility function to check if an object is iterable but not a string.
  [href]

0.5.0 (2015-09-10)
~~~~~~~~~~~~~~~~~~~

- E-Mails containing unicode are now sent properly.
  [href]

- Adds on_insert/on_update/on_delete signals to the session manager.
  [href]

0.4.28 (2015-09-07)
~~~~~~~~~~~~~~~~~~~

- Adds a is_uuid utility function.
  [href]

- Limits the 'subset' call for Pagination collections to once per instance.
  [href]

0.4.27 (2015-08-31)
~~~~~~~~~~~~~~~~~~~

- Fixes ``has_column`` upgrade function not checking the given table.
  [href]

- Fixes browser session chocking on an invalid cookie.
  [href]

0.4.26 (2015-08-28)
~~~~~~~~~~~~~~~~~~~

- Fixes more than one task per module crashing the upgrade.
  [href]

- Always run upgrades may now indicate if they did anything useful. If not,
  they are hidden from the upgrade output.
  [href]

0.4.25 (2015-08-24)
~~~~~~~~~~~~~~~~~~~

- The upgrades table is now prefilled with all modules and tasks, when the
  schema is first created. Fixes #8.
  [href]

- Ensures unique upgrade task function names. See #8.
  [href]

0.4.24 (2015-08-20)
~~~~~~~~~~~~~~~~~~~

- Adds support page titles consisting solely on emojis.
  [href]

- Transactions are now automatically retried once if they fail. If the second
  attempt also fails, a 409 Conflict HTTP Code is returned.
  [href]

0.4.23 (2015-08-14)
~~~~~~~~~~~~~~~~~~~

- Binds all e-mails to the transaction. Only if the transaction commits are
  the e-mails sent.

- The memcached key is now limited in its size.
  [href]

- Properly support postgres extensions.
  [href]

0.4.22 (2015-08-12)
~~~~~~~~~~~~~~~~~~~

- Fixes more unicode email sending issues.
  [href]

0.4.21 (2015-08-12)
~~~~~~~~~~~~~~~~~~~

- Adds a helper function that puts a scheme in front of urls without one.
  [href]

0.4.20 (2015-08-12)
~~~~~~~~~~~~~~~~~~~

- Linkify now escapes all html by default (except for the 'a' tag).
  [href]

- Adds proper support for unicode email addresses (only the domain and the
  text - the local part won't be supported for now as it is rare and doesn't
  even pass Chrome's or Firefox's email validation).
  [href]

- Removes the default order_by clause on adjacency lists.
  [href]

- Adds the ability to profile requests and selected pieces of code.
  [href]

0.4.19 (2015-08-10)
~~~~~~~~~~~~~~~~~~~

- Use bcrypt instead of py-bcrypt as the latter has been deprecated by passlib.
  [href]

- Support hstore types.
  [msom]

0.4.18 (2015-08-06)
~~~~~~~~~~~~~~~~~~~

- Adds a function that returns the object associated with a path.
  [href]

- Fix options not being translated on i18n-enabled forms.
  [href]

0.4.17 (2015-08-04)
~~~~~~~~~~~~~~~~~~~

- Replaces pylibmc with python-memcached, with the latter now having Python 3
  support.
  [href]

- Fix onegov-core upgrade hanging forever.
  [href]

0.4.16 (2015-07-30)
~~~~~~~~~~~~~~~~~~~

- Make sure we don't get a circulare dependency between the connection and
  the session.
  [href]

- Adds the ability to define multiple bases on the session manager.
  [href]

- Switch postgres isolation level to SERIALIZABLE for all sessions.
  [href]

0.4.15 (2015-07-29)
~~~~~~~~~~~~~~~~~~~

- Gets rid of global state used by the session manager.
  [href]

- Adds the ability to define configurations in independent methods (allowing
  for onegov.core.Framework extensions to provide their own configuration).
  [href]

- Adds functions to create and deserialize URL safe tokens.
  [msom]

0.4.14 (2015-07-17)
~~~~~~~~~~~~~~~~~~~

- Adds a sendmail command that replaces repoze.sendmail's qp.
  [href]

0.4.13 (2015-07-16)
~~~~~~~~~~~~~~~~~~~

- Adds a data transfer command to download data from a onegov cloud server and
  install them locally. Requires ssh permissions to function.

- Adds the ability to send e-mails to a maildir, instead of directly to an
  SMTP server.
  [href]

0.4.12 (2015-07-15)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to render a template directly.
  [href]

0.4.11 (2015-07-14)
~~~~~~~~~~~~~~~~~~~

- Make sure upgrade steps are only added once per record.
  [href]

- Add ``has_column`` function to upgrade context.
  [href]

0.4.10 (2015-07-14)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to render a single chameleon macro.
  [href]

0.4.9 (2015-07-13)
~~~~~~~~~~~~~~~~~~~

- Adds a relative date function to the layout.
  [href]

0.4.8 (2015-07-13)
~~~~~~~~~~~~~~~~~~~

- Adds a pagination base class for use with collections.
  [href]

- Adds an isodate format function to the layout base.
  [href]

0.4.7 (2015-07-08)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to send emails.
  [href]

0.4.6 (2015-07-06)
~~~~~~~~~~~~~~~~~~~

- Pass the request in addition to the model when dynamically building the
  form class in the form directive.
  [href]

- Fixes onegov.core.utils.rchop not working correctly.
  [href]

0.4.5 (2015-07-02)
~~~~~~~~~~~~~~~~~~~

- Fixes SQLAlchemy error occurring if more than one model used the new
  AdjacencyList base class.
  [href]

0.4.4 (2015-07-01)
~~~~~~~~~~~~~~~~~~~

- Adds a content mixin for meta/content JSON fields.
  [href]

- Adds an abstract AdjacencyList implementation (refactored from onegov.page).
  [href]

- Adds quote_plus and unquote_plus to compat imports.
  [treinhard]

0.4.3 (2015-06-30)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to format numbers through the layout class.
  [href]

0.4.2 (2015-06-29)
~~~~~~~~~~~~~~~~~~~

- Added a new 'hidden_from_public' property which may be set on any model
  handled by onegov.core Applications. If said property is found and it is
  True, anonymous users are forbidden from viewing it.

  This enables applications to dynamically set the visibilty of any model.
  [href]

0.4.1 (2015-06-26)
~~~~~~~~~~~~~~~~~~~

- Ensure that the bind schema doesn't stick around to cause test failures.
  [href]

0.4.0 (2015-06-26)
~~~~~~~~~~~~~~~~~~~

- Removes support for Python 3.3. Use 2.7 or 3.3.
  [href]

- Adds colors to the sql debug output.
  [href]

- Fix json encoder/decode not working with lists and generators.
  [href]

0.3.9 (2015-06-23)
~~~~~~~~~~~~~~~~~~~

- Moves sanitize_html and linkify functions from onegov.town to core.
  [href]

0.3.8 (2015-06-18)
~~~~~~~~~~~~~~~~~~~

- Remove parentheses from url when normalizing it.
  [href]

0.3.7 (2015-06-17)
~~~~~~~~~~~~~~~~~~~

- Adds a groupby function that returns lists instead of generators.
  [href]

- Include a layout base class useful for applications that render html.
  [href]

- Stop throwing an error if no translation is registered.
  [href]

0.3.6 (2015-06-12)
~~~~~~~~~~~~~~~~~~~

- Fix encoding error when generating the theme on certain platforms.
  [href]

- Make sure the last_change timestamp property works for single objects.
  [href]

0.3.5 (2015-06-03)
~~~~~~~~~~~~~~~~~~~

- Adds a convenience property to timestamps that returns either the modified-
  or the created-timestamp.
  [href]

0.3.4 (2015-06-03)
~~~~~~~~~~~~~~~~~~~

- Fixes SQL statement debugger failing if a statement is executed with a list
  of parameters.
  [href]

0.3.3 (2015-06-02)
~~~~~~~~~~~~~~~~~~~

- Accepts wtform's data attribute in request.get_form.
  [href]

0.3.2 (2015-05-29)
~~~~~~~~~~~~~~~~~~~

- Fix pofile loading not working in certain environments.
  [href]

0.3.1 (2015-05-28)
~~~~~~~~~~~~~~~~~~~

- Adds a method to list all schemas found in the database.
  [href]

0.3.0 (2015-05-20)
~~~~~~~~~~~~~~~~~~~

- Introduces a custom json encoder/decoder that handles additional types.
  [href]

0.2.0 (2015-05-18)
~~~~~~~~~~~~~~~~~~~

- Tighten security around static file serving.
  [href]

- Urls generated from titles no longer contain double dashes ('--').
  [href]

- The browser session now only adds a session_id to the cookies if there's
  a change in the browser session.
  [href]

- Adds the ability to count and print the sql queries that go into a single
  request.
  [href]

- Store all login information server-side. The client only gets a random
  session id scoped to the application.
  [href]

- Make sure that signatures are only valid for the origin application.
  [href]

0.1.0 (2015-05-06)
~~~~~~~~~~~~~~~~~~~

- The form directive now also accepts a factory function.
  [href]

0.0.2 (2015-05-05)
~~~~~~~~~~~~~~~~~~~

- The CSRF protection now associates a random secret with the session. The
  random secret is then used to check if the CSRF token is valid.
  [href]

- Cache the translator on the request to be slightly more efficient.
  [href]

0.0.1 (2015-04-29)
~~~~~~~~~~~~~~~~~~~

- Initial Release [href]
