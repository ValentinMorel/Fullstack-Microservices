import sys 
sys.path.append('python/blockchain/')

from block import Block
from blockchain import Blockchain
import datetime

if __name__ == "__main__" : 
    timestamp = datetime.datetime.now()
    block_test = Block(0, str(timestamp), "genesis", "")

    blockchain = Blockchain()
    blockchain.add_block("2nd block")
    blockchain.add_block("3rd block")
    for i in range(0, len(blockchain.chain)) : 
        print(blockchain.chain[i].get_data())

