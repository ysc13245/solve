nums = []


for c in input():
    if c.isdigit():
        nums.append(c)
    else:
        n2 = nums.pop()
        n1 = nums.pop()
        nums.append(str(eval(n1 + c + n2)))
print(int(float(nums[0])))
