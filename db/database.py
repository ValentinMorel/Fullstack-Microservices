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
