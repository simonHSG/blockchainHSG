from time import time

from printable import Printable

class Block(Printable):
    """ creates a Block class object with its index, transactions, proof and timestamp """
    def __init__(self, index, previous_hash, transactions, proof, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.proof = proof
        self.timestamp = time() if timestamp is None else timestamp
    
