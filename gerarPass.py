import random
import string
import pyperclip

def gerarPass(tamanho=12, usar_maiusculas=True, usar_numeros=True, usar_símbolos=True):
    caracteres = string.ascii_lowercase

    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_símbolos:
        caracteres += string.punctuation

    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

