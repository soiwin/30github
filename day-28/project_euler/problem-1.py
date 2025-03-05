

def multiples_of_3_or_5(n: int) -> int:
    ans = 0

    for i in range(n):
        ans += i if i % 3 == 0 or i % 5 == 0 else 0

    return ans


print(multiples_of_3_or_5(1000))
