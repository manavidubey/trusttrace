import pandas as pd
import matplotlib.pyplot as plt
from collections import deque
from flask import Flask, request, render_template


transaction_df = pd.read_csv('transaction_history.csv')
outliers_df = pd.read_csv('outliers.csv')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        if request.form['submit'] == 'Search':
            related_users = search_related_users(user_id)
            return render_template('index.html', related_users=related_users)
        elif request.form['submit'] == 'Display Graphs':
            display_graphs(user_id)
            return 'Graphs displayed successfully!'
        elif request.form['submit'] == 'Backtrack':
            backtrack_path = backtrack_transactions()
            return render_template('index.html', backtrack_path=backtrack_path)
    return render_template('index.html')

def search_related_users(user_id):
    indices_from = outliers_df.index[outliers_df['User'] == user_id]
    related_users = []
    for i in indices_from:
        related_users.append(outliers_df['To'].iloc[i])

    indices_to = outliers_df.index[outliers_df['To'] == user_id]
    for i in indices_to:
        related_users.append(outliers_df['User'].iloc[i])

    return related_users

def display_graphs(user_id):
    user_transactions = transaction_df[transaction_df['from'] == user_id]
    plt.plot(user_transactions['timeStamp'], user_transactions['value'])
    plt.xlabel('Time')
    plt.ylabel('Transaction Value')
    plt.title('Time Series Graph for User: ' + user_id)
    plt.show()

def backtrack_transactions():
  
    graph = {}
    for _, row in outliers_df.iterrows():
        user = row['User']
        to = row['To']
        if user in graph:
            graph[user].append(to)
        else:
            graph[user] = [to]

   
    start_user = outliers_df.iloc[0]['User']
    end_user = outliers_df.iloc[-1]['To']

    queue = deque([(start_user, [start_user])])
    found_path = False

    while queue:
        user, path = queue.popleft()

        if user == end_user:
            return 'Path found: ' + ' -> '.join(path)
            found_path = True
            break

        if user in graph:
            for neighbor in graph[user]:
                queue.append((neighbor, path + [neighbor]))

    if not found_path:
        return 'Path not found'

if __name__ == '__main__':
    app.run(debug=True)
