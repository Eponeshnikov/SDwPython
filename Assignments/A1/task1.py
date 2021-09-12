import time
import contextlib
import io


def decorator_1(f):
    """
    Function decorator which calculates execution time of function and number of calls of function
    :param f: function
    :return: modified function
    """
    def wrapper(*args, **kwargs):
        # increase call number
        wrapper.count += 1
        # execute function and calculation of execution time
        with contextlib.redirect_stdout(io.StringIO()) as _f:
            start_time = time.time()
            f(*args, **kwargs)
            end_time = time.time()
        # printing information about call number and execution time
        print(f'{f.__name__} call {wrapper.count} executed in {end_time - start_time} sec')
    wrapper.count = 0

    return wrapper
