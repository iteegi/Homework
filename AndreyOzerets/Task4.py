# Task 7.4

from contextlib import ContextDecorator
from time import sleep, time


class SupressDecorator(ContextDecorator):
    """Decorator for supressing exceptions"""

    def __init__(self, file) -> None:
        super().__init__()
        self._file = file

    def __enter__(self):
        print('Starting')
        self._start = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _stop = str(time() - self._start)
        message = f'Execution time is {_stop}'
        if exc_type:
            with open(self._file, 'w') as f:
                f.write(message)
        else:
            print(message)

        print('Finishing')
        return True


@SupressDecorator('log-file.txt')
def fun():
    """Something very important"""

    for _ in range(50):
        sleep(0.01)


if __name__ == '__main__':

    with SupressDecorator('log-file.txt'):
        for _ in range(50):
            sleep(0.01)
            raise Exception('---')