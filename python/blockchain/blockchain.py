from block import Block
import datetime 


class Blockchain(object):
    def __init__ (self, first_block = None):
        self.first_block = first_block
        self.chain = []

        if len(self.chain) == 0 and self.first_block is None :
            self.create_genesis_block()
        else : 
            self.chain.append(self.first_block)
    
    def create_genesis_block(self):
        gen_block = Block(
            index = 0,
            timestamp = datetime.datetime.now(),
            data = 'genesis block',
            prev_hash = ''
        )
        self.chain.append(gen_block)
        return
    
    def add_block(self, data):
        index = len(self.chain)
        previous_hash = self.chain[-1].hash
        timestamp = str(datetime.datetime.now())

        new_block = Block (
            index=index,
            timestamp=timestamp,
            data = data,
            prev_hash=previous_hash
        )
        self.chain.append(new_block)
