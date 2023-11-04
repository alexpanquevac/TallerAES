# AES S-Box de 16x16
from operator import xor
from tkinter import W


#Polinomio irreductible para mi grupo
#x8 + x6 + x5 + x3 + 1 

def galois_multiplication(a, b):
    p = 0
    hi_bit_set = 0
    for i in range(8):
        if b & 1 == 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set == 0x80:
            a ^= 0x11b
        b >>= 1
    return p % 256

def galois_inverse(num):
    if num == 0:
        return 0
    for ext in range(256):
        if galois_multiplication(num, ext) == 1:
            return ext
    return 0

def sbox_transformation(byte):
    c = 0x63
    s_box_byte = byte
    for _ in range(4):
        s_box_byte = ((s_box_byte << 1) & 0xFF) | (s_box_byte >> 7)
        byte ^= s_box_byte
    return (byte ^ c) & 0xFF

def generate_sbox():
    sbox = []
    for byte in range(256):
        inverted = galois_inverse(byte)
        sbox.append(sbox_transformation(inverted))
    return sbox

S_BOX = generate_sbox()
for i in range(16):
    for j in range(16):
        print(hex(S_BOX[i*16 + j]), end=" ")
    print()

print("\n")

def generate_inverse_sbox(sbox):
    inverse_sbox = [0] * 256
    for i, value in enumerate(sbox):
        inverse_sbox[value] = i
    return inverse_sbox

S_BOX_INVERSE = generate_inverse_sbox(S_BOX)
for i in range(16):
    for j in range(16):
        print(hex(S_BOX_INVERSE[i*16 + j]), end=" ")
    print()

S_BOX_AUX = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
]

CLAVE = [0x48, 0x6F, 0x6E,0x61,0x31,0x32,0x33,0x09,0x09,0x09,0x09,0x09,0x09,0x09,0x09,0x09]

R_CON = [
    [0x01, 0x00, 0x00, 0x00],
    [0x10, 0x00, 0x00, 0x00],
    [0x00, 0x01, 0x00, 0x00],
    [0x08, 0x10, 0x00, 0x00],
    [0x00, 0x00, 0x01, 0x00],
    [0x00, 0x00, 0x10, 0x00],
    [0x00, 0x00, 0x00, 0x01],
    [0x00, 0x00, 0x00, 0x10],
    [0x11, 0x10, 0x01, 0x00],
    [0x10, 0x01, 0x11, 0x00],
]

MixColumnsMatrix = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02],
]

matrizEjemplo = [
    [0xEA, 0x04, 0x65, 0x85],
    [0x83, 0x45, 0x5D, 0x96],
    [0x5C, 0x33, 0x98, 0xB0],
    [0xF0, 0x2D, 0xAD, 0xC5]
]

mensajeEjemplo = [
    [0xA1, 0x48, 0x6F, 0x6C],
    [0x61, 0x20, 0x4D, 0x75],
    [0x6E, 0x64, 0x6F, 0x21],
    [0x04, 0x04, 0x04, 0x04]
]

matrizOtra = [
    [0x87, 0xf2, 0x4d, 0x97],
    [0x6e, 0x4c, 0x90, 0xec],
    [0x46, 0xe7, 0x4a, 0xc3],
    [0xa6, 0x8c, 0xd8, 0x95]
]

mensajes = [
    [
        [0x48, 0x6F, 0x6C, 0x61],  # "Hola"
        [0x63, 0x6F, 0x6D, 0x6F],  # "como"
        [0x65, 0x73, 0x74, 0x61],  # "esta"
        [0x3F, 0x20, 0x20, 0x20]   # "?   "
    ],
    [
        [0x41, 0x64, 0x69, 0xF3],  # "Adió"
        [0x73, 0x20, 0x20, 0x20],  # "s   "
        [0x61, 0x20, 0x74, 0x6F],  # "a to"
        [0x64, 0x6F, 0x73, 0x20]   # "dos "
    ],
    [
        [0x42, 0x69, 0x65, 0x6E],  # "Bien"
        [0x76, 0x65, 0x6E, 0x69],  # "veni"
        [0x64, 0x6F, 0x73, 0x21],  # "dos!"
        [0x20, 0x20, 0x20, 0x20]   # "    "
    ],
    [
        [0x4F, 0x6C, 0x61, 0x21],  # "Ola!"
        [0x20, 0x45, 0x73, 0x74],  # " Es"
        [0x6F, 0x20, 0x65, 0x73],  # "o es"
        [0x75, 0x6E, 0x61, 0x20]   # "una "
    ],
    [
        [0x4D, 0x61, 0x74, 0x72],  # "Matr"
        [0x69, 0x7A, 0x20, 0x34],  # "iz 4"
        [0x78, 0x34, 0x20, 0x20],  # "x4  "
        [0x20, 0x20, 0x20, 0x20]   # "    "
    ]
]

