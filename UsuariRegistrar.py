import hashlib
from Usuari import Usuari

class UsuariRegistrat(Usuari):
    def __init__(self, nom: str = "None", cognoms: str = "None", dni: str = "None",
                 contrasenya: str = "", tipus_usuari: str = "usuari") -> None:
        super().__init__(nom, cognoms, dni)
        self._contrasenya = self._encripta_contrasenya(contrasenya)
        self.tipus_usuari = tipus_usuari

    def _encripta_contrasenya(self, contrasenya: str) -> str:
        return hashlib.sha256(contrasenya.encode()).hexdigest()

    def verificar_contrasenya(self, contrasenya: str) -> bool:
        return self._encripta_contrasenya(contrasenya) == self._contrasenya

    def introduir_dades(self) -> str:
        super().introduir_dades()
        raw_contrasenya = input("Introdueix la contrasenya: ")
        self._contrasenya = self._encripta_contrasenya(raw_contrasenya)
        self.tipus_usuari = input("Introdueix el tipus d'usuari (ex. admin, client...): ")
        return "Dades de l'usuari registrat introduïdes correctament."

    def imprimir_dades(self) -> str:
        dades_base = super().imprimir_dades()
        return f"{dades_base}, Tipus d'usuari: {self.tipus_usuari}"

    def contrasenya(self) -> str:
        return "Accés restringit a la contrasenya encriptada."