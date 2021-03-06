# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""

class StackClass:
    def __init__(self, max_size):
        self.elems = [[]]
        self.max_size = max_size

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в начале списка"""
        if len(self.elems[0]) >= self.max_size:
            self.elems.insert(0, [])
        self.elems[0].insert(0, el)

    def pop_out(self):
        if self.is_empty():     # Проверка на попытку извлечь занчение из пустого стека
            return None
        else:
            result = self.elems[0].pop(0)
            if len(self.elems[0]) == 0 and len(self.elems) > 1:     # уберем вложенный стек, если он "не последний"
                self.elems.pop(0)
            return result

    def get_val(self):
        if self.is_empty():     # Проверка на попытку извлечь занчение из пустого стека
            return None
        else:
            return self.elems[0][0]

    def stack_size(self):       # общее количество "тарелок"
        size = 0
        for el in self.elems:
            size += len(el)
        return size

    def stack_count(self):      # количество стеков с тарелками
        return len(self.elems)


if __name__ == '__main__':
    SC_OBJ = StackClass(3)      # создадим экземпляр с глубиной наполнения "3"

    print('Стек пуст? ', SC_OBJ.is_empty())                                 # -> стек пустой
    print('Получить верхний элемент, без удаления: ', SC_OBJ.get_val())     # Проверка на отработку без ошибок
    print('Убираем с вершины стека: ', SC_OBJ.pop_out())                    # Проверка на отработку без ошибок
    print(SC_OBJ)

    # наполняем стек
    for i in range(10):
        SC_OBJ.push_in(i)
    print(SC_OBJ)

    # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
    print('Получить верхний элемент, без удаления: ', SC_OBJ.get_val())
    print(SC_OBJ)

    # узнаем размер стека
    print('Общее количество тарелок: ', SC_OBJ.stack_size())

    # узнаем количество стеков (стоек) в стеке
    print('Количество стоек в стеке: ',SC_OBJ.stack_count())

    # убираем элемент с вершины стека и возвращаем его значение
    print('Убираем с вершины стека: ', SC_OBJ.pop_out())
    print(SC_OBJ)
    # убираем элемент с вершины стека и возвращаем его значение до полного исчерпания всех элементов
    for i in range(10):
        print('Убираем с вершины стека: ', SC_OBJ.pop_out())
        print(SC_OBJ)

    # Снова наполняем стек и убеждаемся, что отработаны ошибки очистки стека (остается рабочим после очистки)
    for i in range(10):
        SC_OBJ.push_in(i)
    print(SC_OBJ)

    # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
    print('Убираем с вершины стека: ', SC_OBJ.pop_out())
    print(SC_OBJ)