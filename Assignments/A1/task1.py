import time
import contextlib
import io


def decorator_1(f):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        with contextlib.redirect_stdout(io.StringIO()) as _f:
            start_time = time.time()
            f(*args, **kwargs)
            end_time = time.time()
        print(f'{f.__name__} call {wrapper.count} executed in {end_time - start_time} sec')
    wrapper.count = 0

    return wrapper
