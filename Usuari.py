import hashlib
import getpass

class Usuari:

    def __init__(self, nom: str = "None", cognoms: str = "None", dni: str = "None"):
        self.nom = nom
        self.cognoms = cognoms
        self.dni = dni

    def imprimir_dades(self) -> str:
        return f"Nom: {self.nom}, Cognoms: {self.cognoms}, DNI: {self.dni}"

    def introduir_dades(self):
        self.nom = input("Introdueix el nom: ")
        self.cognoms = input("Introdueix els cognoms: ")
        self.dni = input("Introdueix el DNI: ")

class UsuariRegistrat(Usuari):
    
    def __init__(self, nom: str = "None", cognoms: str = "None", dni: str = "None", tipus_usuari: str = "lector"):
        super().__init__(nom, cognoms, dni)
        if tipus_usuari.lower() in ["lector", "admin"]:
            self.tipus_usuari = tipus_usuari.lower()
        else:
            self.tipus_usuari = "lector"
        self._contrasenya = None

    def encriptar_contrasenya(self, password: str) -> str:
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def set_contrasenya(self):
        password = getpass.getpass("Introdueix la contrasenya: ")
        password_confirm = getpass.getpass("Confirma la contrasenya: ")
        if password == password_confirm:
            self._contrasenya = self.encriptar_contrasenya(password)
            print("Contrasenya guardada correctament.")
        else:
            print("Les contrasenyes no coincideixen. Torna-ho a intentar.")
            self.set_contrasenya()

    def verificar_contrasenya(self, password: str) -> bool:
        if self._contrasenya is None:
            return False
        return self.encriptar_contrasenya(password) == self._contrasenya

    def introduir_dades(self):
        super().introduir_dades()
        tipus = input("Introdueix el tipus d'usuari (lector/admin): ").lower()
        if tipus in ["lector", "admin"]:
            self.tipus_usuari = tipus
        else:
            self.tipus_usuari = "lector"
        self.set_contrasenya()