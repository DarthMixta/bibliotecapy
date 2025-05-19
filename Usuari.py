class Usuari:
    def __init__(self, nom: str = "None", cognoms: str = "None", dni: str = "None") -> None:
        self.nom = nom
        self.cognoms = cognoms
        self.dni = dni

    def imprimir_dades(self) -> str:
        return f"DNI: {self.dni}, Nom: {self.nom}, Cognoms: {self.cognoms}"

    def introduir_dades(self) -> str:
        self.nom = input("Introdueix el nom de l'usuari: ")
        self.cognoms = input("Introdueix els cognoms de l'usuari: ")
        self.dni = input("Introdueix el DNI de l'usuari: ")
        return "Dades de l'usuari introduïdes correctament."