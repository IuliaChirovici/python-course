# 1. Reverse the order of the items in an array.
# Example:
# a = [1, 2, 3, 4, 5]
# Result:
# a = [5, 4, 3, 2, 1]

array = [1, 2, 3, 4, 5]
print('Array-ul este: ', array)
x = len(array)
print('Lungimea array-ului este: ', x)
print('Array-ul inversat este: ', array[::-1])

#SAU

if x%2 == 0:
    odd = False #par
    print(odd)
else:
    odd = True #impar
j = x-1
for i in range(0, x-1):
    if (odd and i == j) or (not odd and i>j):
        break
    aux = array[i]
    array[i] = array[j]
    array[j] = aux
    j -= 1
print(array)

# 2. Get the number of occurrences of var b in array a.
# Example:
# a = [1, 1, 2, 2, 2, 2, 3, 3, 3]
# b = 2
# Result:
# 4

arr = [1, 1, 2, 2, 2, 2, 3, 3, 3]
b = 2
x = arr.count(b)
print('Numarul de aparitii al lui b este: ', x)

# 3. Given a sentence as string, count the number of words in it.
# Example:
# a = 'ana are mere si nu are pere'
# Result:
# 7

a = 'ana are mere si nu are pere'
b = a.split(' ')
x = len(b)
print('Nr. de cuvinte este ', x)

