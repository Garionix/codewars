def solution(number):
    sum = 0
    if number < 0:
        return 0
    
    for n in range(0, number):
        if n % 3 == 0 or n % 5 == 0:
            sum += n

    return sum
