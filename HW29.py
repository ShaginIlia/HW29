# Динамическое определение функций (def)
def operat(operation):
    if operation == 'multip':
        def multip(x, y):
            return x * y

        return multip
    elif operation == 'div':
        def div(x, y):
            return x / y

        return div


my_func = operat('multip')
my_func2 = operat('div')
print(my_func(3, 3))
print(my_func2(3, 3))

# Лямбда-функции (lambda)

la_power = lambda x, y: x ** y
print(la_power(4, 3))


def power(x, y):
    return x ** y


print(power(4, 3))


# Вызываемые объекты (__call__)

class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, a, b):
        return a * b


rect = Rect(5, 7)
print('Площадь равна', rect(5, 7))
