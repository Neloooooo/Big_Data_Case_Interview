import datetime
import time

"""
写一个装饰器，打印函数执行时间
"""


def print_run_time(is_open: bool = False):
    def decorator(fn):
        def inner(word):
            start_time = None
            if is_open:
                start_time = datetime.datetime.now()
                print(f'start time: {start_time}')
            fn(word)
            if is_open:
                end_time = datetime.datetime.now()
                print(f'end time: {end_time}')
                print(f'total second: {(end_time - start_time).seconds}')
        return inner
    return decorator


@print_run_time(True)
def run(word):
    print('run..')
    time.sleep(3)
    print(f'say: {word}')


if __name__ == '__main__':
    run('hello')
