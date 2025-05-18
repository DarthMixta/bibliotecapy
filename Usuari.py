import re
from datetime import datetime, timedelta

class Llibre:
    def __init__(self, titol: str = "None", autor: str = "None", dni_prestec: str = "None", data_prestec: datetime = None) -> str:
        self.titol = titol
        self.autor = autor
        self.dni_prestec = dni_prestec
        self.data_prestec = data_prestec

    def imprimir_dades(self) -> str:
        if self.dni_prestec != "None":
            prestat_info = f"Prestat a: {self.dni_prestec} el {self.data_prestec.strftime('%Y-%m-%d')}"
        else:
            prestat_info = "Disponible"
        return f"Títol: {self.titol}, Autor: {self.autor}, {prestat_info}"

    def introduir_dades(self) -> str:
        self.titol = input("Introdueix el títol del llibre: ")
        self.autor = input("Introdueix l'autor del llibre: ")
        self.dni_prestec = "None"
        self.data_prestec = None
        return "Dades del llibre introduïdes correctament."


def dni_valid(dni: str) -> bool:
    return re.fullmatch(r"\d{8}[A-Z]", dni) is not None