import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution time:", end - start)
        return result

    return wrapper


@timer
def slow_function():
    time.sleep(2)
    print("Finished slow task.")


slow_function() 
