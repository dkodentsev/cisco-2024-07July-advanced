#!/usr/bin/env python3



from concurrent.futures import ProcessPoolExecutor, wait

def square(n):
    return n ** 2

if __name__ == '__main__':

    with ProcessPoolExecutor(max_workers=5) as executor:
        all_results = []

        for i in range(10):
            result = executor.submit(square, i)  # 1st arg is function, rest are args to it
            all_results.append(result)

        # wait returns two sets, typically called done and not_done
        # by default, wait will return its results only when all threads are done
        done, not_done = wait(all_results)

        # done, not_done = wait(all_results, return_when=FIRST_COMPLETED)

        for one_item in done:
            print(one_item.result())
