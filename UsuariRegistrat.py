from Usuari import Usuari
import hashlib
import getpass

class UsuariRegistrat(Usuari):
    def __init__(self, nom="None", cognoms="None", dni="None", tipus_usuari="lector"):
        super().__init__(nom, cognoms, dni)
        if tipus_usuari.lower() in ("lector", "admin"):
            self.tipus_usuari = tipus_usuari.lower()
        else:
            self.tipus_usuari = "lector"
        self._contrasenya = None

    def encriptar_contrasenya(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def set_contrasenya(self):
        while True:
            contrasenya = getpass.getpass("Introdueix la contrasenya: ")
            confirmacio = getpass.getpass("Confirma la contrasenya: ")
            if contrasenya == confirmacio:
                self._contrasenya = self.encriptar_contrasenya(contrasenya)
                print("Contrasenya guardada correctament.")
                break
            else:
                print("Les contrasenyes no coincideixen. Torna-ho a intentar.")

    def get_contrasenya(self):
        return self._contrasenya

    def verificar_contrasenya(self, password):
        if self._contrasenya is None:
            return False
        return self.encriptar_contrasenya(password) == self._contrasenya

    def introduir_dades(self):
        super().introduir_dades()
        tipus = input("Introdueix el tipus d'usuari (lector/admin): ").lower()
        if tipus in ("lector", "admin"):
            self.tipus_usuari = tipus
        else:
            self.tipus_usuari = "lector"

    def __str__(self):
        return f"{super().__str__()}, Tipus: {self.tipus_usuari}"
