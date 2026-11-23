import json

with open("./config/roles.json", encoding="utf-8") as f:
    ROLES = json.load(f)

with open("./config/users.json", encoding="utf-8") as f:
    USERS = json.load(f)

def check_permission(user_name, resource, act):
    # 사용자 파일에 없나?
    if user_name not in USERS:
        return False, "등록되지 않은 사용자"

    # 재직 중이 아닌가?
    if USERS[user_name]['employed'] == False:
        return False, "퇴사한 계정"

    # 역할이 역할 파일에 없나?
    role = USERS[user_name]['role']
    if role not in ROLES:
        return False, "역할이 없음"

    # 자원:행위 가 권한에 없나?
    permission = f'{resource}:{act}'
    if permission not in ROLES[role]:
        return False, "권한 없음"

    return True, "허용"