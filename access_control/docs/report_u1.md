# Unit 1 보고서 · 역할로 권한 정하기 (한희근)

## 실습 1-1

- (가) 답
  -- 요청 1: seoyeon, sales, SALES:QUERY → 인가
  -- 요청 2: seoyeon, sales, SETTLE:QUERY → 비인가 (표에 없음)
  -- 요청 3: junho, finance, SETTLE:QUERY → 인가
  -- 요청 4: junho, finance, SALES:CHANGE → 비인가 (표에 없음)
  -- 요청 5: gaeun, account_admin, SETTLE:QUERY → 인가
  -- 요청 6: batch-night, batch, SETTLE:QUERY → 비인가 (표에 없음)
- (나) 답: finance의 역할은 '정산 내역을 조회합니다.'로 정의되어있으니 정산 내역(SETTLE)에 대한 조회 권한(:QUERY)에 추가로, 영업 실적(SALES)에 대한 조회 권한(:QUERY)까지 존재한다. 정산을 자동으로 집계하는 batch역할은 SETTLE:QUERY권한만으로도 동작한다.
- (다) 답: 표에 없는 역할에 대해서는 거부되어야 한다. '누구에게 무엇을 허가한다'가 명시된 표이다. 표에 존재하는 '누구'에게만 '무엇'이 허가되어야 한다. 그렇지 않는다면, 역할을 굳이 표에 있는 것으로 명시하며 인가 요청을 할 필요가 없다. 공격자 입장에서도 너무나도 쉽게 권한을 탈취할 수 있다. 표를 관리하는 주체는 else 경우에 대해 따로 명시를 하거나, 표에 없는 역할이 요청하는 경우 어떻게 처리되는지에 대해 인지하고 있어야 한다.

## 실습 1-2

- (가) 답

-- 실행결과

```
seoyeon SALES QUERY -> True 허용
seoyeon SETTLE QUERY -> False 권한 없음
junho SETTLE QUERY -> True 허용
junho SALES CHANGE -> False 권한 없음
dami SALES QUERY -> False 퇴사한 계정
minsu SALES QUERY -> False 등록되지 않은 사용자
gaeun ACCOUNT CHANGE -> True 허용
batch-night SETTLE QUERY -> True 허용
tester SALES QUERY -> False 역할이 없음

```

-- 각각 거부된 지점: 1 없음 / 2 [4] / 3 없음 / 4 [4] / 5 [2] / 6 [1] / 7 없음 / 8 없음 / 9 [3]

- (나) 검사가 하나 뿐이니, 그 이외의 검사들에 대해선 전부 통과해버립니다. 답: 2, 4, 5, 9가 허용되면 안 됩니다. 2, 4: 자료에 행위를 할 권한이 없음 / 5: 퇴사함 / 9: 존재하지 않는 역할
- (다) 답: dami는 2에도 걸리고 3에도 걸리니 순서를 바꾸면 3번 미달로 판정됩니다. 하지만 '해당 인물이 퇴사했는가?'를 판단하는 것이 '해당 인물에게 적합한 역할이 부여되어있는가?'를 판단하는 것보다 중요하므로, 판단의 순서를 바꿔서는 안 된다. (퇴사한 직원은 어차피 권한을 부여해주지 않을 것이므로 역할이 중요하지 않다)

## 실습 1-3

- (가) 답:

```

09:10 seoyeon SETTLE QUERY -> True 예외 1번
10:00 dami SALES QUERY -> False 퇴사한 계정
11:40 gaeun SETTLE QUERY -> True 예외 5번
12:30 gaeun SETTLE QUERY -> False 권한 없음
[만료 뒤 시도] 12:30 gaeun SETTLE QUERY - 만료된 예외 5 2026-10-22 12:00
13:00 junho SETTLE QUERY -> True 역할 권한
14:00 batch-night SALES QUERY -> True 예외 4번
15:00 junho SALES CHANGE -> False 권한 없음
[만료 뒤 시도] 15:00 junho SALES CHANGE - 만료된 예외 2 2026-10-20 18:00
16:20 seoyeon SETTLE QUERY -> True 예외 1번
18:05 seoyeon SETTLE QUERY -> False 권한 없음
[만료 뒤 시도] 18:05 seoyeon SETTLE QUERY - 만료된 예외 1 2026-10-22 18:00

```

-- 만료 뒤 시도로 출력된 세 건: gaeun 5번, junho 2번, seoyeon 1번

- (나) 답: dami는 sales이고 SALES:QUERY 권한을 갖고 있으니, 영업 실적 조회가 돌아가게 된다. 퇴사자를 구분하지 않고 일괄 처리해버린다면, 회사 내에 존재하는 비밀이 유출되는 보안 사고가 발생할 우려가 있다.
- (다) 답:

```

+-------------------------+
| exercise1-2_run.py      |
+-------------------------+
         |
         |
         +--> check_permission
         |
         v
+-------------------------+
| rbac.py                 |
+-------------------------+
         |
         | 읽음
         v
   +-------------------+
   | config/roles.json |
   | config/users.json |
   +-------------------+


+-------------------------+
| exercise1-3_run.py      |
+-------------------------+
         |
         |
         +--> evaluate_access
         |
         v
+-------------------------+
| policy.py               |
+-------------------------+
         |
         +--> check_permission
         |
         +--> find_exception
         |
         v
+-------------------------+
| exception_policy.py     |
+-------------------------+
         |
         | 읽음
         v
   +------------------------+
   | config/exceptions.json |
   +------------------------+

```

-- config/exceptions.json 이 깨지면?: 맨 밑의 화살표가 막히지만, 연쇄적으로 올라가 excercise1-3_run.py도 실행 불가능해진다.

## 마무리

- (가) 답: 문제가 뭐죠 이게? 모르는 게 있으면 적어라? 없어서 비워두겠습니다.

> 아래 도전 칸은 선택입니다. 내가 한 도전만 채웁니다.

## 도전 1-1

- (가) 답:
- (나) 답:
- (다) 답:

## 도전 1-2

- (가) 답:
- (나) 답:
- (다) 답:

## 도전 1-3

- (가) 답:
- (나) 답:
- (다) 답:

## 도전 1-4

- (가) 답:
- (나) 답:
- (다) 답:

## 도전 1-5

- (가) 답:
- (나) 답:
- (다) 답:

```

```
