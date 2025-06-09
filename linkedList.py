from typing import Optional


class Node:
    """Узел односвязного списка"""

    def __init__(self, data: str, next: Optional["Node"] = None) -> None:
        """
        Инициализация узла
        """
        self.data = data
        self.next = next


class LinkedList:
    """Односвязный список"""

    def __init__(self) -> None:
        """Инициализация списка"""
        self.head = None

    def push(self, data: str) -> None:
        """
        Добавление элемента в начало списка
        """
        try:
            if not data:
                raise Exception("Вы не ввели значение")
            node = Node(data, self.head)
            self.head = node
        except Exception as ex:
            print(ex)

    def pop(self) -> Optional[str]:
        """
        Удаление элемента из начала списка
        """
        try:
            if self.head is None:
                raise Exception("Список пуст")

            data = self.head.data
            self.head = self.head.next
            return data
        except Exception as ex:
            print(ex)
            return None
        
    def reverse(self) -> None:
        """
        Разворачивает список
        """
        previous = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        self.head = previous

    def __str__(self) -> str:
        """
        Представление списка в виде строки
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)

