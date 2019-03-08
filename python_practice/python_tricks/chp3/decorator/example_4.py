

# -------- Decorating Functions That Accepts Arguments -------- #
def proxy(func):
    # Collect all positional and keyword arguments and stores them in variables.
    # The wrapper closure then forwards the collected arguments to the
    # original input function using the * and ** “argument unpacking” operators.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'[Before] TRACE: calling {func.__name__}() with args:{args}, kwargs:{kwargs}')
        original_result = func(*args, **kwargs)
        print(f'[After] TRACE: {func.__name__}() returned {original_result!r}')
        return original_result
    return wrapper


@trace
def greet(name, line):
    return f'{name}: {line}'


print(greet('Chun-Ming', 'Hi, there!'))

