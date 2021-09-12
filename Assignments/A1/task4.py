import time
import datetime
import contextlib
import io
import inspect
import os


class decorator_4_1:
    """
    Class decorator which which calculates execution time of function, number of calls of function
    and print function's name, type, signature, type of arguments, docstring, source code and output
    and put all this information to the .txt file. If an error occurs while the function is running,
    the error message is written to the .txt file
    """

    def __init__(self, func):
        """
        Constructor
        :param func: function
        """
        self.func = func
        self.count = 0

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
            :param name_: first part of filename of .txt file. The second part of filename is _task4_1
            :param params: strings to write
            :return: None
            """
            filename = "txtFiles/" + name_ + "_task4_1.txt"  # generate filename
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
        try:  # try execute function
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
        except Exception as e:  # if error in function
            print("Hey, I caught an error in your function :)")
            name_er = self.func.__name__ + "_err"  # special err name
            err = str(e) + "\t" + str(datetime.datetime.utcnow())  # err string with timestamp
            txt_all(name_er, err)  # write err string

        return self.func


def decorator_4_2(f):
    """
    Function decorator  which calculates execution time of function, number of calls of function
    and print function's name, type, signature, type of arguments, docstring, source code and output
    If an error occurs while the function is running, the error message is written to the .txt file
    """
    def wrapper(*args, **kwargs):
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
            :param name_: first part of filename of .txt file. The second part of filename is _task4_2
            :param params: strings to write
            :return: None
            """
            filename = "txtFiles/" + name_ + "_task4_2.txt"  # generate filename
            flag = "w"
            if os.path.exists(filename):
                flag = "a"  # change flag if file exists
            # write strings
            with open(filename, flag) as ff:
                for p in params:
                    ff.write(p)
                    ff.write('\n')

        # increase call number
        wrapper.count += 1
        # execute function and calculation of execution time
        try:  # try execute function
            with contextlib.redirect_stdout(io.StringIO()) as f_:
                start_time = time.time()
                f(*args, **kwargs)
                end_time = time.time()
            # generate and print all information
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
            name_er = f.__name__ + "_err"  # special err name
            err = str(e) + "\t" + str(datetime.datetime.utcnow())  # err string with timestamp
            txt_all(name_er, err)  # write err string

    wrapper.count = 0
    return wrapper
