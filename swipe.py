# Swap Function
def test_swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


a = 15
b = 25
a, b = test_swap(a, b)
print("a=", a, "Test")
print("b=", b)
