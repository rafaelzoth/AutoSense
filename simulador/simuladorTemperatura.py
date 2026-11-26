from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo
import time
import csv

idSensor = 'TEMP001'
registros = []

# simulacao de temperaturas
temperaturasSimuladas = [25, 30, 27, 30, 24, 35, 31, 25, 25, 30]
# fim das temperaturas simuladas

for i in range(len(temperaturasSimuladas)):
    horario = datetime.now().strftime('%H:%M:%S')
    registroAtual = [idSensor, horario, temperaturasSimuladas[i]]
    registros.append(registroAtual)

    # simular 1seg entre os registros
    time.sleep(1)
    #fim da simulacao de tempo

for i in registros:
    print(i)


# exportar os dados

arquivo = open('../dados/temperaturas.csv', 'w')
escritor = csv.writer(arquivo)
escritor.writerow(['idSensor', 'horario', 'temperatura'])

for i in registros:
    escritor.writerow(i)

arquivo.close()