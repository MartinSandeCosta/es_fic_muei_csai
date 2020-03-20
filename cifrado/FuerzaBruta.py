#!/usr/bin/env python
import vigenere

cipherText = "JHLIÑWNACBEPOACPCDDMRKUMDSPITSLIRKAKVACIFWCACA"
dictionary = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
hash = "9ad2ba7c3dfdcb37915dcdf26029d60ce1aa780f743de49f04ade3662e694c34"

def brute(keys):
    """ Para cada password del fichero 'passwords' trata de descifrar el texto cipherText
    usando el dictionary y comprueba si el proceso es correcto. Si coincide el hash calculado
    con el esperado (hash) el programa finaliza.

    :param keys: todas las claves del fichero passwords
    :return: no devuelve ningún valor
    """
    for clave in keys:
        if vigenere.vigenere(cipherText, dictionary, hash, clave.decode('utf-8')): break


def main():
    """Función principal del script de fuerza bruta. Carga los passwords del fichero e inicia el proceso
    de ataque por fuerza bruta

    :return: no devuelve ningún valor
    """
    keys = [palabra.strip() for palabra in open("passwords", "rb").readlines()]
    brute(keys)


if __name__ == '__main__':
    main()