arregloClaves = [
    [0x48, 0x6F, 0x6C, 0x6C, 0x6F, 0x20, 0x57, 0x6F, 0x72, 0x6C, 0x64, 0x20, 0x54, 0x68, 0x65, 0x72],  # "Hello World There"
    [0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F, 0x50],  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    [0x21, 0x24, 0x25, 0x26, 0x2A, 0x40, 0x5E, 0x7C, 0x7E, 0x3F, 0x21, 0x24, 0x25, 0x26, 0x2A, 0x40],  # "!$%&@^|~?!$%&@"
    [0x57, 0x68, 0x61, 0x74, 0x27, 0x73, 0x20, 0x66, 0x6F, 0x75, 0x72, 0x20, 0x34, 0x78, 0x34, 0x20],  # "What's four 4x4 "
    [0x4D, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x20, 0x35, 0x20, 0x4D, 0x65, 0x6E, 0x75, 0x20, 0x54]   # "Message 5 Menu T"
]



def transpose_matrix(matrix):
    num_filas = len(matrix)
    num_columnas = len(matrix[0]) if matrix else 0
    transpuesta = [[0 for _ in range(num_filas)] for _ in range(num_columnas)]
    for i in range(num_filas):
        for j in range(num_columnas):
            transpuesta[j][i] = matrix[i][j]

    return transpuesta
  

RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

def sub_byte(byte, BOX):
    return BOX[byte]


def obtenerWsIniciales(CLAVE):
    W0 = [CLAVE[0], CLAVE[1], CLAVE[2], CLAVE[3]]
    W1 = [CLAVE[4], CLAVE[5], CLAVE[6], CLAVE[7]]
    W2 = [CLAVE[8], CLAVE[9], CLAVE[10], CLAVE[11]]
    W3 = [CLAVE[12], CLAVE[13], CLAVE[14], CLAVE[15]]
    sk0 = [W0,W1,W2,W3]
    return sk0


   
#Metodo que realiza xor de dos matrices   
def xorSk(w,w0):
    nuevoW = []
    for i in range(4):
        nuevoW.append((w[i] ^ w0[i]))
    return nuevoW    

#Obtiene la subclave apartir de la matriz anterior y la constante Sub i
def obtenerSubclave(wS,rcon,BOX):
    w = wS[3]
    fila = [w[0], w[1], w[2], w[3]]
    elemento_rotado = fila.pop()  # Elimina el último elemento
    fila.insert(0, elemento_rotado)
    
    #Se pasa por caja S
    Wis = []
    for elemento in fila:
        valor = sub_byte(elemento, BOX)
        Wis.append(valor)

    #Se realiza xor con Rcon[i]
    WsActual = []
    WsActual = xorSk(Wis,rcon)
    WsActual = xorSk(wS[0],WsActual)
    SKi = []
    SKi.append(WsActual)
    #Se realiza xor con las Ws anteriores
    for i in range(3):
        WsActual = xorSk(sk0[i+1], WsActual)
        SKi.append(WsActual)
    return SKi    

#Genera la subclaves para las 10 mrondas
def generarSubclaves(SUBCLAVES, sk0,BOX):
    for i in range(10):
        ski = obtenerSubclave(sk0,R_CON[i],BOX)
        sk0 = []
        sk0 = ski
        SUBCLAVES.append(transpose_matrix(ski))
    return SUBCLAVES  
    

#Mostramos las SubClaves en pantalla
def mostrarSubClaves(SUBCLAVES) :
    print("SUB-Claves")
    indice = 0
    for i in SUBCLAVES:
        print("Sk-",indice)
        indice+=1
        matriz = []
        for elemento in i:
            fila = []
            for j in elemento:
                fila.append(hex(j))
            print(fila)
               

