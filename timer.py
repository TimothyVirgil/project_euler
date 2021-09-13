'''This is a decorator used to time functions, in seconds.'''

def timer(func):
    import time

    def inner_func(*args,**kwargs):
        start = time.time()
        func()
        print('Total time: {} seconds'.format((time.time()-start)))

    return inner_func    
