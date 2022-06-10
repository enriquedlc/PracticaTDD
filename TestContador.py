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


    # Segundo test:  El valor inicial y el incremento tomarán un valor de 0 y 1 respectivamente si no se indica nada. 
    # El  límite es necesario indicarlo siempre.  

    def test2(self):
        
        contador2 = contador.Contador(limite = 3)

        self.assertEqual(contador2.inicial, 0)
        self.assertEqual(contador2.incremento, 1)
        self.assertEqual(contador2.limite, 3)

if __name__=="__main__":
    unittest.main()
