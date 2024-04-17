nums = list(range(6))
print(nums)

numbers = range(1,21,3)
for num in numbers:
    print(num)

nums2 = list(range(0,51, 10))
for i in nums2: 
    print(i)

for num3 in list(range(3,31,3)): 
    print(num3)
    
    
cubed = []
nums4 = list(range(1, 11))
for i in nums4:
    cubed.append(i**3)
print(cubed)
    
cubed = [i**3 for i in range(0,11)]
print(cubed)

byten = [value * 10 for value in range(0, 51, 3)]
print(byten)





