# for i in range(1,11):
#   print(i)
#  print(f'{i}x{i}={i*i}')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# numbers.remove(1)  ## удаление из списка 1
primes = []
not_primes = []
for i in numbers[1:]:
    is_prime = True
    for j in numbers[1:i]:  ##range(2, i):
        # print(i, j)
        if i / j == int(i / j) and i / j > 1:  # i%j == 0:
            is_prime = False
            break
            # print('конец 2 цикла')
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
        # print(primes)
        # print(not_primes)
        # print('конец 1 цикла')
print(primes)
print(not_primes)
