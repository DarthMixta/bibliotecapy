import hashlib
import getpass
from Usuari import Usuari

class UsuariRegistrat(Usuari):
    def __init__(self, nom, cognoms, dni, contrasenya=None, tipus_usuari=TipusUsuari.LECTOR.value):
        super().__init__(nom, cognoms, dni)
        self._contrasenya = None
        if contrasenya:
            self._contrasenya = self._encripta_contrasenya(contrasenya)
        
        if tipus_usuari not in [t.value for t in TipusUsuari]:
            raise ValueError(f"Tipus d'usuari no vàlid. Ha de ser {[t.value for t in TipusUsuari]}")
        self.tipus_usuari = tipus_usuari
    
    def _encripta_contrasenya(self, contrasenya):
        """
        Encripta una contrasenya utilitzant SHA-256
        
        Args:
            contrasenya (str): Contrasenya en text pla
            
        Returns:
            str: Contrasenya encriptada en hexadecimal
        """
        return hashlib.sha256(contrasenya.encode()).hexdigest()
    
    def verificar_contrasenya(self, contrasenya):
        """
        Verifica si una contrasenya coincideix amb l'emmagatzemada
        
        Args:
            contrasenya (str): Contrasenya en text pla a verificar
            
        Returns:
            bool: True si la contrasenya és correcta, False en cas contrari
        """
        if not self._contrasenya:
            return False
        return self._contrasenya == self._encripta_contrasenya(contrasenya)
    
    def introduir_dades(self):
        """
        Permet introduir les dades de l'usuari registrat per terminal
        Utilitza getpass per a la contrasenya
        """
        super().introduir_dades()
        contrasenya = getpass("Introdueix la contrasenya: ")
        self._contrasenya = self._encripta_contrasenya(contrasenya)
        
        while True:
            tipus = input(f"Introdueix el tipus d'usuari ({[t.value for t in TipusUsuari]}): ").lower()
            if tipus in [t.value for t in TipusUsuari]:
                self.tipus_usuari = tipus
                break
            print("Tipus d'usuari no vàlid!")
    
    def imprimir_dades(self):
        """Imprimeix les dades de l'usuari registrat (sense la contrasenya)"""
        super().imprimir_dades()
        print(f"Tipus d'usuari: {self.tipus_usuari}")
    
    @property
    def contrasenya(self):
        """Getter per a la contrasenya (retorna None per seguretat)"""
        return None
    
    @contrasenya.setter
    def contrasenya(self, nova_contrasenya):
        """
        Setter per a la contrasenya. Encripta automàticament la nova contrasenya.
        
        Args:
            nova_contrasenya (str): Nova contrasenya en text pla
        """
        self._contrasenya = self._encripta_contrasenya(nova_contrasenya)