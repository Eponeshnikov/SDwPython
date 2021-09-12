import time
import contextlib
import io
import inspect


def decorator_2(f):
    def wrapper(*args, **kwargs):
        def print_all(*params):
            for p in params:
                print(p)
        wrapper.count += 1
        with contextlib.redirect_stdout(io.StringIO()) as f_:
            start_time = time.time()
            f(*args, **kwargs)
            end_time = time.time()
        out = f_.getvalue()
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
