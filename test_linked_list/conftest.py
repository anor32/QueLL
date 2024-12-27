import pytest

from LinkedListClass import Node, LinkedList


@pytest.fixture
def linl():
    Ll = LinkedList()
    return Ll