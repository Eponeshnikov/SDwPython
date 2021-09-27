import time
import sys
import io
import contextlib


def fun_exec_time():
    func = sys.argv[1:]
    if len(func) > 0:
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
    else:
        print("usage: compare.py [files]\nThis program creates a "
              "neat table out of their execution time starting with the fastest.")


if __name__ == '__main__':
    fun_exec_time()
