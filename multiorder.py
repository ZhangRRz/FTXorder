
import time
import multiprocessing
from rest.client import FtxClient


api_key = 'QhWqAoqGhoYEyk-SuM3KEEHaBIASQD5ZoPRN_rxR'
api_secret = 'K_yvxOFRsoLJ9UEGSyQl-xpV5hQEKMWQUu-hMT2j'
client = FtxClient(api_key=api_key, api_secret=api_secret)

c = time.time()


def multiprocessing_func(x):
    while(1):
        market = 'POLIS/USD'
        side = 'buy'
        price = 1.8
        size = 30
        type0 = 'limit'
        ioc_flag = True  # 不成交則立即撤單

        order_data = client.place_order(market=market, side=side,
                                        price=price, size=size, type=type0, ioc=ioc_flag)

        print(order_data)


if __name__ == '__main__':
    processes = []
    for i in range(0, 6):
        p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
        processes.append(p)
        p.start()
