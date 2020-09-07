from nameko.rpc import RpcProxy, rpc
from nameko.web.handlers import http
import json

class GatewayService:
    name = 'gateway'

    blockchain_rpc = RpcProxy('blockchain_service')
    mongo_rpc = RpcProxy('mongo_service')
    
    @rpc
    def get_hello(self):
        resp = self.mongo_rpc.get_prev_hash()
        return json.dumps(resp)
