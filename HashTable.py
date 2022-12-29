class HashTable():

    def __init__(self, size):
        self.size = size
        self.hashTable = self.createBuckets()
    
    def createBuckets(self):
        return [ [] for _ in range(self.size)]
    
    # For inserting values into hashmap
    def setVal(self, key, val):

        # Get index using hash function
        hashedKey = hash(key) % self.size

        # Get corresponding bucket
        bucket = self.hashTable[hashedKey]

        foundKey = False
        for index, record in enumerate(bucket):
            recordKey, recordVal = record

            # Check if bucket has same key as value to be inserted
            if recordKey == key:
                foundKey = True
                break
        # If there was match, update key value
        # Otherwise, add new key-value pair to bucket
        if foundKey:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))
        
    # Return searched value with given key
    def getVal(self, key):

        hashedKey = hash(key) % self.size

        bucket = self.hashTable[hashedKey]

        foundKey = False
        for index, record in enumerate(bucket):
            recordKey, recordVal = record

            if recordKey == key:
                foundKey = True
                break
        
        # If there was match, return value
        # Otherwise, there was no match
        if foundKey:
            return recordVal
        else:
            return "No record found"
    
    # For this program, there is no need to delete key-values from the table