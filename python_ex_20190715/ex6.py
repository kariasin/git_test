dial_code = dict()
dial_code[86] = 'China'
dial_code[91] = 'India'

def hash_func(data):
    return data % 10
hash_table = list([0 for i in range(10)])

def storage_data(hash_address, data):
    hash_table[hash_address] = data

def get_data(key):
    return hash_table[hash_func(key)]

address = hash_func(86)
storage_data(address, dial_code[86])
print(get_data(86))


data = list([0 for i in range(8)])
print(data)

