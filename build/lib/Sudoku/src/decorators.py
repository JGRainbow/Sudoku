from time import perf_counter

def timer(func):
    def inner(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        end = perf_counter()
        print(f'\nTime taken: {end - start:.3f} seconds')
        return func
    return inner

@timer
def count_to_n(n):
    return [i for i in range(n)]