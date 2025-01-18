from celery import Celery

from proj.tasks import add, mul, xsum


def main():
    print(add.delay(4, 4).get())
    print(mul.delay(4, 4).get())
    print(xsum.delay([1, 2, 3, 4, 5]).get())


if __name__ == "__main__":
    main()
