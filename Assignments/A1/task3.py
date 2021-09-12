import time
import contextlib
import io
import inspect
import os


def fun_exec_time(*func):
    """
    Function which calculates execution time of arbitrary number of functions and rank them
    :param func: arbitrary number of functions
    :return: None
    """
    times = dict()
    for f in func:
        # execute function and calculation of execution time
        with contextlib.redirect_stdout(io.StringIO()) as f_:
            start_time = time.time()
            f()
            times[f.__name__] = time.time() - start_time  # write time in dict
    times = {k: v for k, v in sorted(times.items(), key=lambda item: item[1])}  # sort dict
    # print table
    print('Function | RANK | TIME ELAPSED')
    for i, t in enumerate(times):
        print(f'{t}\t    {i + 1}\t {times[t]}s')


class decorator_3:
    """
    Class decorator which calculates execution time of function, number of calls of function
    and print function's name, type, signature, type of arguments, docstring, source code and output
    and put all this information to the .txt file
    """

    def __init__(self, func):
        """
        Constructor
        :param func: function
        """
        self.func = func
        self.count = 0  # counter

    def __call__(self, *args, **kwargs):
        """
        Default function for class decorator
        :param args: positional args of function
        :param kwargs: keywords args of function
        :return: function
        """

        def print_all(*params):
            """
            Print arbitrary number of strings
            :param params: parameters to print
            :return: None
            """
            for p in params:
                print(p)

        def txt_all(name_, *params):
            """
            Append arbitrary number of strings into .txt file in txtFiles directory or create a new file if
            .txt file with passed filename does not exist
            :param name_: first part of filename of .txt file. The second part of filename is _task3
            :param params: strings to write
            :return: None
            """
            filename = "txtFiles/" + name_ + "_task3.txt"  # generate filename
            flag = "w"
            if os.path.exists(filename):
                flag = "a"  # change flag if file exists
            # write strings
            with open(filename, flag) as f:
                for p in params:
                    f.write(p)
                    f.write('\n')

        # increase call number
        self.count += 1
        # execute function and calculation of execution time
        with contextlib.redirect_stdout(io.StringIO()) as f_:
            start_time = time.time()
            self.func(*args, **kwargs)
            end_time = time.time()
        out = f_.getvalue()  # result of function printing
        # generate and print all information
        exe_time_call = f'{self.func.__name__} call {self.count} executed in {end_time - start_time} sec'
        name = f'Name:\n {self.func.__name__}'
        type_ = f'Type:\n {type(self.func)}'
        sign = f'Sign:\n {inspect.signature(self.func)}'
        args_ = f'Args:\n positional {args}\n key-worded {kwargs}'
        doc = f'Doc:\n{inspect.getdoc(self.func)}'
        source = f'Source:\n{inspect.getsource(self.func)}'
        output = f'Output:\n{out}'
        print_all(exe_time_call, name, type_, sign, args_, doc, source, output)
        # write all information into .txt
        txt_all(self.func.__name__, exe_time_call, name, type_, sign, args_, doc, source, output)

        return self.func
