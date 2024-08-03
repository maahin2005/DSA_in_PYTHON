# Sorting Algorithm

- what is sorting?
  --> Arrange element in ascending or descending order.

ex.
arr = [10,8,99,100,33,2,10]

i = 0
j = 1

- condition of ascending order:
  => left side should be less then right side
  => our i should be less then??? and i is nothing but min_idn

ascending order=[2,4,8,10,33,99,100]

decending order=[100,99,33,10,8,4,2]

## Selection Sort

- first loop always start from 0 is end with N
- second loop start with (i + 1) and end with N
- and then in the inner loop you have to just arr[min_ind] and arr[j+1]; min_idx nothing but just i
- then swap according to condition

for i in range(N):
min_ind = i
for j in range(i+1, N):
if arr[min_idn] > arr[j]:
min_idn = j

    if min_idn != i:
        arr[i], arr[min_idn] =  arr[min_idn], arr[i]

i = 0 = arr[0] = 10
min_idn = i = 0 = arr[0] = 10
j = 1 = arr[1] = 8

if 10 > 8:
min_idn = j
0 = 1

## Bubble Sort

- start first loop with 0 and end with N
- second loop start with 0 and end with (N - 1 - i)
- compare adjacent element like arr[j] > arr[j+1]

arr = [10,8,99,100,33,2]

- right order for ascending order:
  => left should be less then right
  => 8 should be first and 10 should be right

i = 0 = arr[i] = 10
j = 0 = arr[j] = 10
j + 1 = 1 = arr[j + 1] = 8
10 > 8

for i in range(N):
isSwap = false
for j in range(N-1-i):
if arr[j] > arr[j+1]:
arr[j], arr[j+1] = arr[j+1], arr[j]
isSwap = true
if not isSwap:
break

arr = [10,8,99,100,33,2]

## DRY run of Bubble

- i = 0;
- isSwap = false

- j = 0; j+1 = 1
- arr[j] = 10 ; arr[j+1] = 8
- what is the end of j??? => N - 1 - i => 6 - 1 - 0 => 5
- what we want? 8 should be left and 10 should be right
- we are swaping and isSwap = true
- we have swapper now arr is changed
- arr = [8,10,99,100,33,2]

j = 1
arr[j] = 10 and arr[j+1] = 99
10 > 99 => not swap -> isSwap is false

- arr = [8,10,99,100,33,2]
  j = 2 and j + 1 = 3
  99 > 100 => not swap -> isSwap is false

- arr = [8,10,99,100,33,2]
  j =3 and j +1 = 4
- arr = [8,10,99,33,100,2]
  j = 4 and j + 1 = 5

arr = [8,10,99,33,2,100]
i = 1; j=1; j+1=2
end of j = N - 1 - i => 6 -1 - 1: 4
arr[j] = 10 ; arr[j+1] = 99
j=2 and j+1 = 3
arr[j] = 99 and arr[j+1] = 33
swap = isSwap = true

arr = [8,10,33,99,2,100]
j = 3 and j + 1 => 4
arr[j] = 99 ; arr[j+1] = 2
swap isSwap = true

arr = [8,10,33,2,99,100]

(N-1-i) = (N-1) => j and j+1 =>( N - 1) - i

i = 2 and end of j => (N-1-i)=> 6 - 1- 2=>3
j = 0 and j + 1 = 3
