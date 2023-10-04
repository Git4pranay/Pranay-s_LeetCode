from collections import defaultdict
class MyHashMap:

    def __init__(self):
        self.data=defaultdict()

    def put(self, key: int, value: int) -> None:
        self.data[key]=value

    def get(self, key: int) -> int:
        value=self.data.get(key)
        return value if value != None else -1

    def remove(self, key: int) -> None:
        self.data[key]=None