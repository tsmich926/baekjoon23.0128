#4673
lst1=set()
for nums in range(10001):
    for num in str(nums):
        nums += int(num) 
    lst1.add(nums)

lst2=set(range(1,10001))

self_num=sorted(lst2-lst1)
for i in self_num:
    print(i)








# s=input()
# sum=0
# for i in s:
#     sum+=int(i)
# print(sum)
