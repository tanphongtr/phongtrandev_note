# def warp(func):
#     print('this is wrap')
#     def wrap_f():
#         func()
#     return wrap_f

# @warp
# def test():
#     print('this is test')

# test()


# demo decorator
# def decorator(func):
#     print('this is decorator')
#     def wrap_f():
#         print('this is wrap')
#         func()
#     return wrap_f

# @decorator
# def test():
#     print('this is test')

# test()


# demo decorator parameter
def decorator(*args, **kwargs):
    def wrap(func):
        print('this is decorator')
        def wrap_f(a):
            print('this is wrap')
            func(a, a)
        return wrap_f
    return wrap

# @decorator('a', 'b', 'c')
def test(a, b):
    print('this is test')

# decorator()(test)(1)



