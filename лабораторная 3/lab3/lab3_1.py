# TODO Напишите функцию для поиска индекса товара
def find_index(goods_list:list, search_item):
    if search_item in goods_list:
        return goods_list.index(search_item)
    else:
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# print(find_index(items_list, 'аdfd'))
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
