from rbac import check_permission

REQUESTS = [                                                     # 판정할 요청 리스트. (사용자, 자원, 행위)
    ("seoyeon", "SALES", "QUERY"),                               # 영업이 영업 실적 조회
    ("seoyeon", "SETTLE", "QUERY"),                              # 영업이 정산 조회 (seoyeon 사건)
    ("junho", "SETTLE", "QUERY"),                                # 재무가 정산 조회
    ("junho", "SALES", "CHANGE"),                                # 재무가 영업 실적 변경
    ("dami", "SALES", "QUERY"),                                  # 퇴사자가 영업 실적 조회
    ("minsu", "SALES", "QUERY"),                                 # 사용자 파일에 없는 계정
    ("gaeun", "ACCOUNT", "CHANGE"),                              # 계정 관리자가 권한 변경
    ("batch-night", "SETTLE", "QUERY"),                          # 서비스 계정이 정산 집계
    ("tester", "SALES", "QUERY"),                                # 역할 파일에 없는 역할(intern)
]

for user, resource, action in REQUESTS:
    is_allowed, reason = check_permission(user, resource, action)
    print(user, resource, action, "->", is_allowed, reason)