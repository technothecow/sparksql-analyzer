from lark import Lark,UnexpectedInput


class Analyzer:
    def __init__(self, filename='grammar.lark'):
        try:
            with open(filename) as reader:
                grammar = reader.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"{filename} is not found!")

        self.parser = Lark(grammar)

    def analyze(self, query):
        return self.parser.parse(query)

    def check(self, query):
        try:
            self.parser.parse(query)
            return True
        except UnexpectedInput:
            return False
