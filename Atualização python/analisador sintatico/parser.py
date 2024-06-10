import ply.yacc as yacc
from lexer import tokens

def p_programa(p):
    'programa : declaracoes'
    pass

def p_declaracoes(p):
    '''declaracoes : declaracao
                   | declaracoes declaracao'''
    pass

def p_declaracao(p):
    '''declaracao : declaracao_variavel
                  | declaracao_funcao
                  | comentario'''
    pass

def p_declaracao_variavel(p):
    '''declaracao_variavel : tipo ID ';'
                           | tipo ID '=' expressao ';' '''
    pass

def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | DOUBLE
            | CHAR
            | BOOLEAN'''
    pass

def p_declaracao_funcao(p):
    '''declaracao_funcao : tipo ID '(' parametros ')' bloco'''
    pass

def p_parametros(p):
    '''parametros : parametro
                  | parametros ',' parametro'''
    pass

def p_parametro(p):
    '''parametro : tipo ID'''
    pass

def p_bloco(p):
    'bloco : "{" declaracoes "}"'
    pass

def p_comentario(p):
    'comentario : COMENTARIO'
    pass

def p_expressao(p):
    '''expressao : atribuicao
                 | expressao_logica
                 | expressao_relacional
                 | expressao_aritmetica'''
    pass

def p_atribuicao(p):
    '''atribuicao : ID '=' expressao
                  | ID ADD_ASSIGN expressao
                  | ID SUB_ASSIGN expressao
                  | ID MUL_ASSIGN expressao
                  | ID DIV_ASSIGN expressao
                  | ID MOD_ASSIGN expressao
                  | ID LAND_ASSIGN expressao
                  | ID LOR_ASSIGN expressao'''
    pass

def p_expressao_logica(p):
    '''expressao_logica : expressao_relacional
                        | expressao_logica LAND expressao_relacional
                        | expressao_logica LOR expressao_relacional
                        | LNOT expressao_relacional'''
    pass

def p_expressao_relacional(p):
    '''expressao_relacional : expressao_aritmetica
                            | expressao_aritmetica '>' expressao_aritmetica
                            | expressao_aritmetica GE expressao_aritmetica
                            | expressao_aritmetica '<' expressao_aritmetica
                            | expressao_aritmetica LE expressao_aritmetica
                            | expressao_aritmetica NE expressao_aritmetica
                            | expressao_aritmetica EQ expressao_aritmetica'''
    pass

def p_expressao_aritmetica(p):
    '''expressao_aritmetica : expressao_multiplicativa
                             | expressao_aritmetica '+' expressao_multiplicativa
                             | expressao_aritmetica '-' expressao_multiplicativa'''
    pass

def p_expressao_multiplicativa(p):
    '''expressao_multiplicativa : expressao_unaria
                                  | expressao_multiplicativa '*' expressao_unaria
                                  | expressao_multiplicativa '/' expressao_unaria
                                  | expressao_multiplicativa '%' expressao_unaria'''
    pass

def p_expressao_unaria(p):
    '''expressao_unaria : expressao_postfix
                         | '-' expressao_unaria
                         | INCREMENT expressao_postfix
                         | DECREMENT expressao_postfix'''
    pass

def p_expressao_postfix(p):
    '''expressao_postfix : primaria
                         | primaria '[' expressao ']'
                         | primaria '(' argumentos ')'
                         | primaria '.' ID
                         | primaria ARROW ID'''
    pass

def p_primaria(p):
    '''primaria : ID
                | NUM_INT
                | NUM_DEC
                | TEXTO
                | '(' expressao ')' '''
    pass

def p_argumentos(p):
    '''argumentos : expressoes
                  | '''
    pass

def p_expressoes(p):
    '''expressoes : expressao
                  | expressoes ',' expressao'''
    pass

def p_error(p):
    if p:
        print("Erro de sintaxe na entrada:", p)
    else:
        print("Erro de sintaxe: Fim inesperado do arquivo")

parser = yacc.yacc()

# Teste
data = '''
int main() {
    int a = 5;
    float b = 3.14;
    return 0;
}
'''

parser.parse(data)
