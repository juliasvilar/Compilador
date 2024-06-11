# semantic.py

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

def analisarCodigo(data):
    global variaveis, funcoes
    variaveis = []
    funcoes = []

    linhas = data.split('\n')
    for i, linha in enumerate(linhas):
        if 'int ' in linha or 'float ' in linha:
            partes = linha.split()
            tipo = partes[0]
            nome = partes[1].replace(';', '')
            adicionarVariavel(nome, tipo)
        elif '=' in linha:
            partes = linha.split('=')
            variavel = partes[0].strip()
            valor = partes[1].strip().replace(';', '')

            if not verificarDeclaracaoVariavel(variavel):
                print(f"Erro semântico: variável '{variavel}' não declarada na linha {i+1}")
                return False

            tipo_variavel = obterTipoVariavel(variavel)
            if valor.isdigit():
                tipo_valor = 'int'
            elif valor.replace('.', '', 1).isdigit():
                tipo_valor = 'float'
            else:
                tipo_valor = 'string'

            if not verificarCompatibilidadeTipos(tipo_variavel, tipo_valor):
                print(f"Erro semântico: atribuição de tipo incompatível para a variável '{variavel}' na linha {i+1}")
                return False
        elif 'soma(' in linha:
            parametros = linha[linha.find('(')+1:linha.find(')')].split(',')
            for parametro in parametros:
                if not verificarDeclaracaoVariavel(parametro.strip()):
                    print(f"Erro semântico: variável '{parametro.strip()}' não declarada na linha {i+1}")
                    return False
                tipo_parametro = obterTipoVariavel(parametro.strip())
                if not verificarCompatibilidadeTipos(tipo_parametro, 'int'):
                    print(f"Erro semântico: tipo incompatível para a função 'soma' na linha {i+1}")
                    return False
    return True
