import uuid
from nameko.rpc import rpc, RpcProxy
from nameko_redis import Redis
import hashlib
import json


class BlockchainService:
    name = "blockchain_service"

    @rpc
    def create_new_block(self, index, timestamp, data, prev_hash):
        sha = hashlib.sha256()
        sha.update(
            str(index).encode('utf-8')
            + str(timestamp).encode('utf-8')
            + str(data).encode('utf-8')
            + str(prev_hash).encode('utf-8')
        )
        block_hash = sha.hexdigest()
        return {'index': index,
                'timestamp': timestamp,
                'data': data,
                'prev_hash': prev_hash,
                'hash': block_hash}

    @rpc
    def say_goodbye(self):
        return "Bye, World !"