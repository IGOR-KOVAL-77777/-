def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function()
# inner_function() #В результате вызова функции inner_function вне функции test_function программа
# выдаёт ошибку!!!!!!!!!!!!!!!
