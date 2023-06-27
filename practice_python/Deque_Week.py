from collections import deque as dq

dq = dq(["MON", "TUE", "WED"])

dq.appendleft("SUN")
dq.appendleft("SAT")
dq.append("THR")
print(dq)

dq.pop()
print(dq)

dq.popleft()
print(dq)