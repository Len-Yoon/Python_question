class MyList:
    def __init__(self):
        "리스트 초기화"
        self.my_list = list()

    def insert(self, poe, e):
        "리스트의 지정된 위치(poe)에 값 e를 삽입"
        self.my_list.insert(poe, e)

    def delete(self, pos):
        "리스트에서 지정된 위치(pos)의 값을 삭제"
        self.my_list.pop(pos)

    def isEmpty(self):
        "리스트가 비어있는지 확인하고 메시지를 출력"
        if not self.my_list:
            print("리스트가 비어있어요!")
        else:
            print("리스트에 값이 있어요! =>", self.my_list)

    def size(self):
        "리스트의 크기를 반환"
        return len(self.my_list)

    def clear(self):
        "리스트를 비움"
        self.my_list.clear()

    def find(self, item):
        "리스트에서 item의 인덱스를 반환"
        return self.my_list.index(item)

    def replace(self, pos, item):
        "리스트에서 지정된 인덱스(pos)의 값을 item으로 교체"
        self.my_list[pos] = item
        return self.my_list

    def sorting(self):
        """리스트를 오름차순으로 정렬"""
        self.my_list.sort()
        return self.my_list

    def merge(self, list):
        "리스트에 다른 리스트(list)를 병합"
        self.my_list.extend(list)
        return self.my_list

    def append(self, item):
        "리스트에 item을 추가"
        self.my_list.append(item)
        return self.my_list


# 실행 예시
my_list_obj = MyList()

my_list_obj.insert(0, 3)
my_list_obj.insert(1, 5)
print("insert 실행 후 =>", my_list_obj.my_list)

my_list_obj.delete(0)
print("delete(pop) 실행 후 =>", my_list_obj.my_list)

my_list_obj.isEmpty()

print("my_list의 길이 =>", my_list_obj.size())

my_list_obj.clear()
print("clear 실행 후 =>", my_list_obj.my_list)

my_list_obj.insert(0, 7)
my_list_obj.insert(1, 9)
my_list_obj.insert(2, 11)

print("my_list에서 11인 값에 인덱스 =>", my_list_obj.find(11))

print("my_list에서 0번째 인덱스 값 13으로 교체 =>", my_list_obj.replace(0, 13))

print("my_list에서 sort =>", my_list_obj.sorting())

print("my_list에 [17, 18, 19] 추가 =>", my_list_obj.merge([17, 18, 19]))

print("my_list에 20 값 추가 =>", my_list_obj.append(20))