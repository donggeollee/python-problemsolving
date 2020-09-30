import hashlib

class HashTable:
    def __init__(self, index_count):
        self.index_count = index_count
        self.hash_table = list([None for i in range(index_count)])

    def get_hash(self, key):
        return ord(key[0])

    def indexing(self, hash_code):
        return hash_code % self.index_count

    def put(self, key, value):
        hash_code = self.get_hash(key)
        index = self.indexing(hash_code)
        self.hash_table[index] = value

    def get(self, key):
        hash_code = self.get_hash(key)
        index = self.indexing(hash_code)
        return self.hash_table[index]

class HashTableChaining:
    def __init__(self, index_count):
        self.index_count = index_count
        self.hash_table = list([None for i in range(index_count)])

    def get_hash(self, key):
        encoded_key = key.encode()
        hash_obj = hashlib.sha256()
        hash_obj.update(encoded_key)
        return int(hash_obj.hexdigest(),16)

    def indexing(self, hash_code):
        return hash_code % self.index_count

    def put(self, key, value):
        hash_code = self.get_hash(key)
        index = self.indexing(hash_code)
        if not self.hash_table[index] :
            self.hash_table[index] = [(hash_code, value)]
            return True
        else :
            # 동일한 key의 데이터가 추가 됐을 때 나중에 들어온 데이터로 덮어씌움
            for i in range(len(self.hash_table[index])) :
                if self.hash_table[index][i][0] == hash_code :
                    self.hash_table[index][i] = (hash_code,value)
                    return True
            self.hash_table[index].append((hash_code, value))

    def get(self, key):
        hash_code = self.get_hash(key)
        index = self.indexing(hash_code)
        if self.hash_table[index] == None :
            print("데이터가 존재하지 않습니다.")
            return False
        else :
            for i in range(len(self.hash_table[index])) :
                if self.hash_table[index][i][0] == hash_code :
                    return self.hash_table[index][i][1]
            print("데이터가 존재하지 않습니다.")
            return False

            
# hashTable main
hash_table = HashTable(16)
hash_table.put("lee","01099998888")
hash_table.put("build","01044443333")

print("##### hash_table.hash_table #####")
print(hash_table.hash_table)

print("##### hash_table.get #####")
print(hash_table.get("lee"))
print(hash_table.get("build"))

# HashTableChaining main
hash_table = HashTableChaining(16)

hash_table.put("lee","01099998888")
hash_table.put("build","01044443333")

# duplicate key test
print("##### duplicate key #####")
hash_table.put("build","%?%?%?%?")

# hash collision test
hash_table.put("dd","dd")
hash_table.put("hy","hy")

hash_table.put("dc","dc")
hash_table.put("fd","fd")

hash_table.put("jm","jm")
hash_table.put("zx","zx")

print("##### get #####")
print(hash_table.get("lee"))
print(hash_table.get("build"))
print(hash_table.get("dd"))
print(hash_table.get("hy"))
print(hash_table.get("dc"))
print(hash_table.get("fd"))
print(hash_table.get("jm"))
print(hash_table.get("zx"))
print(hash_table.get("123123"))

print("##### hash_table #####")
print(hash_table.hash_table)