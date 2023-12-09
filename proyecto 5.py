import os
import random

class Juego:
    def __init__(self, mapa, posicion_inicial, posicion_final):
        self.mapa = mapa
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final

    def imprimir_mapa(self):
        print(self.mapa)

    def mover(self, direccion):
        # Lógica para moverse en el mapaclass JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        # Obtener una lista de archivos en el directorio de mapas
        archivos_mapas = os.listdir(path_a_mapas)

        # Elegir un archivo al azar
        nombre_archivo = random.choice(archivos_mapas)

        # Componer la ruta completa al archivo
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        # Llamar al constructor de la clase base (Juego) con los datos del archivo
        super().__init__(*self._leer_archivo(path_completo))

    def _leer_archivo(self, path):
        with open(path, 'r') as archivo:
            # Leer la primera línea para obtener las dimensiones
            dimensiones = archivo.readline().split()
            filas, columnas = int(dimensiones[0]), int(dimensiones[1])

            # Leer el resto del archivo
            contenido = archivo.read()

            # Encontrar las coordenadas de inicio y fin
            inicio, fin = contenido.split(' ')[-2:]

            # Retornar los datos como una tupla
            return contenido.strip(), inicio, fin

# Ejemplo de uso
if __name__ == "__main__":
    # Instanciar la clase JuegoArchivo con la carpeta de mapas como parámetro
    juego = JuegoArchivo("carpeta_de_mapas")

    # Imprimir el mapa y coordenadas iniciales y finales
    juego.imprimir_mapa()
    print("Posición Inicial:", juego.posicion_inicial)
    print("Posición Final:", juego.posicion_final)
