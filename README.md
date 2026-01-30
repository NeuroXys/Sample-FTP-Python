<p>
<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.herokuapp.com?font=Bitcount+Single&pause=1000&width=435&lines=Script+de+backup+automatizado+con+subida+por+FTP+y+notificaci%C3%B3n+por+correo" alt="Typing SVG" /></a>
</p>
Este script en Python automatiza el proceso completo de copia de seguridad de un directorio local. Genera un archivo comprimido con fecha y hora, lo sube a un servidor FTP seguro y envía una notificación por correo electrónico al finalizar.

## Funcionamiento general:

* Accede a un directorio local definido por el usuario.

* Crea un archivo comprimido (.zip) con todos los archivos del directorio, usando una marca temporal en el nombre.

* Muestra el contenido y el tamaño de los archivos incluidos en la copia.

* Se conecta a un servidor FTP con TLS y accede a un directorio remoto.

* Comprueba el número de copias existentes en el servidor y elimina la más antigua si se supera un límite (10 archivos).

* Sube la nueva copia de seguridad al servidor FTP.

* Elimina el archivo comprimido local tras la subida.

* Envía un correo electrónico de confirmación indicando que la copia se ha realizado correctamente.

## Casos de uso habituales:

* Backups periódicos de carpetas personales o de trabajo.

* Copias de seguridad en servidores remotos sin intervención manual.

* Entornos domésticos o educativos donde se requiere una solución sencilla y automatizada.

El script integra gestión de archivos, transferencia segura por FTP y notificaciones por correo en un único flujo automatizado.

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
