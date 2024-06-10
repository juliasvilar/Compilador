import ply.lex as lex

# Definindo os tokens
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

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Definindo expressões regulares para tokens
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
    pass  # Comentários são ignorados

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Erro: Caractere não reconhecido '%s'" % t.value[0])
    t.lexer.skip(1)

# Palavras reservadas
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

# Definindo tokens para operadores e símbolos especiais
t_OPERADOR = r'[\+\-\*/=<>!&|]'
t_SIMBOLO_ESP = r'[\(\){};,\[\]]'

# Construindo o lexer
lexer = lex.lex()

# Código de teste
data = '''
int main() {
    printf("Hello, world!");
    return 0;
}
'''

# Alimente o lexer com o código de teste
lexer.input(data)

# Tokenize e imprima os tokens
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
