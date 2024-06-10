import lexer
import parser
import semantic

def test_lexer():
    data = '''
    int main() {
        printf("Hello, world!");
        return 0;
    }
    '''

    lexer.lexer.input(data)

    while True:
        tok = lexer.lexer.token()
        if tok is None:
            break
        print(tok)

def test_parser():
    data = '''
    int main() {
        printf("Hello, world!");
        return 0;
    }
    '''

    parser.parser.parse(data)

def test_semantic_analyzer():
    semantic.adicionarVariavel("x", "int")
    semantic.adicionarVariavel("y", "float")
    semantic.adicionarVariavel("z", "boolean")

    print("\nVariáveis:")
    for var in semantic.variaveis:
        print(f"Nome: {var.nome}, Tipo: {var.tipo}")

    semantic.adicionarFuncao("soma", "int", ["int", "int"])
    semantic.adicionarFuncao("media", "float", ["float", "float"])

    print("\nFunções:")
    for func in semantic.funcoes:
        print(f"Nome: {func.nome}, Tipo de Retorno: {func.tipo_retorno}, Tipos de Parâmetros: {func.tipos_parametros}")

    print("\nVerificando declarações de variáveis:")
    print("Existe a variável 'x'?", semantic.verificarDeclaracaoVariavel("x"))
    print("Existe a variável 'w'?", semantic.verificarDeclaracaoVariavel("w"))

    print("\nVerificando compatibilidade de tipos:")
    print("int e float são compatíveis?", semantic.verificarCompatibilidadeTipos("int", "float"))
    print("boolean e float são compatíveis?", semantic.verificarCompatibilidadeTipos("boolean", "float"))

    print("\nVerificando o tipo de uma variável:")
    print("Tipo da variável 'y':", semantic.obterTipoVariavel("y"))
    print("Tipo da variável 'w':", semantic.obterTipoVariavel("w"))
    
    print("\nVerificando declarações de funções:")
    print("Existe a função 'soma'?", semantic.verificarDeclaracaoFuncao("soma"))
    print("Existe a função 'produto'?", semantic.verificarDeclaracaoFuncao("produto"))

    print("\nVerificando tipos de parâmetros de funções:")
    print("Tipos de parâmetros da função 'soma' são compatíveis com [int, int]?", semantic.verificarTiposParametros("soma", ["int", "int"]))
    print("Tipos de parâmetros da função 'media' são compatíveis com [int, int]?", semantic.verificarTiposParametros("media", ["int", "int"]))

    print("\nVerificando tipo de retorno de funções:")
    print("Tipo de retorno da função 'soma':", semantic.obterTipoRetorno("soma"))
    print("Tipo de retorno da função 'produto':", semantic.obterTipoRetorno("produto"))

if __name__ == "__main__":
    print("Testando o analisador léxico:")
    test_lexer()

    print("\nTestando o analisador sintático:")
    test_parser()

    print("\nTestando o analisador semântico:")
    test_semantic_analyzer()
