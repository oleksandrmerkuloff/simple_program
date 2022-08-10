import random

test_nums = [random.randint(1, 21) for test_nums in range(10)]
lenght_test_nums = len(test_nums)
print(test_nums)
for i in range(lenght_test_nums):
    for j in range(lenght_test_nums - i - 1):
        if test_nums[j] > test_nums[j + 1]:
            test_nums[j], test_nums[j + 1] = test_nums[j + 1], test_nums[j]
    for j in range(lenght_test_nums - i - 1, -1):
        if test_nums[j] < test_nums[j - 1]:
            test_nums[j], test_nums[j - 1] = test_nums[j - 1], test_nums[j]

print(test_nums)
