from time import perf_counter

def function_timing(func, *args):
    """ returns the function absolute execution time """
    ticker = Ticker()
    ticker.tick()
    result = func(*args)
    ticker.tick()
    timing = ticker.get()
    return (result, timing)

class Ticker():
    """ Ticker to count the time elapsed between two ticks """

    def __init__(self):
        self.start = .0
        self.end = .0

    def tick(self):
        if self.start != .0:
            self.end = round(perf_counter(), 3)
        else:
            self.start = round(perf_counter(), 3)
    
    def get(self):
        return (self.start, self.end)

    def reset(self):
        self.start = .0
        self.end = .0

def copy_docstring(fromfunc):
    """Decorator to copy the docstring of ``fromfunc``.

    It appends an existing docstring to it.
    """
    def _decorator(func):
        sourcedoc = fromfunc.__doc__
        if func.__doc__:
            func.__doc__ = sourcedoc + func.__doc__
        else:
            func.__doc__ = sourcedoc
        return func
    return _decorator
