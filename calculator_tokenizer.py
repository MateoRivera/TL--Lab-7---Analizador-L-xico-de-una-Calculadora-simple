import ply.lex as lex

# Tipos de tokens a manejar
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EXPONENT',
    'LPAREN',
    'RPAREN',
)

# Expresiones regulares para los tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXPONENT = r'\*\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBER = r'(\d+(\.\d*)?|\.\d+)'

# Expresión regular para caracteres ilegales


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Función que dada una cadena de texto, devuelve una lista de tokens


def tokenize(data):
    lexer = lex.lex()
    lexer.input(data)

    return [{"TIPO": tok.type, "TOKEN": tok.value} for tok in lexer]


# Devuelve la instancia del lexer
lexer = lex.lex()
