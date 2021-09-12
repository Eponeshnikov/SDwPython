import time
import contextlib
import io
import inspect
import os


def fun_exec_time(**func):
    times = dict()
    for f in func:
        with contextlib.redirect_stdout(io.StringIO()) as f_:
            start_time = time.time()
            func[f]()
            times[f] = time.time() - start_time
    times = {k: v for k, v in sorted(times.items(), key=lambda item: item[1])}
    print('Function | RANK | TIME ELAPSED')
    for i, t in enumerate(times):
        print(f'{t}\t    {i + 1}\t {times[t]}s')


class decorator_3:

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        def print_all(*params):
            for p in params:
                print(p)

        def txt_all(name_, *params):
            if name_ == "<lambda>":
                name_ = "lambda"
            filename = "txtFiles/" + name_ + ".txt"
            flag = "w"
            if os.path.exists(filename):
                flag = "a"
            with open(filename, flag) as f:
                for p in params:
                    f.write(p)
                    f.write('\n')

        self.count += 1
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
        output = f'Output:\n {out}'
        print_all(exe_time_call, name, type_, sign, args_, doc, source, output)
        txt_all(self.func.__name__, exe_time_call, name, type_, sign, args_, doc, source, output)

        return self.func
