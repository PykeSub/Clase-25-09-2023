class Auto:
    # Constructor
    def __init__(self, color: str, marca: str, anio: int, cc: float, patente: str):
        # Atributos Publicos
        self.color = color
        self.marca = marca
        self.anio = anio
        self.cc = cc
        # Atributos Privados
        self.__patente = patente
        self.__n_ruedas = 4
        
        
        # get (ES OBTENER) ----> Es una funcion que retorna un atributo privado.
        def get_patente(self):
            return self.__patente
        
        # set (ES CAMBIAR) ----> Es una funcion que recibe un parametro y modifica un atributo.
        def set_patente(self, patente: str):
            self.__patente = patente
            
        #str ----> Es una funcion  
        def __str__(self):
            texto = f'Color:{self.color}'
            texto+= f'\nMarca:{self.marca}'
            texto+= f'\nAnio:{self.anio}'
            texto+= f'\nCC:{self.cc}'
            texto+= f'\nPatente:{self.__patente}'
            texto+= f'\nNumero Ruedas:{self.__n_ruedas}'
            return texto
        
        # Atributos
        # Metodos