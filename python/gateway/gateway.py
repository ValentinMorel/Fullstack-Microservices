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

        new_block = self.blockchain_rpc.create_new_block(index, timestamp, data, prev_hash)

        self.mongo_rpc.insert_to_db(new_block)
        
        return "data inserted to DB."

    @rpc
    def get_blockchain(self):
        blockchain = self.mongo_rpc.get_all()
        return blockchain

