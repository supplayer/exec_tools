from gevent import monkey; monkey.patch_all()
from exectools import Coroutine
import gevent


def count_num(a, b):
    print(f"Start: {a}")
    gevent.sleep(10)
    return a/b


if __name__ == '__main__':
    pass
    items_ = [dict(a=2, b=2), dict(a=4, b=2), dict(a=6, b=2)]
    items1 = [1, 2, 3]
    for i in Coroutine(gevent).run_all(count_num, items_, batch_size=10):
        print(i)
