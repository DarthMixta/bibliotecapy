class Llibre:
    def __init__(self, titol: str = "None", autor: str = "None", dni_prestec: str = "None") -> str:
        self.titol = titol
        self.autor = autor
        self.dni_prestec = dni_prestec

    def imprimir_dades(self) -> str:
        prestat_info = f"Prestat a: {self.dni_prestec}" if self.dni_prestec != "None" else "Disponible"
        return f"Títol: {self.titol}, Autor: {self.autor}, {prestat_info}"

    def introduir_dades(self) -> str:
        self.titol = input("Introdueix el títol del llibre: ")
        self.autor = input("Introdueix l'autor del llibre: ")
        self.dni_prestec = "None"
        return "Dades del llibre introduïdes correctament."