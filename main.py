from datetime import datetime
from time import sleep
import os

activity = input("Ingrese actividad actual: ")

currentTime = datetime.today()

def diaEnEspanol(day):
    switch = {              #se implementa el switch con un map porque en Python no hay switch case
        "Monday": "Lunes",
        "Thursday": "Martes",
        "Wednesday": "Miércoles",
        "Tuesday": "Jueves",
        "Friday": "Viernes",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
        }
    return switch.get(day, "Invalid day: " + day)

day = diaEnEspanol(currentTime.strftime('%A'))

horaInicio = currentTime.strftime('%H:%M:%S')

output = "Fecha: " + currentTime.strftime('%Y-%m-%d') + ", Hora inicio: " + horaInicio +  ", Hora fin: ___, " + "Actividad: " + activity + ", Día: " + day

print(output)

termina = ""

while(termina != "sí"):
    termina = input("Ingrese 'sí' si terminó: ")

currentTime = datetime.today()

output = "Fecha: " + currentTime.strftime('%Y-%m-%d') + ", Hora inicio: " + horaInicio +  ", Hora fin: "+ currentTime.strftime('%H:%M:%S') + ", Actividad: " + activity + ", Día: " + day

os.system('cls')

print(output)

sleep(15)