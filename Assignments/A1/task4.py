import time
import datetime
import contextlib
import io
import inspect
import os


class decorator_4_1:

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        def print_all(*params):
            for p in params:
                print(p)

        def txt_all(name_, *params):
            filename = "txtFiles/" + name_ + "_task4_1.txt"
            flag = "w"
            if os.path.exists(filename):
                flag = "a"
            with open(filename, flag) as f:
                for p in params:
                    f.write(p)
                    f.write('\n')

        self.count += 1
        try:
            with contextlib.redirect_stdout(io.StringIO()) as f_:
                start_time = time.time()
                self.func(*args, **kwargs)
                end_time = time.time()
            out = f_.getvalue()
            exe_time_call = f'{self.func.__name__} call {self.count} executed in {end_time - start_time} sec'
            name = f'Name:\n {self.func.__name__}'
            type_ = f'Type:\n {type(self.func)}'
            sign = f'Sign:\n {inspect.signature(self.func)}'
            args_ = f'Args:\n positional {args}\n key-worded {kwargs}'
            doc = f'Doc:\n{inspect.getdoc(self.func)}'
            source = f'Source:\n{inspect.getsource(self.func)}'
            output = f'Output:\n{out}'
            print_all(exe_time_call, name, type_, sign, args_, doc, source, output)
            txt_all(self.func.__name__, exe_time_call, name, type_, sign, args_, doc, source, output)
        except Exception as e:
            print("Hey, I caught an error in your function :)")
            name_er = self.func.__name__ + "_err"
            err = str(e) + "\t" + str(datetime.datetime.utcnow())
            txt_all(name_er, err)

        return self.func


def decorator_4_2(f):
    def wrapper(*args, **kwargs):
        def print_all(*params):
            for p in params:
                print(p)

        def txt_all(name_, *params):
            filename = "txtFiles/" + name_ + "_task4_2.txt"
            flag = "w"
            if os.path.exists(filename):
                flag = "a"
            with open(filename, flag) as f:
                for p in params:
                    f.write(p)
                    f.write('\n')

        wrapper.count += 1
        try:
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
        except Exception as e:
            print("Hey, I caught an error in your function :)")
            name_er = f.__name__ + "_err"
            err = str(e) + "\t" + str(datetime.datetime.utcnow())
            txt_all(name_er, err)

    wrapper.count = 0
    return wrapper
