num = int(input("Enter a number to get all prime numbers up to it: "))
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False
    return True
primes = []
for number in range(2, num + 1):
    if is_prime(number):
        primes.append(number)
print(f"Prime numbers up to {num}: {primes}")
