def merge_dictionaries(dict1, dict2):
    common_trans = set(dict1.trans) & set(dict2.trans)
    merged_dict = Dictionary(dict1.sourcelang, dict2.targetlang, min(dict1.price, dict2.price))
    merged_dict.add_translation(*common_trans)
    return merged_dict


class BookPublisher:
    def __init__(self, name):
        self.name = name
        self.publshbook = []

    def publish(self, *books):
        self.publshbook.extend(books)

    def show_products(self):
        for book in self.publshbook:
            print(book)


class Fiction:
    def __init__(self, title, des, price):
        self.title = title
        self.des = des
        self.price = price

    def __str__(self):
        return f"{self.title} - {self.price}$\n{self.des}"


class Dictionary:
    def __init__(self, sourcelang, targetlang, price):
        self.sourcelang = sourcelang
        self.targetlang = targetlang
        self.price = price
        self.trans = []

    def add_translation(self, *translation_tuples):
        self.trans.extend(translation_tuples)

    def __str__(self):
        res = f"{self.sourcelang} - {self.targetlang} dictionary - {self.price}$\n"
        for translation in self.trans:
            res += f"{translation[0]} - {translation[1]}\n"
        return res


# Sample code
english_hungarian = Dictionary('English', 'Hungarian', 5)
english_hungarian.add_translation(('apple', 'alma'), ('table', 'asztal'), ('dog', 'kutya'))

english_russian = Dictionary('English', 'Russian', 8)
english_russian.add_translation(('apple', 'яблоко'), ('table', 'стол'), ('cat', 'кошка'))

hungarian_russian = merge_dictionaries(english_hungarian, english_russian)

fiction = Fiction('Nineteen Eighty-Four', 'A science fiction novel by English novelist George Orwell', 10)

golden_books = BookPublisher('Golden Books')
golden_books.publish(english_hungarian, english_russian, hungarian_russian, fiction)
golden_books.show_products()
