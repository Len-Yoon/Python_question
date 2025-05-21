class ChainingHashTable:
    def __init__(self, size):
        self.size = size
        # 각 버킷에 리스트(연결 리스트 역할)를 할당
        self.table = [[] for _ in range(size)]

    def hash_func(self, key):
        # 해시 함수: 파이썬 내장 hash() 사용 후 테이블 크기로 나눔
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self.hash_func(key)
        # 이미 같은 키가 있으면 값을 갱신
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        # 없으면 리스트에 (key, value) 추가
        self.table[idx].append((key, value))

    def search(self, key):
        idx = self.hash_func(key)
        # 해당 버킷의 리스트에서 키를 탐색
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None  # 찾지 못한 경우

# 사용 예시
ht = ChainingHashTable(5)
ht.insert('apple', 1)
ht.insert('banana', 2)
ht.insert('grape', 3)