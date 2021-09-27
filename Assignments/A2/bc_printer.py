import io
import re
import sys
import dis
import contextlib


def parser():
    full_cmd_arguments = sys.argv
    argument_list = full_cmd_arguments[1:]
    first_arg = None
    if argument_list[0][0] != '-':
        first_arg = argument_list[0]
    _args = [[argument_list[i] for i, j in enumerate(argument_list) if j[0] == '-'],
             [argument_list[i + 1] for i, j in enumerate(argument_list) if j[0] == '-']]
    return first_arg, _args


def extract_opcodes(spl_data):
    tmp_nums = [str(i) for i in range(10)]
    opcodes = []
    for i in spl_data:
        for j in i.split():
            if sum(1 for c in j if c.isupper()) == len(j) - 1 and j[0] not in tmp_nums:
                if '(' in i.split()[len(i.split()) - 1] and ')' in i.split()[len(i.split()) - 1]:
                    n = i.split()[len(i.split()) - 1][1:len(i.split()[len(i.split()) - 1]) - 1]
                else:
                    n = ''
                opcodes.append([j, n])
    return opcodes


def bc_print():
    command, args = parser()
    for i in range(len(args[0])):
        if args[0][i] == '-py':
            with contextlib.redirect_stdout(io.StringIO()) as _f:
                module = __import__(args[1][i][:-3])
            with contextlib.redirect_stdout(io.StringIO()) as _f:
                dis.dis(module)
            print(f"==== Start parse opcodes in {args[1][i]} ====")
            out = _f.getvalue().split('\n')
            opcodes = extract_opcodes(out)
            for o in opcodes:
                print(o[0], o[1])
            print(f"==== End of parsing ====")


if __name__ == '__main__':
    bc_print()
