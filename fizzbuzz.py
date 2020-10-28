import sys


def main(argv):
    try:
        n = int(argv[0])

    except IndexError:
        print("Error: no argument given")
        sys.exit(1)

    except ValueError:
        print("Error: argument must be an integer")
        sys.exit(1)

    fizzbuzz(n)


def fizzbuzz(n):
    for i in range(1, n+1):
        print(("fizz" if i%3 == 0 else "") + ("buzz" if i%5 == 0 else "") or i)


if __name__ == "__main__":
    main(sys.argv[1:])
