import time
import sys
import io
import contextlib


def fun_exec_time():
    """
    usage: compare.py [files]
    This program ...
    :return:
    """
    func = sys.argv[1:]
    if len(func) == 0:
        print(fun_exec_time.__doc__)
        return 0
    times = dict()
    for f in func:
        with contextlib.redirect_stdout(io.StringIO()) as _f:
            start_time = time.time()
            exec(open(f).read(), globals())
            times[f] = time.time() - start_time
    times = {k: v for k, v in sorted(times.items(), key=lambda item: item[1])}
    print('PROGRAM | RANK | TIME ELAPSED')
    for i, t in enumerate(times):
        print(f'{t}\t    {i + 1}\t {times[t]}s')


if __name__ == '__main__':
    fun_exec_time()
