import hashlib
import datetime
data = b'Hello World'
hash_object = hashlib.sha256()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
#print(hex_dig)

hash_object.update(hex_dig.encode())
hax_dig = hash_object.hexdigest()
#print(hex_dig)

class Block:
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hash_block()

    def hash_block(self):
        hash_object = hashlib.sha256()
        hash_data = str(self.index) + str(self.timestamp) + str(self.data) + str(self.prev_hash)
        hash_object.update(hash_data.encode())
        return hash_object.hexdigest()

def create_genesis_block():
    return Block(0, datetime.datetime.now(), "Genesis Block", "0")

def next_block(prev_block):
    index = prev_block.index + 1
    timestamp = datetime.datetime.now()
    data = "Dave Block" + str(index)
    return Block(index, timestamp, data, prev_block.hash)

blockchain = [create_genesis_block()]
prev_block = blockchain[0]

for index in range(10):
    new_block = next_block(prev_block)
    blockchain.append(new_block)
    prev_block = new_block

    print("Block Index: " + str(new_block.index))
    print("Hash Value: " + str(new_block.hash))
