from homework_2.node import Node

def dummy_merge(list1, list2):
    # Создаем фиктивный узел как начало результирующего списка
    dummy = Node(-1)
    current = dummy

    # Идем по обоим спискам одновременно
    while list1 and list2:
        if list1.val <= list2.val:
            # Подключаем узел из list1
            current.next_ = list1
            list1.prev_ = current
            list1 = list1.next_
        else:
            # Подключаем узел из list2
            current.next_ = list2
            list2.prev_ = current
            list2 = list2.next_
        current = current.next_

    # Если один из списков закончился, присоединяем остаток другого
    if list1:
        current.next_ = list1
        list1.prev_ = current
    elif list2:
        current.next_ = list2
        list2.prev_ = current

    # Результат начинается с узла после dummy
    result = dummy.next_
    if result:
        result.prev_ = None  # Убираем связь с dummy узлом

    return result
