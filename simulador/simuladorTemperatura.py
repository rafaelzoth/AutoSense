import csv
import random
import time
from datetime import datetime
from pathlib import Path

idSensor = "TEMP001"
caminhoArquivo = Path(__file__).parent.parent / "dados" / "temperaturas.csv"


def lerTemperaturaSimulada():
    #Hoje simula; depois será substituída pela leitura do Arduino.
    return round(random.gauss(27, 2), 1)


def coletarRegistros(quantidade, intervalo = 1):
    registros = []
    for _ in range(quantidade):
        registros.append([
            idSensor,
            datetime.now().isoformat(timespec = "seconds"),
            lerTemperaturaSimulada(),
        ])
        time.sleep(intervalo)
    return registros


def exportarRegistros(registros, caminho = caminhoArquivo):
    caminho.parent.mkdir(parents = True, exist_ok = True)
    with open(caminho, "w", newline = "", encoding = "utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["idSensor", "timestamp", "temperatura"])
        escritor.writerows(registros)


if __name__ == "__main__":
    registros = coletarRegistros(10)
    for registro in registros:
        print(registro)
    exportarRegistros(registros)