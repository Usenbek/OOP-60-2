class Book:
    def __init__(self, title, author, pages, format):
        self.title = str(title)
        self.author = str(author)
        self.pages = int(pages)
        self.format = format
    def __str__(self): #выводим информацию про книгу
        return f"{self.title} {self.author} {self.pages}"
    def __len__(self): #кол-во страниц книги
        return self.pages
    def __eq__(self, other): #сравниваем страницы книги
        if self.pages == other.pages:
            return True
        else:
            return False
    def __add__(self, other): #суммируем кол-во страниц книг
        return self.pages + other.pages
    def __getitem__(self, item): # достаем главу из книги
        return f"Chapter {item}: Contents of the book '{self.title}'"

    @classmethod #обращаемся к классу и создаем как по его работе свою конструкцию
    def from_string(cls, s):
        new_attrs = s.split(",")
        new_book = cls(title=new_attrs[0], author=new_attrs[1], pages=new_attrs[2], format=new_attrs[3])
        return new_book

    @staticmethod #проверяем тонкость и кол-во страниц книги
    def is_thick(pages):
        if pages < 500:
            return False
        else:
            return True



book1 = Book("Crime and punishment", "Dostoevsky",574,"paper")
s = "also sparch Zarathustra, Nietzsche,574,paper"
book = Book.from_string(s)
print(book1)
print(book1[3])
print(Book.is_thick(500))
print(book1)
print(len(book1))
print(book1 + book)
print(book1 == book)
print(book1[5])
print(Book.is_thick(600))
print(Book.is_thick(300))

# class Book:
#     def __init__(self, title, author, pages, format = None):
#         self.title = str(title)
#         self.author = str(author)
#         self.pages = int(pages)
#         self.format = format

    # @classmethod
    # def from_string(cls,s):
    #     new_attrs = s.split(",")
    #     new_book =  cls(title=new_attrs[0], author=new_attrs[1], pages=new_attrs[2])
    #     return new_book
    # @staticmethod
    # def is_thick(pages):
    #     if pages < 500:
    #         return False
    #     else:
    #         return True

# s = "Мастер и Маргарита, М. Булгаков, 480"
# book = Book.from_string(s)
# print(Book.is_thick(480))
#
# book_2 = Book(title='usem', author="usen", pages=500)
# print(book_2.pages)
