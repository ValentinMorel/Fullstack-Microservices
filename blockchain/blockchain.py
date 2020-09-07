import uuid
from nameko.rpc import rpc, RpcProxy
from nameko_redis import Redis


class BlockchainService:
    name = "blockchain_service"

    mongo_rpc = RpcProxy('mongo_service')
    redis = Redis('development')

    @rpc
    def create_new_block(self, data):



        return "Hello World !"

    @rpc
    def say_goodbye(self):
        return "Bye, World !"