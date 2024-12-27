import pytest

from LinkedListClass import Node


# тест ноды
def test_node_init():
    node_1 = Node(1)
    assert node_1.data == 1
    assert node_1.next_node == None
    node_2 = Node(2, node_1)
    assert node_2.next_node.data == 1


# тест списка
def test_Ll_init(linl):
    assert linl.head == None


def test_insert_head(linl):
    linl.insert_at_head(1)
    assert linl.head.data == 1
    assert linl.insert_at_head(2) == 'Узел с данными 2 добавлен в начало списка'
    assert linl.head.data == 2


def test_insert_end(linl):
    assert linl.insert_at_end(2) == None
    assert linl.head.data == 2

    assert linl.insert_at_end("223") == "Узел с данными 223 добавлен в конец списка"
    assert linl.head.next_node.data == "223"


def test_remove_node(linl):
    linl.insert_at_head(1)
    linl.insert_at_head(2)
    linl.insert_at_head(3)
    assert linl.remove_node_position(1) == 'Удален узел с данными 3 позиции 1'
    assert linl.remove_node_position(2) == 'Удален узел с данными 1 позиции 2'
    assert linl.remove_node_position(10) == 'Ничего не удалено'


def test_insert_at_position(linl):
    assert linl.insert_at_position("test_1", 1) == 'Узел с данными test_1 добавлен на позицию 1'
    assert linl.insert_at_position("test_2", 2) == 'Узел с данными test_2 добавлен на позицию 2'
    assert linl.insert_at_position("test_3", 5) == (None, 'не найдена позиция')


def test_print_ll(linl):
    linl.insert_at_head(1)
    linl.insert_at_head(2)
    linl.insert_at_head(3)

    assert linl.print_ll() == "Данные списка выведены"


def test_get(linl):
    linl.insert_at_head("hello")
    linl.insert_at_head("world")
    linl.insert_at_head("python")

    assert linl.get("world")[0] == True
    assert linl.get("abracadabra")[0] == False

def test_change_data(linl):
    linl.insert_at_head("hello")
    linl.insert_at_head("world")
    linl.insert_at_head("python")
    assert linl.change_data("python","abracadabra") =="Заменены данные в узле № 1"
    assert linl.change_data("abracadabra","python") =="Заменены данные в узле № 1"
    assert linl.change_data("wewe","abracadabra") =="Данные не обнаружены"
