# importamos la libreria de test
import unittest
import contador

class test_crear_constructor(unittest.TestCase): # heredamos de unittest de todo lo que sea unittest
    
    # Primer test:  Al crear el contador indicamos el valor inicial del mismo, el incremento y el valor límite. 
    
    def test1(self):

        #condicion inicial
        contador1 = contador.Contador(0, 2, 5)

        #verificamos la condicion
        self.assertEqual(contador1.inicial, 0)
        self.assertEqual(contador1.incremento, 2)
        self.assertEqual(contador1.limite, 5)

if __name__=="__main__":
    unittest.main()
