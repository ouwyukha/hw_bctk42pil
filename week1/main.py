import sys
import random
from getpass import getpass
from eth_hash.auto import keccak

class MockBank:
    def __init__(self):
        self.MAX_RETRY = 3
        self.vault = {
            'user1': {
                'password': keccak(b'password_1'),
                'coin': random.randint(1, 100)
            },
            'user2': {
                'password': keccak(b'password_2'),
                'coin': random.randint(1, 100)
            },
            'user3': {
                'password': keccak(b'password_3'),
                'coin': random.randint(1, 100)
            }
        }

    def incorrectPassword(self, retry):
        retry += 1
        print('Incorrect Username or Password, retry {}/{}'.format(retry, self.MAX_RETRY))
        if retry == self.MAX_RETRY:
            print('Reached max attempts, Exit.')
        else:
            self.login(retry)
    
    def correctPassword(self, username):
        print('')
        print('Welcome back, {} !'.format(username))
        print('Your balance : {} coins'.format(self.vault[username]['coin']))
    
    def login(self, retry):
        username = input('Username: ')
        password = getpass('Password: ')

        if username not in self.vault or self.vault[username]['password'] != keccak(password.encode('ascii')):
            self.incorrectPassword(retry)
        else:
            self.correctPassword(username)

    def run(self):
        retry = 0
        print("Welcome to MockBank\n==Login==")
        self.login(0)

if __name__ == '__main__':
    app = MockBank()
    app.run()