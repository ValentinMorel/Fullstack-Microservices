import pymongo
from nameko.rpc import rpc


class MongoService:
    name = 'mongo_service'

    client = pymongo.MongoClient('mongodb+srv://<username>:<password>@cluster0-tdmyp.mongodb.net/test?retryWrites=true&w=majority')
    db = client["test"]
    collection = db["blockchain-microservices"]

    @rpc
    def get_prev_hash(self):
        last_rec = self.collection.find().skip(self.collection.count() - 1)
        data = []
        for i in last_rec : 
            data.append(i)

        # get last hash of chain with : data[0]['prev_hash']
        prev_hash = data[0]['hash']
        print("last hash : ", prev_hash)
        return prev_hash

    @rpc
    def get_prev_index(self):
        last_rec = self.collection.find().skip(self.collection.count() - 1)
        data = []
        for i in last_rec : 
            data.append(i)

        # get last hash of chain with : data[0]['prev_hash']
        prev_index = data[0]['index']
        print("last index : ", prev_index)
        return prev_index

    @rpc
    def insert_to_db(self, data):
        try : 
            self.collection.insert_one(data)
        except : 
            print("The format is unexpected.")

    @rpc
    def get_all(self):
        data = []
        for document in self.collection.find():
            data.append({'index': document['index'],
                         'timestamp': document['timestamp'],
                         'data': document['data'],
                         'prev_hash': document['prev_hash'],
                         'hash': document['hash']})

        return data