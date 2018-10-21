# HashMap Implementation
# To do: Implement delete and rehashing
class HashedElement:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self):
        # Initialize a 16 empty storage array
        self.store = [None for _ in range(16)]

    def get(self, key):
        #get key hash and modulo 16
        index = hash(key) & 15

        if(self.store[index] is None):
            return None
        
        n = self.store[index]
        while(True):
            if(n.key == key):
                return n.value

            #Collision handling
            else:
                if(n.next):
                    n = n.next
                else:
                    return None
    def put(self, key, value):
        hashedElement = HashedElement(key, value)
        index = hash(key) & 15
        
        cell = self.store[index]
        if(cell is None):
            self.store[index] = hashedElement
        else:
            if(cell.key == key):
                #Update value
                cell.value = value
            else:
                #Handle Collision
                while(cell.next):
                    if(cell.key == key):
                        cell.value = value
                        return
                    else:
                        cell = cell.next
                cell.next = hashedElement

#Driver code
hashMap = HashMap()
hashMap.put("3", "hey")
hashMap.put("2", "there")

print(hashMap.get("3"))
print(hashMap.get("2"))