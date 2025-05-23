# Biblioteca - Gestió de Llibres i Usuaris amb SQLite3  

Aquest projecte implementa una biblioteca digital que permet gestionar llibres i usuaris fent servir una base de dades SQLite3.  
Permet afegir, eliminar i llistar llibres i usuaris, així com gestionar préstecs i tornades de llibres.

## Funcionalitats  

### Gestió de llibres:
- Afegir, llistar i eliminar llibres.  
- Assignar un llibre en préstec a un usuari.  
- Tornar un llibre a la biblioteca.  

### Gestió d'usuaris:
- Afegir, llistar i eliminar usuaris.  

### Ús de base de dades SQLite3:
- Els llibres i usuaris es guarden a `bbdd.sqlite3`.  
- Les taules es creen automàticament si no existeixen.  
- Es fan consultes SQL per gestionar la informació.  

### Control d'errors:
- Validació de dades amb `try-except`.  
- Control d'errors per a DNIs repetits.  
- Evita introduir dades incorrectes o buides.  

## Instal·lació i ús  
- Utilitzar un repositori GitHub i Visual Studio Code.  
- Executar el programa:  
  ```bash
  python biblioteca.py

### Base de dades SQL

- El programa fa servir una base de dades anomenada bbdd.sqlite3 amb dues taules principals:

Taula usuaris:

dni	nom	cognoms	tipus_usuari
00000000A	Admin	Default	admin
12345678A	Fran	Martínez	lector

Taula llibres:

titol	autor	dni_prestec	data_prestec
Principito	Cesc Molero	12345678A	2025-05-20
Los 7 enanitos	Franc Rosello	12345678A	2025-05-20

### Menú principal
    Quan executes el programa, veuràs aquest menú:

    - Llistar Llibres
    - Introduir Llibres
    - Eliminar Llibres
    - Llistar Usuaris
    - Introduir Usuaris
    - Eliminar Usuaris
    - Prèstec Llibres
    - Tornar Llibres

### Sortir del programa

    Introdueix un número i segueix les instruccions.

    Tecnologies utilitzades
    Python 3

    SQLite3

    Try-Except per control d'errors

    hashlib per xifrar contrasenyes

    re per validació de DNI

### Millores
    Validació millorada del DNI: Implementada una comprovació més estricta amb expressions regulars per assegurar que els DNIs introduïts compleixen el format oficial.
    Control de préstecs: Afegida limitació per nombre màxim de llibres en préstec (màxim 3 per usuari) i control de durada màxima (màxim un mes) per evitar retards.
    Xifrat de contrasenyes: Les contrasenyes dels usuaris es guarden de forma segura amb hashlib, evitant l’emmagatzematge de contrasenyes en text pla.
    Gestió d’errors més robusta: Millora en el maneig d’excepcions per evitar errors inesperats durant les operacions de base de dades i entrada d’usuari.
    Creació automàtica de taules: El sistema crea automàticament les taules de la base de dades si no existeixen, millorant la usabilitat.
    Menú més intuïtiu: Simplificat el menú principal per facilitar la navegació i ús del programa.