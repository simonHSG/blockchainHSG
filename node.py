from uuid import uuid4

from _blockchain import Blockchain
from verification import Verification

class Node:
    def __init__(self):
        self.id = 'Salim'
        self.blockchain = Blockchain(self.id)
        

    def get_transaction_value(self):
        """ allows input of last transaction as a float """
        tx_recipient = input('Enter the recipient of transaction:')
        tx_amount = float(input('Enter transaction amount please: '))
        return tx_recipient, tx_amount


    def get_user_choice(self):
        """ Allows user to make a choice regarding next action (making transaction, mining block, quitting, etc.) """
        user_input = input('Your choice: ')
        return user_input


    def print_blockchain_elements(self):
        """ Outputs blocks of the blockchain """
        for block in self.blockchain.chain:
            print('Outputing Block')
            print(block)
        else:
            print('-' * 20)

    def listen_for_input(self):
        """ allows user to input choices and complete actions on the blockchain """
        waiting_for_input = True

        while waiting_for_input:
            print('Please choose')
            print('1: Add a new transaction value')
            print('2: Mine a new block')
            print('3: Output the blockchain blocks')
            print('4: Check transaction validity')
            print('q: quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                if self.blockchain.add_transaction(recipient, self.id, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed!')
                print(self.blockchain.get_open_transactions())
            elif user_choice == '2':
                self.blockchain.mine_block()
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('All transactions are valid!')
                else:
                    print('There are invalid transactions!')
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print('Input was invalid, please pick a value from the list!')
            if not Verification.verify_chain(self.blockchain.chain):
                self.print_blockchain_elements()
                print('Invalid blockchain!')
                break
            print('Balance of {}: {:6.2f}'.format(self.id, self.blockchain.get_balance()))
        else:
            print('User left!')

        print('Done!')

node = Node()
node.listen_for_input()