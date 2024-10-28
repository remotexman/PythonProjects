def text_function():
    def inner_function():
        print('Я в области видимости функции text_function')
    inner_function()
# inner_function()