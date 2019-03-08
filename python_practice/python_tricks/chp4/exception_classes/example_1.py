class BaseValidationError(ValueError):
    pass


class NameTooShortError(BaseValidationError):
    pass


class NameTooLongError(BaseValidationError):
    pass


class NameTooCuteError(BaseValidationError):
    pass


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)


def handle_validation_error(err):
    print('[ERROR] catch an error: the length of `{}` is too short'.format(err))


if __name__ == '__main__':

    try:
        validate('joe')
    except BaseValidationError as err:
        handle_validation_error(err)
