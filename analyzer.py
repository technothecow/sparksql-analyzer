from lark import Lark

grammar = None

try:
    with open('grammar.lark') as reader:
        grammar = reader.read()
except FileNotFoundError:
    raise FileNotFoundError("grammar.lark is not found!")

parser = Lark(grammar)


def analyze(text):
    return parser.parse(text)