#metodo de addroundkey
def AddRoundKey(Matriz, Subclave):
  resultado = []
  for i in range(4):
      fila = []
      for j in range(4):
          fila.append(Matriz[i][j]^Subclave[i][j])  
      resultado.append(fila)    
  return resultado

#metodo de subbytes
def subByteRound(matriz,BOX):
    resultado = []
    for elemento in matriz:
        fila = []
        for i in elemento:
            fila.append(sub_byte(i,BOX))
        resultado.append(fila)  
    return resultado 

#metodo de  shiftRow
def shiftRow(matriz):
    matriz[1] = matriz[1][1:] + matriz[1][:1]
    matriz[2] = matriz[2][2:] + matriz[2][:2]
    matriz[3] = matriz[3][3:] + matriz[3][:3]

    return matriz

#metodo de  shiftRow inverso
def shiftRowInverse(matriz):
    matriz[1] = matriz[1][-1] + matriz[1][:-1]
    matriz[2] = matriz[2][-2:] + matriz[2][:-2]
    matriz[3] = matriz[3][-3:] + matriz[3][:-3]

    return matriz

#Metodo de mixcolum
def galois_mul(a, b, polinomio):
        p = 0
        for _ in range(8):
            if b & 1:
                p ^= a
            high_bit_set = a & 0x80
            a <<= 1
            if high_bit_set:
                a ^= polinomio
            b >>= 1
        return p

#Metodo de mixcolums
def mixColumns(mix_matrix, state, polinomio):
    for col in range(4):
        s0, s1, s2, s3 = state[0][col], state[1][col], state[2][col], state[3][col]
        state[0][col] = galois_mul(mix_matrix[0][0], s0,polinomio) ^ galois_mul(mix_matrix[0][1], s1,polinomio) ^ galois_mul(mix_matrix[0][2], s2,polinomio) ^ galois_mul(mix_matrix[0][3], s3,polinomio)
        state[1][col] = galois_mul(mix_matrix[1][0], s0,polinomio) ^ galois_mul(mix_matrix[1][1], s1,polinomio) ^ galois_mul(mix_matrix[1][2], s2,polinomio) ^ galois_mul(mix_matrix[1][3], s3,polinomio)
        state[2][col] = galois_mul(mix_matrix[2][0], s0,polinomio) ^ galois_mul(mix_matrix[2][1], s1,polinomio) ^ galois_mul(mix_matrix[2][2], s2,polinomio) ^ galois_mul(mix_matrix[2][3], s3,polinomio)
        state[3][col] = galois_mul(mix_matrix[3][0], s0,polinomio) ^ galois_mul(mix_matrix[3][1], s1,polinomio) ^ galois_mul(mix_matrix[3][2], s2,polinomio) ^ galois_mul(mix_matrix[3][3], s3,polinomio)

    return state

def imprimir(matriz):
    for elemento in matriz:
        fila = []
        for i in elemento:
            fila.append(hex(i))
        print(fila)  

print("  ")
print("  ")
#Metodo que encripta un mensaje
def encriptar(mensajeEjemplo, polinomio, SUBCLAVES,BOX):
    #ronda 0
    resultado = []
    print("  ")
    print("Ronda 0")
    resultado = AddRoundKey(mensajeEjemplo, SUBCLAVES[0])
    imprimir(resultado)

    for i in range(8):
              indice = i + 1
              print("  ")
              print("Ronda",indice)
              resultado = subByteRound(resultado,BOX)
              print("Sub-Byte",indice)
              imprimir(resultado)
              resultado = shiftRow(resultado)
              print("Shift-Row",indice)
              imprimir(resultado)
              resultado = mixColumns(MixColumnsMatrix,resultado,polinomio)
              print("Mix-Columns",indice)
              imprimir(resultado)

              print("RoundKey",indice)
              resultado = AddRoundKey(mensajeEjemplo, SUBCLAVES[i+1])
              imprimir(resultado)
    print("Ronda 10")              
    resultado = subByteRound(resultado,S_BOX)
    print("Sub-Byte 10")
    imprimir(resultado)
    resultado = shiftRow(resultado)
    print("Shift-Row 10")
    imprimir(resultado)
    print("RoundKey 10")
    resultado = AddRoundKey(mensajeEjemplo, SUBCLAVES[10])
    imprimir(resultado)      

