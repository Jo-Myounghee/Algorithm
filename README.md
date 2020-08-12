[TOC]

# 🐢Algorithms🐇

>  파일명: 문제출처_문제번호.py
>
> git commit -m: 문제출처_문제번호



# 👓 SWEA 

>  [SWEA][https://swexpertacademy.com/main/main.do]

## ✏ ing 

> 파일명: 문제레벨_문제번호.py

## 👓 D2

### 1948.날짜 계산기

#### 풀이(1)

```python
T = int(input())
 
for tc in range(1, T+1):
    day_lst = list(map(int, input().split()))
    m1 = day_lst[0]
    d1 = day_lst[1]
    m2 = day_lst[2]
    d2 = day_lst[3]
 
    day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_day = 0
    if m1 == m2:
        result = d2 - d1 + 1
    else:
        for i in range(m1 - 1, m2 - 1):
            total_day += day_list[i]
 
        result = total_day - d1 + d2 + 1
 
    print(f'#{tc} {result}')
```

#### 문제를 풀면서 고민했던 부분

- 날짜에 접근해야하는데, 날짜에 어떻게 하면 접근할 수 있을까?

  → 처음에는 날짜를 받아오는 모듈을 쓸까 고민했는데, 찾아보니 해당 모듈은 실시간으로 시간을 받아오는 것이어서 의미가 없었다.

  그리고 문제의 제약사항에서 각 달의 마지막 날짜가 정해져있었다.

  → 여기서 힌트를 얻어, 리스트를 만들어야겠다고 생각함.

  1. 처음에는 if-else를 사용해서, input데이터의 month가 같을 때와 다를 때 나눠서 풀이를 진행했다. 근데 마크다운으로 정리하다가 코드를 줄이는 방법을 생각해냈다.

  2. 어차피 else에서 for문의 range가 `(m1 - 1, m2 -1)` 이니까 만약 `m1 == m2` 이면 결국 `total_day` 는 0이 되서 `result`가 if문과 같게 된다. 그래서 수정한 코드는 아래와 같다.

     #### 풀이(2)

     ```python
     T = int(input())
      
     for tc in range(1, T+1):
         day_lst = list(map(int, input().split()))
         m1 = day_lst[0]
         d1 = day_lst[1]
         m2 = day_lst[2]
         d2 = day_lst[3]
      
         day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
         total_day = 0
        
         for i in range(m1 - 1, m2 - 1):
             total_day += day_list[i]
      
         result = total_day - d1 + d2 + 1
      
         print(f'#{tc} {result}')
     ```

     #### 궁금한 점

     근데 이렇게 하니까, 코드 길이가 60자나 줄었는데 실행시간은 20ms늘어났다 !

     사실 이게 무슨 차이인지는 아직은 모르겠지만 ! 이 부분은 나중에 찾아보ㅏ야지 😵

## 🔹 D3

## 🔹 D4

## 🔹 D5

## 🔹 D6