# TODO Найдите количество книг, которое можно разместить на дискете
storage = 1.44
number_of_pages = 100
number_of_lines = 50
number_of_symbols = 25

storage_in_bytes = storage * 1024 * 1024
book_size = number_of_symbols * number_of_lines * number_of_pages * 4
max_books = round(storage_in_bytes / book_size)
print("Количество книг, помещающихся на дискету:", max_books)
