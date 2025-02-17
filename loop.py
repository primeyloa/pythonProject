# for count in [1, 2, 3]:
#     print(count)
#     print("Yes" * count)

def sumNum(nums):
    sum = 0
    for num in nums:
        nextSum = sum + num
        sum = nextSum
        if (sum ==19):
            print("It worked!")
    return sum

def main ():
    sumNum([2,6,3,5,7])
    print(sumNum([2,6,3,5,7]))
