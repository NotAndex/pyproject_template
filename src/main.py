from module_a.simple_math import add, div, mul, sub
from module_b.simple_fun import bar, foo


def main():
    a, b, c, d = add(2, 2), sub(2, 2), mul(2, 2), div(2, 2)

    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print(f"d = {d}")
    foo()
    bar()


if __name__ == "__main__":
    main()
