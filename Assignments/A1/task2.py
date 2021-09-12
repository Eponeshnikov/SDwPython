import time
import contextlib
import io
import inspect


def decorator_2(f):
    """
    Function decorator which calculates execution time of function, number of calls of function
    and print function's name, type, signature, type of arguments, docstring, source code and output
    :param f: function
    :return: modified function
    """

    def wrapper(*args, **kwargs):
        # function to print parameters of function
        def print_all(*params):
            """
            Print arbitrary number of strings
            :param params: parameters to print
            :return: None
            """
            for p in params:
                print(p)

        # increase call number
        wrapper.count += 1
        # execute function and calculation of execution time
        with contextlib.redirect_stdout(io.StringIO()) as f_:
            start_time = time.time()
            f(*args, **kwargs)
            end_time = time.time()
        out = f_.getvalue()  # result of function printing
        # generate and print all information
        exe_time_call = f'{f.__name__} call {wrapper.count} executed in {end_time - start_time} sec'
        name = f'Name:\n {f.__name__}'
        type_ = f'Type:\n {type(f)}'
        sign = f'Sign:\n {inspect.signature(f)}'
        args_ = f'Args:\n positional {args}\n key-worded {kwargs}'
        doc = f'Doc:\n{inspect.getdoc(f)}'
        source = f'Source:\n{inspect.getsource(f)}'
        output = f'Output:\n{out}'
        print_all(exe_time_call, name, type_, sign, args_, doc, source, output)

    wrapper.count = 0
    return wrapper
