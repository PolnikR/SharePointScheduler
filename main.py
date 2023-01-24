# Project : SharePoint Task Scheduler
# Author : AUTOCONT
# Cieľ projektu:
# Vytvorenie aplikácie ktorá bude obsahovat exe súbor, ktorý sa bude spúštať na základe kedy bude nastavený v plániči úloh
# Stack : Python,Tkinter,SharePlum,Schedule
# Výsledok: Aplikácia ktorá bude spúšťať exe súbor na základe nastaveného času v plániči úloh

# Main program

import sys
import GUI as gui

# Načítaj EXE subory zo SharePointu a ulož ich do premennej a vrat ich zoznam pre GUI

list = [{'Subor': 'test.exe', 'Firma': 'AUTOCONT', 'Den': 'Pondelok', 'Cas': '10:00', 'Automaticky': 'True'},
        {'Subor': 'test2.exe', 'Firma': 'Doprastaav', 'Den': 'Utorok', 'Cas': '10:00', 'Automaticky': 'True'},
        {'Subor': 'test3.exe', 'Firma': 'TEHO', 'Den': 'Streda', 'Cas': '10:00', 'Automaticky': 'True'},
        {'Subor': 'test4.exe', 'Firma': 'KIA', 'Den': 'Štvrtok', 'Cas': '10:00', 'Automaticky': 'True'},]

print(list)

# TO DO ROMAN : Vytvor okno 1 so prihlasovacími políčkami username a password a tlačidlom na prihlásenie


# TO DO ROMAN : Skontroluj ci username a password sú správne nastav username - admin password - admin


