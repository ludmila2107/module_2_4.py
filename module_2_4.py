numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers: # проходимся по каждому элементу списка numbers
    if i == 1: # если элемент списка равен 1, то это непростое число, добавляем его в список not_primes
        not_primes.append(i)
    for j in range(2, i-1): # создаем вложенный цикл, диапазон j = от 2 до i-1
        if i % j == 0: # если элемент в numbers делится без остатка на j, то число непростое
            not_primes.append(i) #добавляем его в список not_primes
            break #прерываем цикл после первого соответствия условию
for el in numbers: # создаем еще один цикл, проходим по numbers
    if el not in not_primes: # если элемент в numbers отсутствует в not_primes, добавляем в primes
        primes.append(el)


print('Простые числа: ', primes)
print('Непростые числа: ', not_primes)
