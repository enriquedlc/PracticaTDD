# importamos la libreria de test
import unittest
import contador

class test_crear_constructor(unittest.TestCase): # heredamos de unittest de todo lo que sea unittest
    
    # Primer test:  Al crear el contador indicamos el valor inicial del mismo, el incremento y el valor límite. 
    
    def test1(self):

        #condicion inicial
        contador1 = contador.Contador(0, 2, 5)
        contador1.__inicial = 1

        #verificamos la condicion
        self.assertEqual(contador1.getInicial(), 0)
        self.assertEqual(contador1.getIncremento(), 2)
        self.assertEqual(contador1.getLimite(), 5)


    # Segundo test:  El valor inicial y el incremento tomarán un valor de 0 y 1 respectivamente si no se indica nada. 
    # El  límite es necesario indicarlo siempre.  

    def test2(self):
        
        contador2 = contador.Contador(limite = 3)

        self.assertEqual(contador2.getInicial(), 0)
        self.assertEqual(contador2.getIncremento(), 1)
        self.assertEqual(contador2.getLimite(), 3)

        #  Tercer Test: Ninguno de los tres valores (valor inicial, incremento y límite) pueden cambiarse una vez creado  el contador. 

    def test3(self):
         
         contador3 = contador.Contador(limite = 7)
         contador3.__inicial = 1

         self.assertEqual(contador3.getInicial(), 0)
         self.assertEqual(contador3.getIncremento(), 1)
         self.assertEqual(contador3.getLimite(), 7)

    def test4(self):
        contador4 = contador.Contador(limite = 5)
        

        contador4.incrementarValorInicial()
        self.assertEqual(contador4.getValorActualContador(), 1)
        contador4.incrementarValorInicial()
        self.assertEqual(contador4.getValorActualContador(), 2)
        contador4.incrementarValorInicial()
        self.assertEqual(contador4.getValorActualContador(), 3)
        contador4.incrementarValorInicial()
        self.assertEqual(contador4.getValorActualContador(), 4)
        contador4.incrementarValorInicial()
        self.assertEqual(contador4.getValorActualContador(), 5)
        contador4.incrementarValorInicial()

if __name__=="__main__":
    unittest.main()
