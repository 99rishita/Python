class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr=[None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for j in key:
            h += ord(j)
        return h%100
    
    '''def add(self, key, value):
        index=self.get_hash(key)
        self.arr[index]=value

    def get(self, key):
        index=self.get_hash(key)
        print(self.arr[index])'''

    def __setitem__(self, key, value):
        index=self.get_hash(key)
        self.arr[index]=value

    def __getitem__(self, key):
        index=self.get_hash(key)
        print(self.arr[index])

    def __delitem__(self, key):
        index = self.get_hash(key)
        self.arr[index] = None

t = HashTable()
#t.add('march 6', 121) #add key and value
#t.get('march 6') #get the value
t['march 6'] = 130
t['march 16'] = 25
t['nov 18'] = 1 #add key value pair as done in dictionary
t['march 6']
#del t['march 6']
print(t.arr)
