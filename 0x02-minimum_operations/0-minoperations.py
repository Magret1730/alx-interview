#!/usr/bin/python3
# if n < 1, return count = 0
# count = 1
# gets the first letter 'H'
# if n = 1, return count =  1
# else

# def duplicate_letters(input_list):
#    result = []
#    for letter in input_list:
#        result.append(letter * 2)
#    return result

# def minOperations(n):
#    arr = []
#     count = 0
#    if (n < 1):
#        return 0
#    elif (n == 1):
#        return 1
#    else:
#        if (n % 2 == 0):
#            div = n / 2
#            arr.append('H')
#            for letter in arr:
#                arr.append(letter)
            # arr_copy = arr.copy()
            # arr.split('')
            # arr.append(arr_copy)
#            count += 2
#            print(arr, count)
#            count_arr = count(arr)
#            if (count_arr == div):
#                arr_copy1 = arr.copy()
#                arr.append(arr_copy1)
#                count += 2
#            return count
#        else:
#            div = arr[round(n / 2)]
#            arr.append('H')
#            arr_copy2 = arr.copy()
#            arr.append(arr_copy2)
#            count += 2
#            count_arr2 = count(arr)
#            if (count_arr2 == div):
#                arr_copy3 = arr.copy()
#                arr.append(arr_copy3).pop()
#                count += 2
#            else:
#                arr_copy4 = arr.copy()
#                arr.append(arr_copy4)
#                count += 2


    


# n = 9
# H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
# Number of operations: 6

# else
# if n % 2 != 0
# if the number is odd, we should treat differently
# n = 9
# H -> copy all(count++) -> paste(count++) -> HH -> 



# if the number is even we should treat differently
# n = 4
# div = n/2 = 4/2 = 2
# H -> copy all(count++) -> paste(count++) -> HH -> count_var =  i.e 2
# if count_var == div:
# copy all(count++) -> paste(count++) -> HHHH
# else
# n = 8

def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
