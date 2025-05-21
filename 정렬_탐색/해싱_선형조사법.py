class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        # 각 버킷에 하나의 값만 저장
        self.table = [None] * size

    def hash_func(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self.hash_func(key)
        # 충돌이 발생하면 한 칸씩 순차적으로 빈칸을 찾음
        for i in range(self.size):
            probe_idx = (idx + i) % self.size
            # 빈 공간이거나, 동일 키가 있으면 삽입/갱신
            if self.table[probe_idx] is None or self.table[probe_idx][0] == key:
                self.table[probe_idx] = (key, value)
                return
        raise Exception("Hash table is full")  # 테이블이 가득 찬 경우

    def search(self, key):
        idx = self.hash_func(key)
        # 한 칸씩 이동하며 탐색
        for i in range(self.size):
            probe_idx = (idx + i) % self.size
            if self.table[probe_idx] is None:
                return None  # 찾지 못함
            if self.table[probe_idx][0] == key:
                return self.table[probe_idx][1]
        return None

# 사용 예시
ht = LinearProbingHashTable(5)
ht.insert('apple', 1)
ht.insert('banana', 2)
ht.insert('grape', 3)
print(ht.search('banana'))  # 2 출력