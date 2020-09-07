import uuid
from nameko.rpc import rpc, RpcProxy
from nameko_redis import Redis


class BlockService:
    name = "block_service"
    redis = Redis('development')

    @rpc
    def create_new_block(self, data):
        
        return "Hello World !"

    @rpc
    def say_goodbye(self):
        return "Bye, World !"