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

    assert linl.insert_at_end("223") =="Узел с данными 223 добавлен в конец списка"
    assert linl.head.next_node.data == "223"


def test_remove_node(linl):
    linl.insert_at_head(1)
    linl.insert_at_head(2)
    linl.insert_at_head(3)
    assert linl.remove_node_position(1) == 'Удален узел с данными 3 позиции 1'
    assert linl.remove_node_position(2) == 'Удален узел с данными 1 позиции 2'
    assert linl.remove_node_position(10) == 'Ничего не удалено'

def