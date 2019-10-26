"""
    bricklink.exceptions
    --------------------

    A module providing Bricklink exceptions
"""


class InvalidResponseException(Exception):
    pass


class InvalidURIException(Exception):
    pass


class InvalidRequestBodyException(Exception):
    pass


class ParameterMissingOrInvalidException(Exception):
    pass


class BadOauthRequestException(Exception):
    pass


class PermissionDeniedException(Exception):
    pass


class ResourceNotFoundException(Exception):
    pass


class MethodNotAllowedException(Exception):
    pass


class UnsupportedMediaTypeException(Exception):
    pass


class ResourceUpdateNotAllowedException(Exception):
    pass


class InternalServerErrorException(Exception):
    pass


class UnspecifiedException(Exception):
    pass


class InvalidParameterException(Exception):
    pass
