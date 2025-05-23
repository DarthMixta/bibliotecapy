from Biblioteca import Biblioteca
from UsuariRegistrat import UsuariRegistrat
from Llibre import Llibre

class Menu:
    def __init__(self, biblioteca: Biblioteca, usuari: UsuariRegistrat):
        self.biblioteca = biblioteca
        self.usuari = usuari

    def mostrar_menu(self):
        raise NotImplementedError("Aquest mètode no està implementat.")

    def executar_opcio(self, opcio):
        raise NotImplementedError("Aquest mètode no està implementat.")

    def run(self):
        while True:
            self.mostrar_menu()
            opcio = input("Selecciona una opció: ")
            if opcio == "0":
                print("Sortint... Adéu!")
                break
            self.executar_opcio(opcio)

class MainMenu(Menu):
    def mostrar_menu(self):
        print("\n--- MENÚ BIBLIOTECA (ADMIN) ---")
        print("1. Afegir usuari")
        print("2. Actualitzar usuari")
        print("3. Eliminar usuari")
        print("4. Mostrar usuaris")
        print("5. Afegir llibre")
        print("6. Actualitzar llibre")
        print("7. Eliminar llibre")
        print("8. Mostrar llibres")
        print("9. Prestar llibre")
        print("10. Tornar llibre")
        print("0. Sortir")
    
    def executar_opcio(self, opcio):
        if opcio == "1":
            nou = UsuariRegistrat()
            nou.introduir_dades()
            nou.set_contrasenya()
            if self.biblioteca.afegir_usuari(nou):
                print("Usuari afegit.")
        elif opcio == "2":
            dni = input("DNI de l'usuari a actualitzar: ")
            nom = input("Nou nom: ")
            cognoms = input("Nous cognoms: ")
            print(self.biblioteca.actualitzar_usuari(dni, nom, cognoms))
        elif opcio == "3":
            dni = input("DNI de l’usuari a eliminar: ")
            print(self.biblioteca.eliminar_usuari(dni))
        elif opcio == "4":
            self.biblioteca.imprimir_usuaris()
        elif opcio == "5":
            llibre = Llibre()
            llibre.introduir_dades()
            print(self.biblioteca.afegir_llibre(llibre))
        elif opcio == "6":
            titol_actual = input("Títol actual del llibre: ")
            nou_titol = input("Nou títol: ")
            nou_autor = input("Nou autor: ")
            print(self.biblioteca.actualitzar_llibre(titol_actual, nou_titol, nou_autor))
        elif opcio == "7":
            titol = input("Títol del llibre a eliminar: ")
            print(self.biblioteca.eliminar_llibre(titol))
        elif opcio == "8":
            print(self.biblioteca.imprimir_llibres())
        elif opcio == "9":
            titol = input("Títol del llibre: ")
            dni = input("DNI del lector: ")
            print(self.biblioteca.prestar_llibre(titol, dni))
        elif opcio == "10":
            titol = input("Títol del llibre: ")
            print(self.biblioteca.tornar_llibre(titol))
        else:
            print("Opció no vàlida.")

class MenuLector(Menu):
    def mostrar_menu(self):
        print("\n--- MENÚ LECTOR ---")
        print("1. Llistar llibres")
        print("2. Prestar llibre")
        print("3. Tornar llibre")
        print("0. Sortir")

    def executar_opcio(self, opcio):
        if opcio == "1":
            print(self.biblioteca.imprimir_llibres())
        elif opcio == "2":
            titol = input("Títol del llibre: ")
            print(self.biblioteca.prestar_llibre(titol, self.usuari.dni))
        elif opcio == "3":
            titol = input("Títol del llibre: ")
            print(self.biblioteca.tornar_llibre(titol))
        else:
            print("Opció no vàlida.")

if __name__ == "__main__":
    biblioteca = Biblioteca()

    tipus = input("Ets administrador (a) o lector (l)? ").strip().lower()

    if tipus == "a":
        usuari_admin = UsuariRegistrat()
        menu = MainMenu(biblioteca, usuari_admin)
    else:
        usuari_lector = UsuariRegistrat()
        usuari_lector.dni = input("Introdueix el teu DNI: ")
        menu = MenuLector(biblioteca, usuari_lector)

    menu.run()
