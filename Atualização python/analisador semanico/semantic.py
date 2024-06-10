variaveis = {}
num_variaveis = 0

funcoes = {}
num_funcoes = 0

def adicionarVariavel(nome, tipo):
    global variaveis, num_variaveis
    variaveis[nome] = tipo
    num_variaveis += 1

def verificarDeclaracaoVariavel(nome):
    return nome in variaveis

def verificarCompatibilidadeTipos(tipo1, tipo2):
    return tipo1 == tipo2

def obterTipoVariavel(nome):
    return variaveis.get(nome, None)

def adicionarFuncao(nome, tipo_retorno, tipos_parametros):
    global funcoes, num_funcoes
    funcoes[nome] = {'tipo_retorno': tipo_retorno, 'tipos_parametros': tipos_parametros}
    num_funcoes += 1

def verificarDeclaracaoFuncao(nome):
    return nome in funcoes
