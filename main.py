from web3 import Web3
import os
import hashlib
import time
import random

GANACHE_URL = 'http://192.168.1.138:7545'
INFURA_URL = ''
LOGS_DIR = './logs'
MINED_FILE = './mined.txt'

def check_balance_and_perform_action(address):
    if (not web3.is_address(address)): return
    
    balance_wei = web3.eth.get_balance(address)
    balance_eth = web3.from_wei(balance_wei, 'ether')

    # You can adjust the balance threshold based on your needs
    if balance_eth > 0.00001:  # For example, if the balance is greater than 0.1 ETH
        return True, f"Balance condition met: {balance_eth} ETH"
    else:
        return False, f"Balance condition not met: {balance_eth} ETH"

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

unix_date = str(int(time.time()))

def log_write(data, log_filename):
    log_string = f'\n{str(int(time.time()))}\t'

    if not os.path.exists(log_filename):
        with open(log_filename, 'w'):
            pass

    with open(log_filename, 'a+') as file:
        log_string += f'{data}'
        file.write(log_string)

web3 = Web3(Web3.HTTPProvider(GANACHE_URL))

while True:
    flag = 0
    private_key = "0x" + os.urandom(32).hex()
    account = web3.eth.account.from_key(private_key)
    data = {account.address, private_key}
    
    if (check_balance_and_perform_action(account.address) == True):
        log_write(data, MINED_FILE)
        print(data, '\t balance condition met')    
        
    log_write(data, f'{LOGS_DIR}/{unix_date}.log')
    