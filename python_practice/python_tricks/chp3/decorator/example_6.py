from dis import dis

b = 6
def f(a):
    global b
    print(a)
    print(b)
    b = 9

f(1)
print(b)

dis(f)