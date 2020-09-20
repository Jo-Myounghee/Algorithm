[toc]

# 💌 백트래킹

> ~~퇴각검색~~ (한국어로 번역한게 더 어렵네요. 편하게 백트래킹이라고 하겠습니다 !)
>
> 현재 상태에서 가능한 모든 후보군을 따라 들어가며 탐색하고, 해를 찾는 도중에 막히면(해가 아니면) 되돌아가서 다시 해를 찾아가는 기법

- **유망하지 않으면 배제를 하고 부모노드로 되돌아가면서 풀이 시간이 단축된다.**

## 백트래킹 알고리즘

1. 지금 노드가 유망한가(promising function사용, 유망한지 확인하는 함수)

   1-1. 맞다면 2번 진행

   1-2. 아니면 return (가지치기)

2. 그 다음 노드를 재귀호출(recur)하여 1번부터 진행

### sudo

```python
def checknode(v):
    if promising(v):
        if there is a solution at v:
            write the solution
        else:
            for w in each child of v:
                checknode(w)
```

### 결론 

DFS처럼 스택을 사용하되 모든 경로의 수를 확인하는 것이 아닌 각 노드의 유망성을 먼저 판단하고, 유망하다고 생각되면 확인, 그렇지 않다면 pass

-> DFS(깊이 우선 탐색)과 다른 점은 유망성에 따른 가지치기의 유무



## 백트래킹 대표 유형 3가지

> 사실 백트래킹은 재귀를 사용해서 그런지 구현하는 과정이 어렵습니당 ㅠ (제 기준 .. 아무리 이론을 봐도 모르겠더라구여 ? )
>
> 그래서 열심히 찾아본 결과 다행히도 백트래킹을 사용할 수 있는 문제들은 대표 유형에서 크게 벗어나지 않는다고 하니,
>
>  백트래킹을 사용하는 대표 문제 3개의 풀이 코드를 보며 공부를 해봅시당 :)

### 1. BOJ 15649: N과 M

> 문제 링크 : https://www.acmicpc.net/problem/15649

#### 1) 문제 개요

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

#### 2) 문제 접근

range(1, N+1)에서 요소의 개수가 M인 부분집합의 개수를 구하는 문제

#### 3) 문제 풀이(1) : 정석 풀이

```python
N, M = map(int, input().split())
visited = [False] * N  # 탐사 여부 check
out = []  # 출력 내용

def solve(depth, N, M):
    if depth == M:  # 탈출 조건
        print(' '.join(map(str, out)))  # list를 str으로 합쳐 출력
        return
    for i in range(len(visited)):  # 탐사 check 하면서
        if not visited[i]:  # 탐사 안했다면
            visited[i] = True  # 탐사 시작(중복 제거)
            out.append(i+1)  # 탐사 내용
            solve(depth+1, N, M)  # 깊이 우선 탐색
            visited[i] = False  # 깊이 탐사 완료
            out.pop()  # 탐사 내용 제거

solve(0, N, M)
```

#### 4) 문제 풀이(2) : 내장함수 permutations 사용

- permutations를 사용할 경우 자동적으로 순열을 생성해줌 (이 문제의 경우 range(1, N+1)의 범위에서 길이가 M인 순열)

```python
from itertools import permutations
N, M = map(int, input().split())
P = permutations(range(1, N+1), M)
for i in P:
    print(' '.join((map(str, i))))
```



### 2.BOJ 9663: N-Queen

> 문제 링크 : https://www.acmicpc.net/problem/9663

#### 1) 문제 개요

N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

#### 2) 문제 접근

- 한 행 씩 확인
- 해당 행에서 한 칸씩 퀸을 놓을 수 있는지 없는지 확인
  - 놓을 수 없다면 break
  - 놓을 수 있다면 재귀 호출 

#### 3) 문제 풀이

```python
# 퀸 놓아보기 함수
def build_queen(n, N):
    global result
    if n == N:	# 재귀 빠져나가기
        result += 1
        return 
    # 재귀 못 빠져나갈 때 퀸을 놓아보고 이전 퀸들과 비교
    else:
        for i in range(N):
            row[n] = i
            # for문이 break 걸리지 않고 다 돌면 else(재귀) 실행
            for j in range(n):
                # 한 열에 하나씩 들어가므로 열 비교는 필요 없음
                # 대각선은 수학식을 생각해서 쉽게 구할 수 있음
                if row[j] == row[n] or (row[n]-n) == (row[j] - j) or (row[n] + n) == (row[j] + j):
                    break
                else: build_queen(n+1, N)
# 입력
s = int(input())

# 초기값 설정
result = 0
row = [300] * s

# 퀸 놓아보기 함수
build_queen(0, s)

# 출력
print(result)
```



### 3. BOJ 1182 : 부분 수열의 합

> 문제 링크: https://www.acmicpc.net/problem/1182

#### 1) 문제 개요

N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

#### 2) 문제 접근

- 원소를 포함하는 경우, 포함하지 않는 경우를 나누어 원소의 합이 S가 넘지 않을 때까지 재귀 진행
- 만약 원소의 합이 S가 넘는다면
  - 합이 S인 경우 : res += 1
  - 합이 S보다 큰 경우 : return

#### 3) 문제 풀이 

> 재귀 이용

```python
def f(idx, d):
    global res
    if(idx >= n):
        if(s == d):
            res += 1
            return
    else:
        # 원소를 포함하는 경우
        f(idx+1, d+arr[idx])
        # 원소를 포함하지 않는 경우
        f(idx+1, d)

n, s = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
f(0,0)
# s가 0인, 즉 공집합인 경우에는 정답에서 -1을 해줌
if(s):
    print(res)
else:
    print(res - 1)
```



## 출처

https://youtu.be/Enz2csssTCs

https://wlstyql.tistory.com/56

https://txegg.tistory.com/108?category=804548

https://dongsik93.github.io/algorithm/2019/11/13/algorithm-boj-1182/