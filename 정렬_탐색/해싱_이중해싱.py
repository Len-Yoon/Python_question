class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_func1(self, key):
        # 첫 번째 해시 함수
        return hash(key) % self.size

    def hash_func2(self, key):
        # 두 번째 해시 함수 (0이 안 나오게 1 더함)
        return 1 + (hash(key) % (self.size - 1))

    def insert(self, key, value):
        idx1 = self.hash_func1(key)
        idx2 = self.hash_func2(key)
        # 충돌 시 두 번째 해시 함수로 간격을 정해 빈칸 탐색
        for i in range(self.size):
            probe_idx = (idx1 + i * idx2) % self.size
            if self.table[probe_idx] is None or self.table[probe_idx][0] == key:
                self.table[probe_idx] = (key, value)
                return
        raise Exception("Hash table is full")

    def search(self, key):
        idx1 = self.hash_func1(key)
        idx2 = self.hash_func2(key)
        # 같은 방식으로 탐색
        for i in range(self.size):
            probe_idx = (idx1 + i * idx2) % self.size
            if self.table[probe_idx] is None:
                return None
            if self.table[probe_idx][0] == key:
                return self.table[probe_idx][1]
        return None

# 사용 예시
ht = DoubleHashingHashTable(5)
ht.insert('apple', 1)
ht.insert('banana', 2)
ht.insert('grape', 3)
print(ht.search('banana'))  # 2 출력