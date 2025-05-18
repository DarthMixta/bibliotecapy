import re
from datetime import datetime, timedelta

class Biblioteca:
    def __init__(self):
        self.usuaris = {}
        self.llibres = {}

    def afegir_usuari(self, usuari: str) -> str:
        try:
            dni, nom = usuari.split(",", 1)
            dni = dni.strip()
            nom = nom.strip()
            if not dni_valid(dni):
                return f"DNI invàlid: {dni}"
            self.usuaris[dni] = nom
            return f"Usuari {nom} afegit correctament."
        except Exception as e:
            return f"Error en afegir usuari: {e}"

    def actualitzar_usuari(self, dni: str, nou_nom: str) -> str:
        if dni in self.usuaris:
            self.usuaris[dni] = nou_nom.strip()
            return f"Nom actualitzat a {nou_nom.strip()} per DNI {dni}."
        return f"Usuari amb DNI {dni} no trobat."

    def afegir_llibre(self, llibre_str: str) -> str:
        try:
            titol, autor = llibre_str.split(",", 1)
            llibre = Llibre(titol.strip(), autor.strip())
            self.llibres[titol.strip()] = llibre
            return f"Llibre '{titol.strip()}' afegit correctament."
        except Exception as e:
            return f"Error en afegir llibre: {e}"

    def actualitzar_llibre(self, titol: str, nou_autor: str) -> str:
        if titol in self.llibres:
            self.llibres[titol].autor = nou_autor.strip()
            return f"Autor actualitzat a {nou_autor.strip()} per llibre '{titol}'."
        return f"Llibre '{titol}' no trobat."

    def imprimir_usuaris(self) -> str:
        if not self.usuaris:
            return "No hi ha usuaris."
        return "\n".join([f"{dni} - {nom}" for dni, nom in self.usuaris.items()])

    def imprimir_llibres(self, filtre: str = "tots") -> str:
        if not self.llibres:
            return "No hi ha llibres."

        resultat = []
        for llibre in self.llibres.values():
            if filtre == "tots":
                resultat.append(llibre.imprimir_dades())
            elif filtre == "disponibles" and llibre.dni_prestec == "None":
                resultat.append(llibre.imprimir_dades())
            elif filtre == "prestats" and llibre.dni_prestec != "None":
                resultat.append(llibre.imprimir_dades())
        return "\n".join(resultat) if resultat else "Cap llibre coincideix amb el filtre."

    def eliminar_usuari(self, dni: str) -> str:
        if dni in self.usuaris:
            del self.usuaris[dni]
            for llibre in self.llibres.values():
                if llibre.dni_prestec == dni:
                    llibre.dni_prestec = "None"
                    llibre.data_prestec = None
            return f"Usuari amb DNI {dni} eliminat."
        return f"Usuari amb DNI {dni} no trobat."

    def eliminar_llibre(self, titol: str) -> str:
        if titol in self.llibres:
            del self.llibres[titol]
            return f"Llibre '{titol}' eliminat."
        return f"Llibre '{titol}' no trobat."

    def prestar_llibre(self, titol: str, dni: str) -> str:
        if titol not in self.llibres:
            return f"Llibre '{titol}' no trobat."
        if dni not in self.usuaris:
            return f"Usuari amb DNI {dni} no trobat."
        if not dni_valid(dni):
            return f"DNI invàlid: {dni}"

        llibre = self.llibres[titol]
        if llibre.dni_prestec != "None":
            return f"El llibre ja està prestat."

        llibres_prestats = [l for l in self.llibres.values() if l.dni_prestec == dni]
        if len(llibres_prestats) >= 3:
            return "L'usuari ja té 3 llibres prestats."

        llibre.dni_prestec = dni
        llibre.data_prestec = datetime.now()
        return f"Llibre '{titol}' prestat a {dni}."

    def tornar_llibre(self, titol: str) -> str:
        if titol not in self.llibres:
            return f"Llibre '{titol}' no trobat."

        llibre = self.llibres[titol]
        if llibre.dni_prestec == "None":
            return f"El llibre ja està disponible."

        if datetime.now() - llibre.data_prestec > timedelta(days=30):
            avis = " (ATENCIÓ: préstec excedit d'un mes)"
        else:
            avis = ""

        llibre.dni_prestec = "None"
        llibre.data_prestec = None
        return f"Llibre '{titol}' retornat correctament.{avis}"