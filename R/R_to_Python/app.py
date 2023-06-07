import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('graphical_overview.html')
    return render_template('index.html')


@app.route('/graphical-overview', methods=['POST'])
def graphical_overview():
    account_number = request.form['txt1']
    
    # Retrieve data from the bank.xlsx file
    bank = pd.read_excel('bank.xlsx')
    
    # Withdrawal Overview
    waa = bank['WITHDRAWAL AMT'][bank['Account No'] == account_number]
    plt.plot(waa)
    plt.xlabel('Time')
    plt.ylabel('Withdrawal Amount')
    plt.title('Withdrawal Overview')
    plt.show()
    
    # Deposit Overview
    daa = bank['DEPOSIT AMT'][bank['Account No'] == account_number]
    plt.plot(daa)
    plt.xlabel('Time')
    plt.ylabel('Deposit Amount')
    plt.title('Deposit Overview')
    plt.show()
    
    # Maximum Transactions
    withdrawl = bank['WITHDRAWAL AMT'][bank['Account No'] == account_number]
    deposit = bank['DEPOSIT AMT'][bank['Account No'] == account_number]
    maximum_withdrawl = max(withdrawl.dropna())
    maximum_deposit = max(deposit.dropna())
    max_transactions = pd.DataFrame({'Maximum Withdrawal': [maximum_withdrawl], 'Maximum Deposit': [maximum_deposit]})
    
    # Maximum Withdrawal Transaction details
    waa_index = withdrawl[withdrawl == maximum_withdrawl].index[0]
    waa_details = bank['TRANSACTION DETAILS'][(bank['Account No'] == account_number) & (bank['WITHDRAWAL AMT'] == maximum_withdrawl)]
    
    # Maximum Deposit Transaction details
    daa_index = deposit[deposit == maximum_deposit].index[0]
    daa_details = bank['TRANSACTION DETAILS'][(bank['Account No'] == account_number) & (bank['DEPOSIT AMT'] == maximum_deposit)]
    
    return render_template('graphical_overview.html', max_transactions=max_transactions, waa_details=waa_details, daa_details=daa_details)

@app.route('/withdrawal-history', methods=['POST'])
def withdrawal_history():
    account_number = request.form['txt2']
    
    # Retrieve data from the bank.xlsx file
    bank = pd.read_excel('bank.xlsx')
    
    # Withdrawal History
    withdrawl = bank['WITHDRAWAL AMT'][bank['Account No'] == account_number]
    transaction_details = bank['TRANSACTION DETAILS'][bank['Account No'] == account_number]
    withdrawal_history = pd.DataFrame({'Transaction Details': transaction_details, 'Withdrawal Amount': withdrawl}).dropna()
    
    return render_template('withdrawal_history.html', withdrawal_history=withdrawal_history)

@app.route('/deposit-history', methods=['POST'])
def deposit_history():
    account_number = request.form['txt3']
    
    # Retrieve data from the bank.xlsx file
    bank = pd.read_excel('bank.xlsx')
    
    # Deposit History
    deposit = bank['DEPOSIT AMT'][bank['Account No'] == account_number]
    transaction_details = bank['TRANSACTION DETAILS'][bank['Account No'] == account_number]
    deposit_history = pd.DataFrame({'Transaction Details': transaction_details, 'Deposit Amount': deposit}).dropna()
    
    return render_template('deposit_history.html', deposit_history=deposit_history)

if __name__ == '__main__':
    app.run(debug=True)
