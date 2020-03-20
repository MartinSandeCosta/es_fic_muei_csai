#!/usr/bin/env python
import hashlib


def mono_alfabeto(initial_letter, dictionary):
    """Devuelve mono_alfabeto que se inicia a partir de la letra inicial

    :param initial_letter: letra a partir de la cual calcular el mono_alfabeto.
    :param dictionary: diccionario utilizado.
    :return: el mono alfabeto
    """
    mono_alfabeto = dictionary[dictionary.index(initial_letter):] + dictionary[:dictionary.index(initial_letter)]
    return mono_alfabeto


def calculahash(cadena):
    """Devuelve el hash SHA256 de una cadena dada como entrada

    :param cadena: texto de entrada para calcular su hash
    :return: el hash calculado con SHA256
    """
    return hashlib.sha256(cadena.encode()).hexdigest()


def vigenere(input_text, dictionary, hash, clave):
    """La implementación del descifrado Vigenere está basada en el código de Bogdanov Bogdan
    Enlace de descarga: https://code.sololearn.com/cUoAwxEFYsL3/#py
    Se trata de una versión simplificada (mayúsculas, símbolo siempre en diccionario, única aparición en diccionario).
    Genera inicialmente una "clave_continua" con tantas copias de la palabra clave como necesite hasta igual la
    longitud del texto a descifrar.

    :param input_text: el texto cifrado
    :param dictionary: el diccionario usado
    :param hash: el hash calculado sobre texto claro
    :param clave: la clave usada para descifrar el texto
    :return: devuelve True en caso de que la clave descifre el texto correctamente
    """
    clave_continua = clave * (len(input_text) // len(clave)) + clave[:len(input_text) % len(clave)]
    res = ''
    i = 1
    for char in clave_continua:
        new = mono_alfabeto(char, dictionary)
        for t in input_text:
            res += dictionary[new.index(t)]
            input_text = input_text[i:]
            break

    hash_resultado = calculahash(res)

    if hash_resultado == hash:
        print(clave + "---> Clave correcta!!")
        return True
    else:
        print(clave + ": Clave incorrecta.")
        return False
