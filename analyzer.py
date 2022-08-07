from lark import Lark, UnexpectedInput, GrammarError


class Analyzer:
    def __init__(self, filename='grammar.lark'):
        # проверка существования файла грамматики
        try:
            with open(filename) as reader:
                grammar = reader.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"{filename} is not found!")

        # пытаемся инициализировать парсер с данной грамматикой
        try:
            self.parser = Lark(grammar)
        except GrammarError:
            raise GrammarError("Grammar is incorrect!")

    def analyze(self, query):
        # парсим запрос и возвращаем дерево; если запрос некорректный, то вызовется исключение
        return self.parser.parse(query)

    def check(self, query):
        # пытаемся пропарсить запрос; если поднимается исключение, то в нем какая-то ошибка
        try:
            self.parser.parse(query)
            return True
        except UnexpectedInput:
            return False
