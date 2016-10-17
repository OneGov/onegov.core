from sedate import standardize_date, to_timezone
from sqlalchemy_utils.types import DateTimeRangeType
from sqlalchemy import types


class UTCDateTimeRange(DateTimeRangeType):
    """ Stores dates ranges as UTC.

    Internally, they are stored as timezone naive, because Postgres takes
    the local timezone into account when working with timezones. Values taken
    and values returned are forced to be timezone-aware though.

    """

    def process_bind_param(self, value, engine):
        if value is not None:
            value = tuple(
                to_timezone(v, 'UTC').replace(tzinfo=None) for v in value)

            import pdb; pdb.set_trace()

            return super().process_bind_param(value, engine)

    def process_result_value(self, value, engine):
        import pdb; pdb.set_trace()
