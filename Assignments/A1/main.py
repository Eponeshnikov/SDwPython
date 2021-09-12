from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3, fun_exec_time
from task4 import decorator_4_1, decorator_4_2


def pascal_triangle(n=100):
    """
    Python program to print Pascal's Triangle
    :param n: number of rows (default n = 100)
    :return: None
    """
    trow = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(trow)
        trow = [l + r for l, r in zip(trow + y, y + trow)]


def sq_sol(a, b, c, d=0):
    """
    Python program to solve quadratic equation (ax^2 + bx + c = d)
    :param a: argument before x^2
    :param b: argument before x
    :param c: free argument
    :param d: argument after equals sign (default d = 0)
    :return: x1 and x2
    """
    import math
    c -= d
    D = b ** 2 - 4 * a * c
    x1 = (-b - math.sqrt(D)) / (2 * a)
    x2 = (-b + math.sqrt(D)) / (2 * a)
    print(x1, x2)
    return x1, x2


cube = lambda x: x ** 3
cube.__name__ = "cube"
cube.__doc__ = f"""Python function to calculate cube of number \n:param x: cube number \n:return: cube of number"""
quad = lambda x: x ** 2
quad.__name__ = "quad"
quad.__doc__ = f"""Python function to calculate quad of number \n:param x: quad number \n:return: quad of number"""


def test_task1():
    """
    Function which call functions using function decorator from task1
    :return: None
    """
    # Apply decorator from task1
    pascal_triangle_t1 = decorator_1(pascal_triangle)
    sq_sol_t1 = decorator_1(sq_sol)
    cube_t1 = decorator_1(cube)
    quad_t1 = decorator_1(quad)
    # call decorated functions with different parameters
    for i in range(1, 10, 3):
        pascal_triangle_t1(i)
        cube_t1(i)
        quad_t1(i)
        sq_sol_t1(a=1, b=-i - i, c=i * i)
        print('\n')


def test_task2():
    """
    Function which call functions using function decorator from task2
    :return: None
    """
    # Apply decorator from task2
    pascal_triangle_t2 = decorator_2(pascal_triangle)
    sq_sol_t2 = decorator_2(sq_sol)
    cube_t2 = decorator_2(cube)
    quad_t2 = decorator_2(quad)
    # call decorated functions with different parameters
    for i in range(1, 10, 5):
        pascal_triangle_t2(i)
        print("-" * 30)
        cube_t2(i)
        print("-" * 30)
        quad_t2(i)
        print("-" * 30)
        sq_sol_t2(a=1, b=-i - i, c=i * i)
        print("-" * 30)


def test_task3():
    """
    Function which call functions using class decorator from task3 and rank decorated functions
    :return: None
    """
    # Apply decorator from task3
    pascal_triangle_t3 = decorator_3(pascal_triangle)
    sq_sol_t3 = decorator_3(sq_sol)
    cube_t3 = decorator_3(cube)
    quad_t3 = decorator_3(quad)
    # call decorated functions with different parameters
    for i in range(1, 10, 5):
        pascal_triangle_t3(i)
        print("-" * 30)
        cube_t3(i)
        print("-" * 30)
        quad_t3(i)
        print("-" * 30)
        sq_sol_t3(a=1, b=-i - i, c=i * i)
        print("-" * 30)

    # Initialize functions with default parameters to pass them to fun_exec_time
    pascal_triangle_t3_time = pascal_triangle_t3
    pascal_triangle_t3_time.__name__ = "pascal_triangle_t3"
    sq_sol_t3_time = lambda a=1, b=-5, c=6: sq_sol_t3(a, b, c)
    sq_sol_t3_time.__name__ = "sq_sol_t3"
    cube_t3_time = lambda x=100: cube_t3(x)
    cube_t3_time.__name__ = "cube_t3"
    quad_t3_time = lambda x=100: quad_t3(x)
    quad_t3_time.__name__ = "quad_t3"

    # calculate rank table
    # calling this function, more information will be written to the .txt file
    fun_exec_time(pascal_triangle_t3_time, sq_sol_t3_time, quad_t3_time, cube_t3_time)


