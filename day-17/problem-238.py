

def productExceptSelf(nums: list[int]) -> list[int]:
    length = len(nums)
    ans = [1] * length
    prefix, suffix = 1, 1
    for i in range(length):
        ans[i] = prefix
        prefix *= nums[i]

    for i in range(length - 1, -1, -1):
        ans[i] *= suffix
        suffix *= nums[i]

    return ans


print(productExceptSelf([-3, 1, 0, -1, 3]))
