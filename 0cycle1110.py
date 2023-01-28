
#! 백준 더하기 사이클 1110
# N=input()
# if int(N)<100 :
#     print(N[len(N)-1])
# N=[3,54]
# print(type(N[0]))

# N=input()
# nnew = 0
# sum = 0
# cnt = 0
# while True:
#     if int(N) < 10 :
#         new_N = '0' + N
#         nnew=new_N[-1] + N
#         print(nnew)
    #     cnt += 1

    # if nnew == N:
    #     print(cnt)
    #     break
    
#     else:
#         for i in N:
#             sum += int(i)
#         sum=str(sum)
#         nnew=N[-1] + sum
#         print(nnew)
#         cnt += 1


#? 입력받은 수의 각각 자릿수합 구하기
# s=input()
# sum=0
# for i in s:
#     sum+=int(i)
# print(sum)

# n=int(input())
# while True:
#     for i in range(n):
#         print(i)
#     if i == 10:
#         break



N=input()
nnew = 0
sum = 0
cnt = 0
while nnew != N:
    if int(N) < 10 :
        new_N = '0' + N
        nnew=new_N[-1] + N
        cnt += 1
    else:
        for i in N:
            sum += int(i) 
        sum=str(sum)   
        nnew=N[-1] + sum       
        cnt += 1
    
    print(cnt)