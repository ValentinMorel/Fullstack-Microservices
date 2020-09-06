import hashlib

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

    