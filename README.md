# CSAI
Repositorio de código para la asignatura CSAI del MUEI de la FIC

* En la carpeta cifrado podéis encontrar un pequeño ejemplo de código para realizar un ataque de fuerza bruta siguiendo las especificaciones de la práctica de cifrado.

* Para generar diccionarios con combinaciones de 1 a 4 elementos usando el conjunto de letras del castellano y guardarlo en un fichero llamado *passwords*, os recomendaría utilizar `crunch`, herramienta por línea de comandos, de la siguiente manera:

```bash
[usuario@equipo ~]$ crunch 1 4 ABCDEFGHIJKLMNÑOPQRSTUVWXYZ -o passwords
```

* Se trata de un snippet de código muy simple, no pretende ser completo en absoluto pero va a ayudar a calcular los tiempos requeridos para la práctica.

* Permite calcular el tiempo que llevaría realizar un ataque de fuerza bruta para romper un cifrado Vigenere en caso de disponer del hash de la cadena de texto sin cifrar.

El ejemplo del algoritmo de cifrado se realiza con los siguientes datos:

* Cadena en claro: HOLAMENSAJEINICIALDEPRUEBAPARALAPRACTICADECSAI
* Clave: CSAI
* Diccionario: ABCDEFGHIJKLMNÑOPQRSTUVWXYZ
* Texto cifrado: JHLIÑWNACBEPOACPCDDMRKUMDSPITSLIRKAKVACIFWCACA
* Hash (SSHA256): 9ad2ba7c3dfdcb37915dcdf26029d60ce1aa780f743de49f04ade3662e694c34

Para calcular el tiempo que tarda el algoritmo se puede realizar de la siguiente forma:

```bash
[usuario@equipo ~]$ time python3 FuerzaBruta.py
```

La idea es que podáis tomar el esqueleto como ejemplo para resolver la práctica.