#!/usr/bin/env python
import vigenere
import argparse

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
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i', '--input', type=argparse.FileType(), help='input file')
    argparser.add_argument('-d', '--dictionary', type=argparse.FileType(),
                           help='file with the dictionary to be used')
    argparser.add_argument('--hash', type=argparse.FileType(),
                           help='file with the hash to be used for comparison')
    args = argparser.parse_args()

    cipherText = args.input.read().replace("\n", "")
    dictionary = args.dictionary.read().replace("\n", "")
    hash = args.hash.read().replace("\n", "")

    main()
