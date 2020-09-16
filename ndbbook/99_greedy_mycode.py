N, K = map(int, input().split())
cnt = 0
while 1:
    if N % K == 0:
        N //= K
    else:
        N -= 1
    cnt += 1
    if N == 1: break
print(cnt)

'''
1. N이 K로 나누어 떨어진다면 N을 K로 나눈 값을 다시 N에 입력한다.
2. N이 K로 나누어 떨어지지 않는 경우에는 -1을 한다
3. N이 1이 될 때까지 위의 계산을 반복한다.
'''
'''
답안을 보고 느낀점
답안 접근법
1. N이 K로 나누어 떨어지는 수가 될 때까지 1씩 빼기(while)
1-1. N이 K로 나누어 떨어지는 수를 target으로 하고, 해당 숫자까지 몇번 빼야하는지 숫자를 구해서 n에 더해줌
1-2. n이 k보다 작을 때, 반복문 탈출하고 마지막으로 남은 수에 대해서 빼준 만큼 count를 해준다.
'''