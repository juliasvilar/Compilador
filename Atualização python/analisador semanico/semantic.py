class Variavel:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

variaveis = []

class Funcao:
    def __init__(self, nome, tipo_retorno, tipos_parametros):
        self.nome = nome
        self.tipo_retorno = tipo_retorno
        self.tipos_parametros = tipos_parametros

funcoes = []

def adicionarVariavel(nome, tipo):
    global variaveis
    variaveis.append(Variavel(nome, tipo))

def verificarDeclaracaoVariavel(nome):
    for variavel in variaveis:
        if variavel.nome == nome:
            return True
    return False

def verificarCompatibilidadeTipos(tipo1, tipo2):
    tipos_numericos = ["int", "float"]

    # Verificação para operações aritméticas
    if tipo1 in tipos_numericos and tipo2 in tipos_numericos:
        return True

    # Verificação para operações lógicas
    if tipo1 == "boolean" and tipo2 == "boolean":
        return True

    return False

def obterTipoVariavel(nome):
    for variavel in variaveis:
        if variavel.nome == nome:
            return variavel.tipo
    return None

def adicionarFuncao(nome, tipo_retorno, tipos_parametros):
    global funcoes
    funcoes.append(Funcao(nome, tipo_retorno, tipos_parametros))

def verificarDeclaracaoFuncao(nome):
    for funcao in funcoes:
        if funcao.nome == nome:
            return True
    return False

def verificarTiposParametros(nome_funcao, tipos_argumentos):
    for funcao in funcoes:
        if funcao.nome == nome_funcao:
            if len(funcao.tipos_parametros) != len(tipos_argumentos):
                return False
            for tipo_parametro, tipo_argumento in zip(funcao.tipos_parametros, tipos_argumentos):
                if tipo_parametro != tipo_argumento:
                    return False
            return True
    return False

def obterTipoRetorno(nome_funcao):
    for funcao in funcoes:
        if funcao.nome == nome_funcao:
            return funcao.tipo_retorno
    return None
