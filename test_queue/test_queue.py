from Queue import QueueC

# возможно стоило использоевать фикстуру для класса
# Но я не уверен что правильно из одного файла для разных тестов использовать фикстуры мне показалось это не правильным решил так
# можно так делать вообще?
def test_IsEmpty():
    q = QueueC()
    assert q.isEmpty() == True
    q.enqueue(1)
    assert q.isEmpty() == False


def test_IsFull():
    q = QueueC(2)
    assert q.IsFull() == False
    q.enqueue("1")
    assert q.IsFull() == False
    q.enqueue(11)
    assert q.IsFull() == True


