import pymongo
import hashlib
import datetime 
import json


class Block(object): 
    def __init__(self, index : int, timestamp : str, data: str, prev_hash : str):
        self.index = index 
        self.timestamp = timestamp
        self.data = data 
        self.prev_hash = prev_hash 
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(
            str(self.index).encode('utf-8')
            + str(self.timestamp).encode('utf-8')
            + str(self.data).encode('utf-8')
            + str(self.prev_hash).encode('utf-8')
        )
        return sha.hexdigest()

    def get_data(self):
        return {'index': self.index,
                'timestamp': self.timestamp,
                'data': self.data,
                'prev_hash': self.prev_hash,
                'hash': self.hash}

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


blockchain = Blockchain()
blockchain.add_block("2nd block")
blockchain.add_block("3rd block")

    
client = pymongo.MongoClient('mongodb+srv://<username>:<password>@cluster0-tdmyp.mongodb.net/test?retryWrites=true&w=majority')

db = client["test"]
collection = db["blockchain-microservices"]


####### TEST CODE GOES HERE TO PERFORM SOME REQUESTS ON THE DATABASE #######
"""
for i in range(0, len(blockchain.chain)) : 
    data = blockchain.chain[i].get_data()
    collection.insert_one(data)


last_rec = collection.find().skip(collection.count() - 1)

data = []
for i in last_rec : 
    data.append(i)

# get last hash of chain with : data[0]['prev_hash']
print("last hash : ", data[0]['prev_hash'])


for document in collection.find():
    print(json.dumps({'index':document['index'], 'data':document['data']}))
"""