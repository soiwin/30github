from collections import defaultdict


def maker_prefixsum(nums: list[int]) -> list[int]:
    prefixsum = [0] * (len(nums) + 1)

    for i in range(1, len(nums) + 1):
        print(prefixsum[i - 1] + nums[i - 1])
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]

    return prefixsum


def rsq(prefixsum, l, r):
    return prefixsum[r] - prefixsum[l]


def prefixsum_segment(nums):
    prefix_sum_by_value = defaultdict(int)
    prefix_sum_by_value[0] = 1
    nowsum = 0

    for num in nums:
        nowsum += num
        prefix_sum_by_value[nowsum] += 1

    return dict(prefix_sum_by_value)


