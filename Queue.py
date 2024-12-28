class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class QueueC:
    def __init__(self, size_max=5):
        self.head = None
        self.tail = None
        self.size_q = 1
        self.size_max = size_max

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif self.size_q < self.size_max:
            self.tail.next_node = new_node
            self.size_q += 1
        else:
            print("заполнен")
            return "заполен"
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return "пустая очередь"
        else:
            qu_item = self.head
            self.head = self.head.next_node
        return qu_item.data

    def show(self):
        if self.head is None:
            return "пустая очередь"
        curent_elem = self.head
        while curent_elem:
            print(curent_elem.data)
            curent_elem = curent_elem.next_node

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def IsFull(self):
        return self.size_max == self.size_q

# подобие интерфейса
user_input = input("начать работу с очередью, да/нет")

if user_input == "да":
    q = QueueC(int(input("введите лимит очереди стандартно 5")))
    user_end = "старт"
    while user_end != "0":
        user_end = (input("выберите действие\nдобавить в очередь 1\n"
                          "убрать из очереди 2\n показать содержимое 3\n"
                          "проверить пустая ли очередь 4\n"
                          "проверить полная  ли очередь 5\n"
                          "завершить работу 0\n"
                          ))
        if user_end == "1":
            q.enqueue(input("введите данные для добавления"))

        elif user_end == "2":
            q.dequeue()
            print("данные удалены из очереди")
        elif user_end == "3":
            q.show()
            print('данные успешно выведены')
        elif user_end == "4":
           print(f"на данный момент очередь является {("не пустой","пустой")[q.isEmpty()]}")
        elif user_end == "5":
            print(f"на данный момент очередь является {("не полной", "полной")[q.IsFull()]}")
        print()