def test_task4_1():
    """
    Function which call functions using class decorator from task3, rank decorated functions and test
    decorated functions for catching errors
    :return: None
    """
    # Apply decorator from task4
    pascal_triangle_t4 = decorator_4_1(pascal_triangle)
    sq_sol_t4 = decorator_4_1(sq_sol)
    cube_t4 = decorator_4_1(cube)
    quad_t4 = decorator_4_1(quad)
    # call decorated functions with different parameters
    for i in range(1, 10, 5):
        pascal_triangle_t4(i)
        print("-" * 30)
        cube_t4(i)
        print("-" * 30)
        quad_t4(i)
        print("-" * 30)
        sq_sol_t4(a=1, b=-i - i, c=i * i)
        print("-" * 30)

    # Initialize functions with default parameters to pass them to fun_exec_time
    pascal_triangle_t4_time = pascal_triangle_t4
    pascal_triangle_t4_time.__name__ = "pascal_triangle_t4"
    sq_sol_t4_time = lambda a=1, b=-5, c=6: sq_sol_t4(a, b, c)
    sq_sol_t4_time.__name__ = "sq_sol_t4"
    cube_t4_time = lambda x=100: cube_t4(x)
    cube_t4_time.__name__ = "cube_t4"
    quad_t4_time = lambda x=100: quad_t4(x)
    quad_t4_time.__name__ = "quad_t4"

    # calculate rank table
    # calling this function, more information will be written to the .txt file
    fun_exec_time(pascal_triangle_t4_time, sq_sol_t4_time, quad_t4_time, cube_t4_time)

    # test errors catching
    sq_sol_t4(5, -5, 6)
    sq_sol_t4(5, -5, 4)
    pascal_triangle_t4("10")
    cube_t4(["10"])
    cube_t4(["1"])
    quad_t4(["10"])


def test_task4_2():
    """
    Function which call functions using function decorator from task3, rank decorated functions and test
    decorated functions for catching errors
    :return: None
    """
    # Apply decorator from task4
    pascal_triangle_t4 = decorator_4_2(pascal_triangle)
    sq_sol_t4 = decorator_4_2(sq_sol)
    cube_t4 = decorator_4_2(cube)
    quad_t4 = decorator_4_2(quad)
    # call decorated functions with different parameters
    for i in range(1, 10, 5):
        pascal_triangle_t4(i)
        print("-" * 30)
        cube_t4(i)
        print("-" * 30)
        quad_t4(i)
        print("-" * 30)
        sq_sol_t4(a=1, b=-i - i, c=i * i)
        print("-" * 30)

    # Initialize functions with default parameters to pass them to fun_exec_time
    pascal_triangle_t4_time = pascal_triangle_t4
    pascal_triangle_t4_time.__name__ = "pascal_triangle_t4"
    sq_sol_t4_time = lambda a=1, b=-5, c=6: sq_sol_t4(a, b, c)
    sq_sol_t4_time.__name__ = "sq_sol_t4"
    cube_t4_time = lambda x=100: cube_t4(x)
    cube_t4_time.__name__ = "cube_t4"
    quad_t4_time = lambda x=100: quad_t4(x)
    quad_t4_time.__name__ = "quad_t4"

    # calculate rank table
    # calling this function, more information will be written to the .txt file
    fun_exec_time(pascal_triangle_t4_time, sq_sol_t4_time, quad_t4_time, cube_t4_time)

    # test errors catching
    sq_sol_t4(5, -5, 6)
    sq_sol_t4(5, -5, 4)
    pascal_triangle_t4("10")
    cube_t4(["10"])
    cube_t4(["1"])
    quad_t4(["10"])


def main():
    """
    Main function which executes all tests
    :return: None
    """
    print("="*30)
    print("===== Testing task 1 =====")
    test_task1()
    print("=" * 30)
    print("===== Testing task 2 =====")
    test_task2()
    print("=" * 30)
    print("===== Testing task 3 =====")
    test_task3()
    print("=" * 30)
    print("===== Testing task 4 =====")
    print("----- Class decorator ----")
    test_task4_1()
    print("----- Function decorator ----")
    test_task4_2()


if __name__ == "__main__":
    main()
