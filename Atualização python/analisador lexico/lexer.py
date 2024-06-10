import ply.lex as lex

tokens = (
    'INT', 'FLOAT', 'DOUBLE', 'CHAR', 'BOOLEAN',
    'ID', 'NUM_INT', 'NUM_DEC', 'TEXTO',
    'CONDICIONAL', 'FUNCAO_RECURSIVA', 'RETORNO', 'FUNCAO_PRINCIPAL',
    'PALAVRA_RES', 'BIBLIOTECA', 'OPERADOR', 'SIMBOLO_ESP',
    'VOID', 'IF', 'ELSE', 'WHILE', 'FOR', 'RETURN', 'PRINTF',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'ASSIGN', 'ADD_ASSIGN', 'SUB_ASSIGN', 'MUL_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN',
    'GE', 'LE', 'GT', 'LT', 'EQ', 'NE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET', 'SEMICOLON', 'COMMA'
)

t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUM_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NUM_DEC(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_TEXTO(t):
    r'\"([^\\\"]|\\.)*\"'
    return t

def t_COMENTARIO(t):
    r'\/\/.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Erro: Caractere não reconhecido '%s'" % t.value[0])
    t.lexer.skip(1)

reserved = {
    'void': 'VOID',
    'scanf': 'PALAVRA_RES',
    'printf': 'PRINTF',
    'stdio': 'BIBLIOTECA',
    'string': 'BIBLIOTECA',
    'stdlib': 'BIBLIOTECA',
    'int': 'INT',
    'float': 'FLOAT',
    'double': 'DOUBLE',
    'char': 'CHAR',
    'boolean': 'BOOLEAN',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'return': 'RETURN',
    'main': 'FUNCAO_PRINCIPAL'
}

t_OPERADOR = r'[\+\-\*/=<>!&|]'
t_SIMBOLO_ESP = r'[\(\){};,\[\]]'

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'

t_ASSIGN = r'='
t_ADD_ASSIGN = r'\+='
t_SUB_ASSIGN = r'-='
t_MUL_ASSIGN = r'\*='
t_DIV_ASSIGN = r'/='
t_MOD_ASSIGN = r'%='

t_GE = r'>='
t_LE = r'<='
t_GT = r'>'
t_LT = r'<'
t_EQ = r'=='
t_NE = r'!='

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_COMMA = r','

lexer = lex.lex()

data = '''
int main() {
    printf("Hello, world!");
    return 0;
}
'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
