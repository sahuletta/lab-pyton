# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first, participants_second, separator = ','):

    first_group = set(participants_first.split(separator))
    second_group = participants_second.split(separator)
    res = list(first_group.intersection(second_group))
    res.sort()
    return res

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
test = find_common_participants(participants_first_group, participants_second_group, separator = '|')
print(test)