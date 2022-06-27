
class IdError(Exception):
    pass


class IdIsNotNumericException(IdError):
    pass


class IdNotFoundException(IdError):
    pass


class IdAlreadyExistsException(IdError):
    pass


class BookError(Exception):
    pass


class BookNotAvailableException(BookError):
    pass


class OptionError(Exception):
    pass


class OptionValueException(OptionError):
    pass


class OptionIndexException(OptionError):
    pass


class DateError(Exception):
    pass


class InvalidDateException(DateError):
    pass

