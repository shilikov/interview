

TRUE_BALLANS_TUPLE = ('()', '[]', '{}')


LIST_1 = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}',
    '{[}]'
]
LIST_2 = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]



class Stack():
    def __init__(self):
        self.stack = []

    def isEmpty(self) -> bool:
        '''
        Проверяет стек на пустоту.
        Метод возвращает True или False
        '''
        return not self.stack or False


    def push(self, _item) -> None:
        '''
        Добавляет новый элемент на вершину стека.
        Метод ничего не возвращает.
        '''
        self.stack.append(_item)


    def pop(self):
        '''
        Удаляет верхний элемент стека.
        Стек изменяется.
        Метод возвращает верхний элемент стека.
        '''
        return None if self.isEmpty() else self.stack.pop()



    def peek(self):
        '''
        Возвращает верхний элемент стека,
        но не удаляет его.
        Стек не меняется.
        '''
        return None if self.isEmpty() else self.stack[-1]



    def size(self):
        '''
        Возвращает количество элементов в стеке.
        '''
        return len(self.stack)



def check_ballance(data):
    stack = Stack()
    for char in data:
        if char in '([{':
            stack.push(char)
        else:
            if stack.isEmpty():
                return False
            else:
                if stack.peek() + char in TRUE_BALLANS_TUPLE:
                    stack.pop()
                else:
                    return False

    return stack.isEmpty() or False


def main(*ballanced):
    for ballans in ballanced:
        print(f"cбалансированно: {ballans}") if check_ballance(ballans) else print(f"неcбалансированно: {ballans}")


if __name__ == '__main__':
    main(*LIST_1, *LIST_2)






