import ply.lex as lex

tokens = (
    'INT',
    'FLOAT',
    'DOUBLE',
    'CHAR',
    'BOOLEAN',
    'ID',
    'NUM_INT',
    'NUM_DEC',
    'TEXTO',
    'CONDICIONAL',
    'FUNCAO_RECURSIVA',
    'RETORNO',
    'FUNCAO_PRINCIPAL',
    'PALAVRA_RES',
    'BIBLIOTECA',
    'OPERADOR',
    'SIMBOLO_ESP'
)

t_ignore = ' \t\n'

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
    'void': 'PALAVRA_RES',
    'scanf': 'PALAVRA_RES',
    'printf': 'PALAVRA_RES',
    'stdio': 'BIBLIOTECA',
    'string': 'BIBLIOTECA',
    'stdlib': 'BIBLIOTECA',
    'int': 'INT',
    'float': 'FLOAT',
    'double': 'DOUBLE',
    'char': 'CHAR',
    'boolean': 'BOOLEAN',
    'if': 'CONDICIONAL',
    'else': 'CONDICIONAL',
    'for': 'FUNCAO_RECURSIVA',
    'while': 'FUNCAO_RECURSIVA',
    'return': 'RETORNO',
    'main': 'FUNCAO_PRINCIPAL'
}

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
    if tok is None:
        break
    print(tok)
