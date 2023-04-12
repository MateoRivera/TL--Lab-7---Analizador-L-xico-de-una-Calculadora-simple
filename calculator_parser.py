import ply.yacc as yacc
from calculator_tokenizer import tokens, lexer


precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'EXPONENT'),
    ('right', 'UMINUS'),
)


def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = p[1] - p[3]


def p_expression_times(p):
    'expression : expression TIMES expression'
    p[0] = p[1] * p[3]


def p_expression_divide(p):
    'expression : expression DIVIDE expression'
    try:
        p[0] = p[1] / p[3]
    except ZeroDivisionError:
        print("¡División entre cero!")
        p[0] = float('nan')


def p_expression_exponent(p):
    'expression : expression EXPONENT expression'
    p[0] = p[1] ** p[3]


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = float(p[1])


def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]


def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)


def solve(expression):
    parser = yacc.yacc()
    result = parser.parse(expression, lexer=lexer)
    return result
