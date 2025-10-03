from homework_2.node import Node

def no_dummy_merge(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    # Определяем голову результирующего списка
    if list1.val <= list2.val:
        head = list1
        list1 = list1.next_
    else:
        head = list2
        list2 = list2.next_

    # Отсоединяем голову от предыдущего узла
    head.prev_ = None

    # Указатель для построения нового списка
    current = head

    # Идем по обоим спискам
    while list1 and list2:
        if list1.val <= list2.val:
            current.next_ = list1
            list1.prev_ = current
            list1 = list1.next_
        else:
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

    return head
