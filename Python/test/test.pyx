def sum_of_n_numbers(n):
    cdef int i, sum
    sum = 0
    for i in range(n):
        sum += i
    return sum
