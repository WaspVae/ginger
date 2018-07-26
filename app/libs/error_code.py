from .error import APIException


class Success(APIException):
    code = 201
    msg = 'success'
    error_code = 0


class DeleteSuccess(APIException):
    code = 202
    msg = 'delete success'
    error_code = -1


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 40000


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 40001


class DuplicateGift(APIException):
    code = 400
    msg = 'the current book has already in gift'
    error_code = 40002


class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 40100


class Forbidden(APIException):
    code = 403
    msg = 'forbidden, not have authorization'
    error_code = 40300


class NotFound(APIException):
    code = 404
    msg = 'the source are not found'
    error_code = 40400


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 50000
