from time import time
import hashlib
import json


class Blockchain(object):
    def __init__(self):
        self._chain = []
        self._current_transactions = []

        self._create_genesis_block()

    def chain(self):
        return self._chain

    def _create_genesis_block(self):
        """
        Creates the first block
        :return: void
        """
        self.new_block(proof=100, previous_hash=1)

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined block
        :param sender: <str> address of the sender
        :param recipient: <str> address of the recipient
        :param amount: <int> amount
        :return: <int> index of the block that will hold this transaction
        """

        self._current_transactions.append({
            'sender': sender,
            'recivier': recivier,
            'amount': amount
        })

        return self.last_block['index'] + 1

    def new_block(self, proof, previous_hash=None):
        """
        Creates a new block in the Blockchain
        :param proof: <int> The output of the ProofOfWork algorithm
        :param previous_hash: (Optional) <int> Hash of the previous block
        :return: <dict> New block
        """

        block = {
            'index': len(self._chain) + 1,
            'timestamp': time,
            'transactions': self._current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self._chain[-1])
        }

        # Reset the current transactions:
        self._current_transactions = []

        self._chain.append(block)
        return block

    def proof_of_work(self, previous_proof):
        """
        Simple implementation of the Proof Of Work algorithm:
        - Find a number p' such that hash(pp') contains leading 4 zeros
        - p is previous proof and p' is the new proof
        :param previous_proof: <int>
        :return: <int> new proof
        """

        proof = 0
        while not self._check_proof(previous_proof, proof):
            proof += 1

        return proof

    def _check_proof(self, previous_proof, proof):
        """
        Checks is the hash(previous_proof, proof) contains 4 leading zeros
        :param previous_proof: <int>
        :param proof: <int>
        :return: <bool> True is correct, else False
        """

        guess_string = f'{previous_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess_string).hexdigest()
        return guess_hash[:4] == '0000'

    @property
    def last_block(self):
        """
        Returns the last block in the chain
        :return: <int> last block index
        """

        pass

    @staticmethod
    def hash(self, block):
        """
        Creates SHA-256 hash of the block
        :param block: <dict> block
        :return: <std> SHA-256 hash of the input block
        """
        block_string = json.dump(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
