import unittest
from datetime import datetime, timedelta
from Biblioteca import Biblioteca, Llibre, dni_valid

class TestDniValid(unittest.TestCase):
    def test_dni_correcte(self):
        self.assertTrue(dni_valid("12345678Z"))
    
    def test_dni_incorrecte_format(self):
        self.assertFalse(dni_valid("1234Z"))
        self.assertFalse(dni_valid("ABCDEFGHZ"))
        self.assertFalse(dni_valid("12345678z")) 

class TestLlibre(unittest.TestCase):
    def test_imprimir_disponible(self):
        llibre = Llibre("Títol X", "Autor Y")
        esperat = "Títol: Títol X, Autor: Autor Y, Disponible"
        self.assertEqual(llibre.imprimir_dades(), esperat)

    def test_imprimir_prestat(self):
        llibre = Llibre("Títol X", "Autor Y", "12345678Z", datetime(2024, 5, 1))
        self.assertIn("Prestat a: 12345678Z el 2024-05-01", llibre.imprimir_dades())


class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.biblio = Biblioteca()

    def test_afegir_usuari_valid(self):
        resposta = self.biblio.afegir_usuari("12345678Z, Joan")
        self.assertEqual(resposta, "Usuari Joan afegit correctament.")
        self.assertIn("12345678Z", self.biblio.usuaris)

    def test_afegir_usuari_invalid(self):
        resposta = self.biblio.afegir_usuari("ABC, Joan")
        self.assertIn("DNI invàlid", resposta)

    def test_afegir_llibre(self):
        resposta = self.biblio.afegir_llibre("1984, George Orwell")
        self.assertIn("afegit correctament", resposta)
        self.assertIn("1984", self.biblio.llibres)

    def test_prestar_llibre(self):
        self.biblio.afegir_usuari("12345678Z, Maria")
        self.biblio.afegir_llibre("1984, Orwell")
        resposta = self.biblio.prestar_llibre("1984", "12345678Z")
        self.assertIn("prestat a 12345678Z", resposta)

    def test_tornar_llibre_dins_termini(self):
        self.biblio.afegir_usuari("12345678Z, Maria")
        self.biblio.afegir_llibre("1984, Orwell")
        self.biblio.prestar_llibre("1984", "12345678Z")
        resposta = self.biblio.tornar_llibre("1984")
        self.assertIn("retornat correctament", resposta)

    def test_tornar_llibre_passat_termini(self):
        self.biblio.afegir_usuari("12345678Z, Maria")
        self.biblio.llibres["1984"] = Llibre("1984", "Orwell", "12345678Z", datetime.now() - timedelta(days=40))
        resposta = self.biblio.tornar_llibre("1984")
        self.assertIn("excedit d'un mes", resposta)

    def test_limit_llibres_prestats(self):
        self.biblio.afegir_usuari("12345678Z, Marc")
        for i in range(3):
            self.biblio.afegir_llibre(f"Llibre{i}, Autor")
            self.biblio.prestar_llibre(f"Llibre{i}", "12345678Z")
        self.biblio.afegir_llibre("LlibreExtra, Autor")
        resposta = self.biblio.prestar_llibre("LlibreExtra", "12345678Z")
        self.assertIn("ja té 3 llibres", resposta)


if __name__ == '__main__':
    unittest.main()