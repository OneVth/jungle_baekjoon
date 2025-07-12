# BOJ 9020 - 골드바흐의 추측

## 문제 요약

4 이상 10,000 이하의 짝수 n이 주어졌을 때, 두 소수의 합으로 이루어진 골드바흐 파티션을 구하는 문제입니다. 가능한 파티션이 여러 개일 경우, 두 소수의 차이가 가장 작은 조합을 출력합니다.

[문제 링크](https://www.acmicpc.net/problem/9020)

![Pasted image 20250712165921](https://ik.imagekit.io/v860zjtxv/Pasted_image_20250712165921_SJgNZ1tBU.png)

처음에는 `is_prime()` 함수를 사용해 문제를 풀었고, 정답도 맞았다.  

그런데 에라토스테네스의 체 방식으로 소수 테이블을 미리 구해두면 더 빠르지 않을까 싶어서 실험해보았다.  

하지만 실제 제출 결과에서는 직접 판별 방식이 더 빠른 실행 시간을 기록했다.

- 실행 시간이 긴 것이 에라토스테네스의 체를 이용한 방식이고,
- 실행 시간이 짧은 쪽이 `is_prime()` 함수로 매 입력에 대해 소수를 판별하는 방식이다.

## 제출 코드

### 1. 입력값마다 is_prime() 함수로 소수를 판별하는 방식

```python
import sys


def is_prime(a: int) -> bool:
    if a < 2:
        return False

    for i in range(2, a):
        if i * i > a:
            break

        if a % i == 0:
            return False

    return True


n = int(sys.stdin.readline().strip())

for _ in range(n):
    even = int(sys.stdin.readline().strip())
    half = even // 2
    for i in range(half, 1, -1):
        if is_prime(i) and is_prime(even - i):
            print(i, even - i, end=" ")
            break
    print()

```

### 2. 에라토스테네스의 체로 미리 소수를 구해놓는 방식

```python
import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    MAX = 10000
    is_prime_arr = [True] * (MAX + 1)
    is_prime_arr[0] = is_prime_arr[1] = False

    for i in range(2, MAX + 1):
        if is_prime_arr[i]:
            for j in range(i * i, MAX + 1, i):
                is_prime_arr[j] = False

    even = int(sys.stdin.readline().strip())
    half = even // 2
    for i in range(half, 1, -1):
        if is_prime_arr[i] and is_prime_arr[even - i]:
            print(i, even - i, end=" ")
            break
    print()

```

## 실험 결과

| 구현 방식 | 코드 길이 | 실행 시간 (PyPy3) |
|---|---|---|
| `is_prime()` 방식 | 487 B | 160 ms |
| 에라토스테네스의 체 방식 | 543 B | 704 ms|

- 해당 문제(BOJ 9020)에서는 `is_prime()` 방식이 체보다 실행 시간 더 우수
- 이유: 체는 필요 없는 소수까지 계산하지만, 문제는 "한 쌍만" 찾으면 끝나므로 오히려 불필요한 연산이 많아짐

### 예상과 달랐던 이유 분석

- 짝수 `n`에 대해 골드바흐 파티션(두 소수의 합)을 한 쌍만 찾으면 됨
- 입력 수는 많지 않고, 각 입력에 대해 소수 판별 횟수도 적음
- 에라토스테네스의 체는 미리 소수 테이블을 작성해서 소수를 판별할 때는 O(1)의 복잡도를 가지지만 초기 테이블 작성 비용이 크다.
- 즉, 입력이 많거나 반복 판별이 많을 때 유리한 것이다.

## 결론

한 쌍만 찾는 문제에서는 `is_prime()`이 더 효율적이다.