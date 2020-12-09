"""Arithmetic Logic Unit Simulator

This is an attempt to create an ALU starting from just NOT and AND.
"""


import sys
import inspect


def main(argv):
    x = int(argv[0])
    y = int(argv[1])

    result=bin_digits_to_int(four_bit_adder(
            *int_to_bin_digits(x),
            *int_to_bin_digits(y)))

    print(f"{x} + {y} = {result}")


def NOT(a):
    return a ^ 1


def AND(a, b):
    return a and b


def NAND(a, b):
    return NOT(AND(a, b))


def OR(a, b):
    return NAND(NOT(a), NOT(b))


def XOR(a,b ):
    return AND(OR(a, b), NAND(a, b))


def half_adder(a, b):
    s = XOR(a, b)
    c = AND(a, b)

    return (c, s)


def full_adder(a, b, c_in):
    c_0, s_0 = half_adder(a, b)
    c_1, s_1 = half_adder(c_in, s_0)

    return (OR(c_0, c_1), s_1)


def four_bit_adder(a_3, a_2, a_1, a_0, b_3, b_2, b_1, b_0):
    c_0, s_0 = full_adder(a_0, b_0, 0)
    c_1, s_1 = full_adder(a_1, b_1, c_0)
    c_2, s_2 = full_adder(a_2, b_2, c_1)
    c_3, s_3 = full_adder(a_3, b_3, c_2)

    return (c_3, s_3, s_2, s_1, s_0)


def truth_table(func):
    # FIXME: param names longer than 1 char cause headings to be misaligned
    params = inspect.signature(func).parameters

    cases = (
        tuple((i//2**j)%2 for j in range(len(params)))
        for i in range(2**len(params)))

    table = " ".join(params)
    table += f" {func.__name__}"
    table += f"\n{'-'*len(table)}\n"

    for case in cases:
        for arg in case:
            table += f"{arg} "

        table += f"{func(*case)}\n"

    return table


def int_to_bin_digits(int_):
    return tuple(map(int, f"{int_:0>4b}"))


def bin_digits_to_int(digits):
    return int("".join(map(str, digits)), base=2)


if __name__ == "__main__":
    main(sys.argv[1:])
