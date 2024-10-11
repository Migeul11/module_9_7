def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        is_simple = True
        for i in range(2, (res // 2) + 1):
            if res % i == 0:
                is_simple = False
                print("Составное")
                break
        if is_simple:
            print("Простое")
        return res
    return wrapper


@is_prime
def sum_three(first, second, third):
    return first + second + third


result = sum_three(2, 3, 6)
print(result)
