import time
import sys
import io
import contextlib


def fun_exec_time():
    func = sys.argv[1:]
    times = dict()
    for f in func:
        with contextlib.redirect_stdout(io.StringIO()) as _f:
            start_time = time.time()
            exec(open(f).read())
            times[f] = time.time() - start_time
    times = {k: v for k, v in sorted(times.items(), key=lambda item: item[1])}
    print('PROGRAM | RANK | TIME ELAPSED')
    for i, t in enumerate(times):
        print(f'{t}\t    {i + 1}\t {times[t]}s')


if __name__ == '__main__':
    fun_exec_time()
