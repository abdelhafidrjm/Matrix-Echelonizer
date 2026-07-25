def coundDigits(n):
    count = 0
    while n != 0:
        n = (n - n % 10) / 10
        count += 1
    return count

num = int(input())
print(coundDigits(num))