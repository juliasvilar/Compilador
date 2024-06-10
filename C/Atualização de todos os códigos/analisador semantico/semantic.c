#include "semantic.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

Variavel variaveis[100];
int num_variaveis = 0;

Funcao funcoes[100];
int num_funcoes = 0;

void adicionarVariavel(char* nome, char* tipo) {
    variaveis[num_variaveis].nome = strdup(nome);
    variaveis[num_variaveis].tipo = strdup(tipo);
    num_variaveis++;
}

bool verificarDeclaracaoVariavel(char* nome) {
    for (int i = 0; i < num_variaveis; i++) {
        if (strcmp(variaveis[i].nome, nome) == 0) {
            return true;
        }
    }
    return false;
}

bool verificarCompatibilidadeTipos(char* tipo1, char* tipo2) {
    return strcmp(tipo1, tipo2) == 0;
}

char* obterTipoVariavel(char* nome) {
    for (int i = 0; i < num_variaveis; i++) {
        if (strcmp(variaveis[i].nome, nome) == 0) {
            return variaveis[i].tipo;
        }
    }
    return NULL;
}

void adicionarFuncao(char* nome, char* tipo_retorno, char* tipos_parametros) {
    funcoes[num_funcoes].nome = strdup(nome);
    funcoes[num_funcoes].tipo_retorno = strdup(tipo_retorno);
    funcoes[num_funcoes].tipos_parametros = strdup(tipos_parametros);
    num_funcoes++;
}

bool verificarDeclaracaoFuncao(char* nome) {
    for (int i = 0; i < num_funcoes; i++) {
        if (strcmp(funcoes[i].nome, nome) == 0) {
            return true;
        }
    }
    return false;
}
