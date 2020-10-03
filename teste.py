a = 0
def func():
    b = 0
    a = 100
    print(a)
    def func2():
        nonlocal b
        b = 5
        print(b, "dentro")
    func2()
    a += 1
    print(b , 'fora')
    print(a , 'func1')
func()
print(globals())