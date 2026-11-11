from collections import Counter

def report_suspects(failed_users, threshold=2):
     counts = Counter(failed_users)
     for user, count in counts.items():
          if count >= threshold:
               print(f'확인 필요: {user} · {count}회')

users = ["kim01", "kim01", "kim01", "park03"]
report_suspects(users)