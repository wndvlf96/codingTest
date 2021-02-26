from sys import stdin
import heapq

in1 = int(stdin.readline().strip())
ans = []
for i in range(in1):
    hq1 = []                                        # 정상적 hq로 pop하면 항상 최소값 튀어나옴
    hq2 = []                                        # 모든 값에 * -1을 해서 넣어서 pop시 * -1을 해서 최대값을 튀어나오게 할 것임.
    in2 = int(stdin.readline().strip())
    vit = [0]* 1000001
    for j in range(in2):
        in3 = stdin.readline().strip().split()
        if in3[0] == 'I':                           # vit함수를 1로 바꿔준다. 큐에서 이 명령의 index를 기억하며 나중에 이걸로 지워진지를 확인한다.
            heapq.heappush(hq1, (int(in3[1]),j))
            heapq.heappush(hq2, (int(in3[1]) * -1, j))
            vit[j] = 1
        elif in3[0] == 'D':                         # vit가 1일 때까지 pop
            if in3[1] == '1':                   # 현재 q에서 최댓값을 팝하여라
                while hq2 and vit[hq2[0][1]] == 0:
                    heapq.heappop(hq2)
                if hq2 != []:
                    maxnow, index = heapq.heappop(hq2)
                    vit[index] = 0
                    #hq1.remove(maxnow)              # 이걸 바꿔야 된다.
            else:                               # 현재 q에서 최소값을 팝하여라
                while hq1 and vit[hq1[0][1]] == 0:
                    heapq.heappop(hq1)
                if hq1 != []:
                    minnow, index = heapq.heappop(hq1)
                    vit[index] = 0
                    #hq2.remove(minnow*-1)           # 이걸 바꿔야 된다.
    # 마지막으로 반복문으로 hq1,hq2 둘다 돌아서 vit[index]==1 일때까지
    while hq1 and vit[hq1[0][1]] == 0:
        heapq.heappop(hq1)
    while hq2 and vit[hq2[0][1]] == 0:
        heapq.heappop(hq2)
    if hq1 == [] or hq2 == []:
        ans.append('EMPTY')
    else:
        ansstr = str(heapq.heappop(hq2)[0] * -1) +' '+ str(heapq.heappop(hq1)[0])
        ans.append(ansstr)
for i in ans:
    print(i)