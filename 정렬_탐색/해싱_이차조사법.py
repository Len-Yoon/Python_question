class QuadraticProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_func(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self.hash_func(key)
        # 충돌이 발생하면 i^2만큼 떨어진 곳을 탐색
        for i in range(self.size):
            probe_idx = (idx + i * i) % self.size
            if self.table[probe_idx] is None or self.table[probe_idx][0] == key:
                self.table[probe_idx] = (key, value)
                return
        raise Exception("Hash table is full")

    def search(self, key):
        idx = self.hash_func(key)
        # i^2만큼 떨어진 곳을 순차적으로 탐색
        for i in range(self.size):
            probe_idx = (idx + i * i) % self.size
            if self.table[probe_idx] is None:
                return None
            if self.table[probe_idx][0] == key:
                return self.table[probe_idx][1]
        return None

# 사용 예시
ht = QuadraticProbingHashTable(5)
ht.insert('apple', 1)
ht.insert('banana', 2)
ht.insert('grape', 3)
print(ht.search('banana'))  # 2 출력