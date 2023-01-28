# C = int(input())
# for i in range(C):
#     N = int(input())
#     for m in range(N):
#         scores = list(map(int,input().split()))
#         print(scores)


C = int(input())
sum = 0
over=0
for i in range(C):
    scores = list(map(int,input().split()))
    sscore = scores[1:]
    aver =sum/scores[0]
    for k in sscore:
        sum += k
        if k > aver:
            over += 1
    print(over)
    # rate = over/scores[0]*100
    # print(f'{rate:.3f}%')