import pandas as pd
from collections import deque


df = pd.read_csv('outliers.csv')


graph = {}
for _, row in df.iterrows():
    user = row['User']
    to = row['To']
    if user in graph:
        graph[user].append(to)
    else:
        graph[user] = [to]


start_user = df.iloc[0]['User']
end_user = df.iloc[-1]['To']

queue = deque([(start_user, [start_user])])
found_path = False

while queue:
    user, path = queue.popleft()

    if user == end_user:
        print("Path found:", ' -> '.join(path))
        found_path = True
        break

    if user in graph:
        for neighbor in graph[user]:
            queue.append((neighbor, path + [neighbor]))

if not found_path:
    print("Path not found")
