from linkedList import LinkedList

class Engine:
    """Абстрактная вычислительная машина"""

    def __init__(self, expression: str) -> None:
        """
        Инициализация компилятора
        """
        self.stack = LinkedList()
        self.instructions = LinkedList()
        self.operators = {'+': 'AD', '-': 'SB', '*': 'ML', '/': 'DV'}
        self.n = len(expression)
        self.temp_count = 1
        self.expression = expression

    def compile(self):
        """
        Конвертирование выражения в постфиксной форме в формулировку из задания
        """
        for i, c in enumerate(self.expression):
            if c.isalpha():
                self.stack.push(c)
            elif c in self.operators:
                right = self.stack.pop()
                left = self.stack.pop()
                if(right is None or left is None):
                    raise Exception("Недостаточно операндов")
                    
                self.instructions.push(f"LD {left}")
                self.instructions.push(f"{self.operators[c]} {right}")

                temp_var = None
                if i < self.n - 1:
                    if right.startswith("T") and right[1:].isdigit():
                        temp_var = right
                    elif left.startswith("T") and left[1:].isdigit():
                        temp_var = left
                    else:
                        temp_var = f"T{self.temp_count}"
                        self.temp_count += 1

                    self.instructions.push(f"ST {temp_var}")
                    self.stack.push(temp_var)
    
    def run(self)  -> None:
        """
        Запуск
        """
        try:
            self.compile()
            if(not self.instructions.head):
                raise Exception("Некорректный список")
            self.instructions.reverse()
            while self.instructions.head:
                print(self.instructions.pop())
        except Exception as ex:
            print(ex)
            return None


if __name__ == "__main__":
    Engine("ABC*+DE-/").run()