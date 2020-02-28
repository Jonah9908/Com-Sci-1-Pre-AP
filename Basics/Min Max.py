nums = [12, 7, 8, 15, 2, 10, 3]
small = nums[0]
big= nums[0]
spot = 0

while spot < len(nums):
    if small > nums[spot]:
        small = nums[spot]
    if big < nums[spot]:
        big = nums[spot]
    spot = spot + 1


print("The biggest number is " + str(big) + ". " + "the smallest number is " + str(small) + ".")
    

