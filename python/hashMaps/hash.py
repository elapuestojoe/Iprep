
class HashKey(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return "{}-{}".format(self.key, self.value)
class HashMap(object):
    def __init__(self, size):
        self.array = [None]*size
        self.size = size

    def put(self, key, value):
        position = hash(key) % self.size
        hashObject = HashKey(key, value)

        for i in range(self.size):
            if(self.array[position] is None or self.array[position].key == key):
                self.array[position] = hashObject
                return True
            else:
                position += 1
                position = position % self.size
        return False
    
    def get(self, key):
        position = hash(key) % self.size
        
        for i in range(self.size):
            if(self.array[position] is None):
                return None
            elif(self.array[position].key == key):
                return self.array[position].value
            else:
                position += 1
                position = position % self.size
        return None

myHashMap = HashMap(10)
myHashMap.put("ey", 30)
myHashMap.put("ey", 40)
print(myHashMap.get("ey"))
print(myHashMap.get("e"))
print(myHashMap.array)