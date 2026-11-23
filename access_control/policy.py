from rbac import check_permission                                # 실습 1-2에서 만든 역할 판정 함수를 불러온다
from exception_policy import find_exception                      # 제공 파일의 예외 판정 함수를 불러온다


def evaluate_access(user, resource, action, now):                # 사용자 · 자원 · 행위 · 지금 시각을 받는 함수
    is_allowed, reason = check_permission(user, resource, action)
    if is_allowed:
        return True, "역할 권한"
    else:
        if reason != "권한 없음":
            return False, reason
        else:
            found, found_exception_id = find_exception(user, f'{resource}:{action}', now)
            return found, f'예외 {found_exception_id}번' if found else "권한 없음"