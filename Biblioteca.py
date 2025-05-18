class Biblioteca:
    def __init__(self):
        self.usuaris = {}  # {dni: Usuari}
        self.llibres = {}  # {titol: Llibre}

    def afegir_usuari(self, usuari_str: str) -> str:
        try:
            dni, nom = usuari_str.split(",", 1)
            usuari = Usuari(nom.strip(), "", dni.strip())
            self.usuaris[dni.strip()] = usuari
            return f"Usuari {nom.strip()} afegit correctament."
        except Exception as e:
            return f"Error en afegir usuari: {e}"

    def afegir_llibre(self, llibre_str: str) -> str:
        try:
            titol, autor = llibre_str.split(",", 1)
            llibre = Llibre(titol.strip(), autor.strip())
            self.llibres[titol.strip()] = llibre
            return f"Llibre '{titol.strip()}' afegit correctament."
        except Exception as e:
            return f"Error en afegir llibre: {e}"

    def imprimir_usuaris(self) -> str:
        if not self.usuaris:
            return "No hi ha usuaris."
        return "\n".join([usuari.imprimir_dades() for usuari in self.usuaris.values()])

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
        llibre = self.llibres[titol]
        if llibre.dni_prestec != "None":
            return f"El llibre ja està prestat."
        llibre.dni_prestec = dni
        return f"Llibre '{titol}' prestat a {dni}."

    def tornar_llibre(self, titol: str) -> str:
        if titol not in self.llibres:
            return f"Llibre '{titol}' no trobat."
        llibre = self.llibres[titol]
        if llibre.dni_prestec == "None":
            return f"El llibre ja està disponible."
        llibre.dni_prestec = "None"
        return f"Llibre '{titol}' retornat correctament."