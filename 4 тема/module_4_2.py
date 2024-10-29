def text_function():
    def inner_function():
        print('Я в области видимости функции text_function')
    print(locals())
    inner_function()
try:
    inner_function()
except NameError as error:
    print(error)            # name 'inner_function' is not defined


text_function()