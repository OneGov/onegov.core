class CSVError(Exception):
    pass


class MissingColumnsError(CSVError):
    def __init__(self, columns):
        self.columns = columns


class AmbiguousColumnsError(CSVError):
    def __init__(self, columns):
        self.columns = columns


class DuplicateColumnNamesError(CSVError):
    pass


class InvalidFormatError(CSVError):
    pass


class EmptyFileError(CSVError):
    pass


class EmptyLineInFileError(CSVError):
    pass


class AlreadyLockedError(Exception):
    """ Raised if :func:`onegov.core.locking.lock` fails to acquire a lock. """

    def __init__(self, namespace, key):
        self.namespace = namespace
        self.key = key


class WorkerError(Exception):
    pass


class TooManyWorkersError(WorkerError):
    pass


class TooManyInstancesError(WorkerError):
    pass
