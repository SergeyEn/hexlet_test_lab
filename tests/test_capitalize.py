from capitalize import capitalize


#if capitalize('hello') != 'Hello':
 #   raise Exception('Функция работает неверно!')
assert capitalize('hello') == 'Hello'

#if capitalize('') != '':
 #   raise Exception('Функция работает неверно!')
assert capitalize('') == ''

print('Все тесты пройдены!')
