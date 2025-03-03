
from ply import lex, yacc

tokens = (
    'IDENTIFICADOR', 'NUMERO', 'CADENA', 'CARACTER',
    'SUMA', 'RESTA', 'PRODUCTO', 'DIVISION', 'MODULO',
    'ASIGNACION', 'IGUALDAD', 'DIFERENTE', 'MENOR', 'MENOR_IGUAL',
    'MAYOR', 'MAYOR_IGUAL', 'Y_LOGICO', 'O_LOGICO', 'NEGACION',
    'PARENTESIS_IZQ', 'PARENTESIS_DER', 'LLAVE_IZQ', 'LLAVE_DER', 'CORCHETE_IZQ', 'CORCHETE_DER',
    'PUNTO_Y_COMA', 'COMA', 'PUNTO', 'DOS_PUNTOS',
    'INCREMENTO', 'DECREMENTO',
    'SUMA_ASIGNACION', 'RESTA_ASIGNACION', 'PRODUCTO_ASIGNACION', 'DIVISION_ASIGNACION',
    'SI', 'SI_NO', 'MIENTRAS', 'PARA', 'HACER', 'RETORNAR', 'SELECCIONAR', 'CASO',
    'INTERRUMPIR', 'CONTINUAR', 'POR_DEFECTO', 'IR_A', 'TIPO_DEF',
    'ESTRUCTURA', 'UNION', 'ENUMERACION', 'CONSTANTE', 'TAMANIO', 'ESTATICO',
    'VACIO', 'ENTERO', 'FLOTANTE', 'DOBLE'
)


#Expresiones regulares para token

t_SUMA              = r'\+'
t_RESTA             = r'-'
t_MULTIPLICACION    = r'\*'
t_DIVISION          = r'/'
t_MODULO            = r'%'



t_ASIGNACION    = r'='
t_IGUALDAD      = r'=='
t_DIFERENTE     = r'!='
t_MENOR         = r'<'
t_MENOR_IGUAL   = r'<='
t_MAYOR         = r'>'
t_MAYOR_IGUAL   = r'>='




t_Y_LOGICO      = r'&&'
t_O_LOGICO      = r'\|\|'
t_NEGACION      = r'!'



t_PARENTESIS_IZQ  = r'\('
t_PARENTESIS_DER  = r'\)'
t_LLAVE_IZQ     = r'\{'
t_LLAVE_DER     = r'\}'
t_CORCHETE_IZQ  = r'\['
t_CORCHETE_DER  = r'\]'



t_PUNTO_Y_COMA  = r';'
t_COMA          = r','
t_PUNTO         = r'\.'
t_FLECHA        = r'->'
t_DOS_PUNTOS    = r':'


# Palabras clave
reservadas = {
    'if': 'IF', 'else': 'ELSE', 'while': 'WHILE', 'for': 'FOR', 'return': 'RETURN',
    'int': 'INT', 'float': 'FLOAT', 'char': 'CHAR', 'double': 'DOUBLE', 'void': 'VOID',
    'printf': 'PRINTF', 'scanf': 'SCANF'
}


def t_INCLUDE(t):
    r'\#include'
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'IDENTIFICADOR')
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# t_ASIGNACION = r'='
# t_SUMA = r'\+'
# t_RESTA = r'-'
# t_MULT = r'\*'
# t_DIV = r'/'
# t_PAREN_IZQ = r'\('
# t_PAREN_DER = r'\)'
# t_LLAVE_IZQ = r'\{'
# t_LLAVE_DER = r'\}'
# t_PUNTOYCOMA = r';'
# t_COMA = r','
# t_IGUALDAD = r'=='
# t_DIFERENTE = r'!='
# t_AND = r'&&'
# t_OR = r'\|\|'
# t_INCREMENTO = r'\+\+'
# t_DECREMENTO = r'--'

def t_COMENTARIO_SIMPLE(t):
    r'//.*'
    pass  # Ignorar comentarios

def t_COMENTARIO_MULTILINEA(t):
    r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/'
    pass  # Ignorar comentarios multilínea

t_ignore = ' \t'  # Ignorar espacios y tabulaciones

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

# Definición de la gramática (analizador sintáctico)
def p_expresion_asignacion(p):
    'expresion : IDENTIFICADOR ASIGNACION expresion'
    print("Asignación válida")

def p_expresion_binaria(p):
    '''expresion : expresion SUMA expresion
                 | expresion RESTA expresion
                 | expresion MULT expresion
                 | expresion DIV expresion
                 | expresion IGUALDAD expresion
                 | expresion DIFERENTE expresion
                 | expresion AND expresion
                 | expresion OR expresion'''
    print("Operación válida")

def p_expresion_incremento(p):
    '''expresion : IDENTIFICADOR INCREMENTO
                 | IDENTIFICADOR DECREMENTO'''
    print("Incremento/Decremento válido")

def p_expresion_numero(p):
    'expresion : NUMERO'
    print("Número válido")

def p_expresion_identificador(p):
    'expresion : IDENTIFICADOR'
    print("Identificador válido")

# Reglas para estructuras de control
def p_expresion_if(p):
    'expresion : IF PAREN_IZQ expresion PAREN_DER LLAVE_IZQ expresion LLAVE_DER'
    print("Estructura if válida")

def p_expresion_if_else(p):
    'expresion : IF PAREN_IZQ expresion PAREN_DER LLAVE_IZQ expresion LLAVE_DER ELSE LLAVE_IZQ expresion LLAVE_DER'
    print("Estructura if-else válida")

def p_expresion_while(p):
    'expresion : WHILE PAREN_IZQ expresion PAREN_DER LLAVE_IZQ expresion LLAVE_DER'
    print("Estructura while válida")

def p_expresion_for(p):
    'expresion : FOR PAREN_IZQ expresion PUNTOYCOMA expresion PUNTOYCOMA expresion PAREN_DER LLAVE_IZQ expresion LLAVE_DER'
    print("Estructura for válida")

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}', línea {p.lineno}")
    else:
        print("Error de sintaxis")

parser = yacc.yacc()

# Prueba con una cadena de código C-like
data = "int x = 5 + 3;"
lexer.input(data)

print("Tokens:")
while tok := lexer.token():
    print(tok)

print("\nAnálisis Sintáctico:")
parser.parse(data)