#Metodo que desencripta un mensaje
def desencriptar(mensajeEjemplo, polinomio, SUBCLAVES,BOX):
    resultado = []
    print("  ")
    print("Ronda 0")
    resultado = AddRoundKey(mensajeEjemplo, SUBCLAVES[10])
    imprimir(resultado)
    for i in range(8, -1, -1):
        indice = 0
        indice += 1
        print("  ")
        print("Ronda",indice)
        resultado = shiftRowInverse(resultado)
        print("Shift-Row",indice)
        imprimir(resultado)
        resultado = subByteRound(resultado,BOX)
        print("Sub-Byte",indice)
        imprimir(resultado)
        print("RoundKey",indice)
        resultado = AddRoundKey(resultado, SUBCLAVES[i])
        imprimir(resultado)
        resultado = mixColumns(MixColumnsMatrix,resultado,polinomio)
        print("Mix-Columns",indice)
        imprimir(resultado)
    resultado = shiftRowInverse(resultado)
    print("Shift-Row",indice)
    imprimir(resultado)
    resultado = subByteRound(resultado,BOX)
    print("Sub-Byte",indice)
    imprimir(resultado)
    print("RoundKey",indice)
    resultado = AddRoundKey(resultado, SUBCLAVES[i])
    imprimir(resultado)


def texto_a_matriz(texto):
    # Convierte el mensaje en una cadena hexadecimal sin el prefijo '0x'
    mensaje_hex = ''.join(['{:02x}'.format(ord(caracter)) for caracter in texto])
    
    # Calcula la cantidad de relleno necesario para que sea una matriz 4x4
    cantidad_relleno = 16 - (len(mensaje_hex) % 16)
    
    # Agrega los ceros de relleno
    mensaje_hex += '00' * (cantidad_relleno // 2)
    
    # Divide la cadena hexadecimal en una matriz 4x4
    matriz = [mensaje_hex[i:i+8] for i in range(0, len(mensaje_hex), 8)]
    
    # Formatea cada elemento de la matriz como '0xXX'
    matriz = [['0x' + matriz[i][0:2], '0x' + matriz[i][2:4], '0x' + matriz[i][4:6], '0x' + matriz[i][6:8]] for i in range(4)]
    
    return matriz

# Solicita un mensaje al usuario
mensaje = input("El mensaje: ")

# Convierte el mensaje en una matriz 4x4
matriz_resultante = texto_a_matriz(mensaje)

# Imprime la matriz resultante
for fila in matriz_resultante:
    print(fila)


sk0 = obtenerWsIniciales(CLAVE)
SUBCLAVES = []
SUBCLAVES.append(transpose_matrix(sk0))

SUBCLAVES = generarSubclaves(SUBCLAVES, sk0,S_BOX)
mostrarSubClaves(SUBCLAVES)
encriptar(mensajeEjemplo,0x11B,SUBCLAVES,S_BOX) 



""" print(" ")
print(" ")
print("Encripción utilizando nuestro polinomio")
encriptar(mensajeEjemplo,0x1B3, SUBCLAVES,S_BOX)

print(" ")
print(" ")
print("Usando diferentes claves y mensajes")
#Diferentes mensajes
sk0 = obtenerWsIniciales(arregloClaves[0])
SUBCLAVES = []
SUBCLAVES.append(transpose_matrix(sk0))

SUBCLAVES = generarSubclaves(SUBCLAVES, sk0,S_BOX)
mostrarSubClaves(SUBCLAVES)
for i in range(5):
    print(" ")
    print(" ")
    print("Mensaje ",i+1)
    encriptar(mensajes[i],0x11B,SUBCLAVES,S_BOX) 

print(" ")
print(" ")
#Diferentes claves
for i in range(5):
    sk0 = obtenerWsIniciales(arregloClaves[i])
    SUBCLAVES = []
    SUBCLAVES.append(transpose_matrix(sk0))

    SUBCLAVES = generarSubclaves(SUBCLAVES, sk0,S_BOX)
    mostrarSubClaves(SUBCLAVES)
    encriptar(mensajes[2],0x11B,SUBCLAVES,S_BOX) 


#Desencriptar
sk0 = obtenerWsIniciales(CLAVE)
SUBCLAVES = []
SUBCLAVES.append(transpose_matrix(sk0))

SUBCLAVES = generarSubclaves(SUBCLAVES, sk0,S_BOX_INVERSE)
mostrarSubClaves(SUBCLAVES) """