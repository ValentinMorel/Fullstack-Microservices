from nameko.rpc import RpcProxy, rpc
from nameko.web.handlers import http
import json
import hashlib
import datetime

class GatewayService:
    name = 'gateway'

    blockchain_rpc = RpcProxy('blockchain_service')
    mongo_rpc = RpcProxy('mongo_service')
    
    @rpc
    def add_new_block(self, data):
        prev_hash = self.mongo_rpc.get_prev_hash()
        index = self.mongo_rpc.get_prev_index() + 1
        timestamp = datetime.datetime.now()

        sha = hashlib.sha256()
        sha.update(
            str(index).encode('utf-8')
            + str(timestamp).encode('utf-8')
            + str(data).encode('utf-8')
            + str(prev_hash).encode('utf-8')
        )
        block_hash = sha.hexdigest()

        self.mongo_rpc.insert_to_db({'index': index,
                                     'timestamp': timestamp,
                                     'data': data,
                                     'prev_hash': prev_hash,
                                     'hash': block_hash})
        return "data inserted to DB."

