# Computer-013 networksim 처음 써 보기

## networksim · 다른 VLAN 연결하기
- 연결 전 시험 결과: Test traffic 이 실패했다. "There is no path between the networks – a link is missing."
- 추가한 장치: L3 switch
- 연결한 장치: SW VLAN10, SW VLAN20 (L3 스위치를 양쪽 L2 스위치에 각각 연결)
- 연결 후 시험 결과: Test traffic 이 PASSES. 위쪽 Check 를 누르니 Solved! 와 PC → server (SMB 445) passes 가 나왔다.
- 서로 다른 네트워크 사이에 필요했던 기능: L3 라우팅 (L3 스위치)

## 막힌 것
없음

## 다음에 확인할 것
없음
