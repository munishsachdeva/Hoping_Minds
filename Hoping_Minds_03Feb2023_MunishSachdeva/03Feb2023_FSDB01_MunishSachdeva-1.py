def f():
    def g():
        print('function g()')
        print('function g() ends')
        return
    g() #calling inner function g()
    return
f() #calling outer function f()
