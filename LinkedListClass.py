class Node:
    """основной класс для связывания узлами принимает текущий узел и следующий"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """связаный список инциализация без передачи параметров """

    def __init__(self):
        self.head = None
        """метод для вставки элемента в с начала списка принимает данные для вставки"""

    def insert_at_head(self, data):
        new_node = Node(data)  # связываем ноду
        if self.head is None:  # проверка на наличие данных дальше таких много  просто переназначем голову
            self.head = new_node
        else:
            new_node.next_node = self.head  # если данные есть связываем с текущими
            self.head = new_node
        return f"Узел с данными {new_node.data} добавлен в начало списка"

    """метод для вставки элемента в с конец списка принимает данные для вставки"""

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:  # проверка на наличие данных в целом тоже самое что и первый только инвертировано
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:  # итерируем по нодам пока  нода не равна None
            current_node = current_node.next_node
        current_node.next_node = new_node  # после последней ноды создаем и добавляем в  список
        return f"Узел с данными {new_node.data} добавлен в конец списка"

    """метод для удаления элемента по индексу принимает индекс """

    def remove_node_position(self, rm_position):
        if rm_position == 1:  # быстрая проверка на первый индекс
            removed_node = self.head
            self.head = self.head.next_node  # переназначаем следущую ноду  за место головы
            return f"Удален узел с данными {removed_node.data} позиции {rm_position}"
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < rm_position - 1:  # итерация до нужного индекса
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None or current_node.next_node is None:  # проверка если идекс неверный
            return "Ничего не удалено"
        removed_node = current_node.next_node  # сохраняем данные которые удалим
        current_node.next_node = current_node.next_node.next_node  # удаление элемента
        return f"Удален узел с данными {removed_node.data} позиции {rm_position}"

    """метод вставки на позицию принимает данные для вставки и позицию"""

    def insert_at_position(self, data, node_position):
        new_node = Node(data)
        if node_position == 1:  # быстрая проверка на первый индекс
            self.insert_at_head(data)
            # new_node.next_node = self.head
            # self.head = new_node
            return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"
        """Опционально"""
        current_node = self.head
        # if node_position > self.len_ll():
        #     self.insert_at_end(data)
        #     # while current_node.next_node:
        #     #     current_node = current_node.next_node
        #     # current_node.next_node = new_node
        #     return
        current_node_position = 1
        while current_node is not None and current_node_position < node_position - 1:  # итерация до нужного индекса
            current_node = current_node.next_node
            current_node_position += 1
        """Если есть опционально (код выше то следующие 2 строки не нужны)"""
        if current_node is None:
            return None, "не найдена позиция"
        new_node.next_node = current_node.next_node  # добавляем на указаную позицию
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"

    """вывод всех элементов списка ничего не примает выводит элементы"""

    def print_ll(self):
        current_node = self.head
        while current_node:  # итерация по всем элементов и последующий вывод каждого
            #  print(current_node.data) для теста закоментировал
            current_node = current_node.next_node

        return "Данные списка выведены"

    """метод для проверки наличия эелемента в списке принимает данные для проверки"""

    def get(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:  # если данные текущей ноды равны указаным
                return True, current_node  # возврат кортежа
            current_node = current_node.next_node  # для итерации
        return False, None  # если ложно условие
    """метод для замены данных принимает старые данные и новые для замены меняет меняет старые на новые"""
    def change_data(self, node_data, change_data):
        current_node = self.head
        current_node_position = 1
        while current_node:
            if current_node.data == node_data: # если нашли старые данные
                current_node.data = change_data  # замена на новые данные
                return f"Заменены данные в узле № {current_node_position}"
            current_node = current_node.next_node
            current_node_position += 1
        return "Данные не обнаружены" # если if == False Сответвие данных не найдено

    # def change_data(self, node_data, change_data):
    """Это второй способ для примера"""
    #     result, current_node = self.get(node_data)
    #     if result:
    #         current_node.data = change_data
    #         return "Данные изменены!"
    #     return "Данные не обнаружены"



# вы мне указали в одной из домашек на коментарии как их писать надо что немного странно потому что в задании сказано писать док стринги
# я вообщем не понял что имелось ввиду я добавил коментарии тоже на всякий случай
# теперь в файле док стринги и коментарии