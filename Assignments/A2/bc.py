"""
Use python bc.py to get help
"""
import io
import os
import sys
import dis
import marshal
import contextlib
import py_compile


def parser():
    """
    Parsing command line
    :return: command, flags with values
    """
    full_cmd_arguments = sys.argv
    argument_list = full_cmd_arguments[1:]
    first_arg = None
    if argument_list[0][0] != '-':
        first_arg = argument_list[0]
    _args = [[argument_list[i] for i, j in enumerate(argument_list) if j[0] == '-'],
             [argument_list[i + 1] for i, j in enumerate(argument_list) if j[0] == '-']]
    return first_arg, _args


def extract_opcodes(spl_data):
    """
    Parsing dis.dis() func
    :param spl_data: input data
    :return: list of opcodes with arguments
    """
    tmp_nums = [str(i) for i in range(10)]
    opcodes = []
    for i in spl_data:
        for e, j in enumerate(i.split()):
            if sum(1 for c in j if c.isupper()) >= len(j) - 3 and j[0] not in tmp_nums and j[0].isupper() and e <= 3:
                if '(' in i.split()[len(i.split()) - 1] and ')' in i.split()[len(i.split()) - 1]:
                    n = i.split()[len(i.split()) - 1][1:len(i.split()[len(i.split()) - 1]) - 1]
                else:
                    n = ''
                opcodes.append([j, n])
    return opcodes


def disassemb(file):
    """
    Parsing dis.dis() func
    :param file: file to parse
    :return: list of opcodes with arguments
    """
    with contextlib.redirect_stdout(io.StringIO()) as _f:
        dis.dis(file)
    out = _f.getvalue().split('\n')
    opcodes = extract_opcodes(out)
    return opcodes


def gen_opcodes_list_and_set(all_opcodes):
    """
    Generates list with number of opcodes and set of opcodes
    :param all_opcodes: dict
    :return: list with number of opcodes and set of opcodes
    """
    uniq_opcodes = set()
    num_opcodes = []
    for code in all_opcodes:
        res = [i[0] for i in all_opcodes[code]]
        uniq_opcodes.update(res)
    for code in all_opcodes:
        res = [i[0] for i in all_opcodes[code]]
        for oc in uniq_opcodes:
            tmp = [oc, res.count(oc), code]
            num_opcodes.append(tmp)
    return num_opcodes, uniq_opcodes


def gen_list_4_print(num_opcodes, uniq_opcodes):
    """
    Generates list to print on table
    :param num_opcodes: list of opcodes
    :param uniq_opcodes: set of opcodes
    :return: list to print on table
    """
    num_opcodes = sorted(num_opcodes, key=lambda x: x[1], reverse=True)
    num_opcodes_1 = num_opcodes.copy()
    for_print = []
    for i in range(len(uniq_opcodes)):
        op = num_opcodes_1[0][0]
        ids = [j for j in range(len(num_opcodes_1)) if num_opcodes_1[j][0] == op]
        for_del = []
        for id in ids:
            for_del.append(num_opcodes_1[id])
        for_print.append(for_del)
        for d in for_del:
            num_opcodes_1.remove(d)
    return for_print


def gen_head(pys, length):
    """
    Generates head of table
    :param pys: names of files
    :param length: length to field
    :return: head
    """
    head = 'INSTRUCTION   '  # 14
    for k in pys:
        if len(k) > length:
            py = k[:length - 2] + '..'
        elif len(k) < length:
            py = ' ' * (length - len(k) - (length - len(k)) // 2) + k + ' ' * ((length - len(k)) // 2)
        else:
            py = k
        head += f'|{py}'
    return head


def gen_rows(pys, length, for_print):
    """
    Generates rows of table
    :param pys: names of files
    :param length: length to field
    :param for_print: list to print
    :return: rows
    """
    rows_print = []
    for row in for_print:
        row_print = row[0][0]

        for i, k in enumerate(pys):
            for j in row:
                if j[2] == k:
                    if i == 0:
                        spaces = 15 - len(row_print) + length // 2
                    else:
                        spaces = length - len(str(j[1])) + 1
                    row_print += ' ' * spaces + str(j[1])
        rows_print.append(row_print)
    return rows_print


def txt_all(name_, *params):
    """
    Append arbitrary number of strings into .txt file in txtFiles directory or create a new file if
    .txt file with passed filename does not exist
    :param name_: name of filename of .txt file.
    :param params: strings to write
    :return: None
    """
    filename = name_ + ".txt"  # generate filename
    flag = "w"
    if os.path.exists(filename):
        flag = "a"  # change flag if file exists
    # write strings
    with open(filename, flag) as f:
        for p in params:
            f.write(p)
            f.write('\n')


def bc():
    """
    usage: bc.py action [-flag value]*
    !!!Add flag before each file or src!!!
    This program ...
    compile
        -py file.py compile file into bytecode and store it as file.pyc
        -s "src" compile src into bytecode and store it as out.pyc
    print
        -py src.py
        -pyc src.pyc produce human-readable bytecode from python file produce human-readable bytecode from compiled .pyc file
        -s "src" produce human-readable bytecode from normal string
    compare -format src [-format src]+
        produce bytecode comparison for giving sources (prints and saves to result.txt)
        (supported formats -py, -pyc, -s)
    :return: None
    """
    command, args = parser()
    if command is None:
        print(bc.__doc__)
        return 0
    file = None
    compile_name = None
    all_opcodes = dict()
    for i in range(len(args[0])):
        if args[0][i] == '-py':
            with open(args[1][i]) as f:
                file = f.read()
                compile_name = args[1][i]
        elif args[0][i] == '-pyc':
            header = 12
            if sys.version_info >= (3, 7):
                header = 16
            with open(args[1][i], 'rb') as f:
                f.seek(header)
                file = marshal.load(f)
        elif args[0][i] == '-s':
            file = args[1][i]
            compile_name = 'out.py'
        opcodes = disassemb(file)
        if command == "print":
            print(f"==== Start parse opcodes in '{args[1][i]}' ====")
            for o in opcodes:
                print(o[0], o[1])
            print(f"==== End of parsing ====")
        elif command == "compile" and args[0][i] != '-pyc':
            if args[0][i] == '-s':
                with open(compile_name, 'w') as f:
                    f.write(args[1][i])
                py_compile.compile(compile_name, cfile=compile_name + "c")
                os.remove(compile_name)
            else:
                py_compile.compile(compile_name, cfile=compile_name + "c")
        elif command == "compare":
            all_opcodes[compile_name] = opcodes

    if command == "compare":
        num_opcodes, uniq_opcodes = gen_opcodes_list_and_set(all_opcodes)
        for_print = gen_list_4_print(num_opcodes, uniq_opcodes)
        length = 11
        pys = all_opcodes.keys()
        head = gen_head(pys, length)
        rows_print = gen_rows(pys, length, for_print)

        with contextlib.redirect_stdout(io.StringIO()) as _f:
            print(head)
            for row_print in rows_print:
                print(row_print)
        out = _f.getvalue()
        print(out)
        txt_all("result", out)


if __name__ == '__main__':
    bc()
