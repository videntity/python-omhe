class OMHEError(Exception): pass
class InvalidCommandError(OMHEError):pass
class InvalidValueError(OMHEError):pass
class InvalidMessageError(OMHEError):pass
class InvalidHelperFormatError(OMHEError):pass
class NotADatetimeObjectError(OMHEError):pass
class DatetimeFormatError(OMHEError):pass