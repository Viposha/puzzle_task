from datetime import datetime


def time_measure(func):
    """Decorator for measure time of func execution"""
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        finish = datetime.now()
        func_time = finish - start
        print(f"Time for execution:  {round(func_time.total_seconds(), 2)} seconds.")
        return result
    return wrapper
