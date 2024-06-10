%option noyywrap

DIGITO       [0-9]
LETRA        [a-zA-Z]
ID           [a-zA-Z_][a-zA-Z0-9_]*
NUM_INT      [0-9]+
NUM_DEC      [0-9]+\.[0-9]+
TEXTO        \"[^\"]*\"
COMENTARIO   \/\/.*
OPERADOR     [=+\-*/%&|!><]=?|\|\||&&|!=|>|>=|<|<=
SIMBOLO_ESP  [\(\)\[\]\{\},;#!?:.]
ESPACO       [ \t]

%%

void|scanf|printf { printf("PALAVRA_RES: %s\n", yytext); }
stdio|string|stdlib { printf("BIBLIOTECA: %s\n", yytext); }
int|float|char|boolean { printf("TIPO DE VARIAVEL: %s\n", yytext); }
if|else { printf("CONDICIONAL: %s\n", yytext); }
for|while { printf("FUNCAO RECURSIVA: %s\n", yytext); }
return  { printf("RETORNO: %s\n", yytext); }
main { printf("FUNCAO PRINCIPAL: %s\n", yytext); }

{ESPACO}     { /* Ignorar espaços e tabulações */ }
{NUM_INT}    { printf("NUM_INT: %s\n", yytext); }
{NUM_DEC}    { printf("NUM_DEC: %s\n", yytext); }
{ID}         { printf("ID: %s\n", yytext); }
{TEXTO}      { printf("TEXTO: %s\n", yytext); }
{OPERADOR}   { printf("OPERADOR: %s\n", yytext); }
{SIMBOLO_ESP} { printf("SIMBOLO_ESP: %s\n", yytext); }
{COMENTARIO} { /* Ignorar comentários */ }
.            { printf("Erro: Caractere não reconhecido: %s\n", yytext); }

%%

int main() {
    yylex();
    return 0;
}
