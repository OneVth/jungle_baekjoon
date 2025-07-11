# BOJ 9498 - 시험 성적

## 문제 요약

시험 점수를 입력받아 90 이상은 A, 80 이상은 B, 70 이상은 C, 60 이상은 D, 나머지는 F를 출력하는 문제입니다.  

입력은 0 이상 100 이하의 정수 한 개입니다.

🔗 [문제 링크](https://www.acmicpc.net/problem/9498)

---

## 제출 코드

### 1. if-else 분기 방식

```python
score = int(input())

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
```

### 2. dict 테이블 기반 방식

```python
score = int(input())
grade_table = {10: 'A', 9: 'A', 8: 'B', 7: 'C', 6: 'D'}
print(grade_table.get(score // 10, 'F'))
```

### 3. list 테이블 기반 방식

```python
score = int(sys.stdin.readline().strip())
grade_table = ['F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A']
print(grade_table[score // 10])
```

| 구현 방식 | 코드 길이 | 실행 시간 (PyPy3) |
| ------------- | ----- | ------------- |
| `if-else` 방식  | 185 B | 92 ms |
| `dict` 테이블 방식 | 152 B | 96 ms |
| `list` 테이블 방식 | 157 B | 88 ms |

- `list` 테이블 방식이랑 `dict` 테이블 방식이 `if-else` 방식보다 빠르지 않을까 예상했음.
- 내 예상과 달리 `dict` 테이블 방식이 가장 느리다.
- GPT가 PyPy3 기준으로 분기문은 JIT 최적화가 잘 적용되어 있어서 성능이 더 좋을 수 있다고 한다.