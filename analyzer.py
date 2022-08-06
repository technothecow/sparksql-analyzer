from lark import Lark


class Analyzer:
    def __init__(self, filename='grammar.lark'):
        try:
            with open(filename) as reader:
                grammar = reader.read()
        except FileNotFoundError:
            raise FileNotFoundError("grammar.lark is not found!")

        self.parser = Lark(grammar)

    def analyze(self, text):
        return self.parser.parse(text)
