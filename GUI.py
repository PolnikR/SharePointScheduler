# Tento súbor obsahuje triedy a funkcie pre GUI aplikácie
# Na GUI použijem knižnicu Tkinter
#

class LoginWindow:
    # TO DO ROMAN : konštruktor triedy GUI ktory vytvori prázdne okno s logom v ľavo
    def __init__(self, master):
        pass

    # TO DO ROMAN : Pridaj do okna 2 input polia pre username a password a tlačidlo na prihlásenie
    def pridaj_Login(self):
        pass

    # TO DO ROMAN : Skontroluj ci username a password sú správne nastav username - admin password - admin
    def skontroluj_Login(self, username, password):
        if username == "admin" and password == "admin":
            self.zobraz_HlavneOkno()
        else:
            #Vypíš chybovú hlášku do okna a nezobraz hlavné okno ak sa prihlásenie nepodarilo
            pass

    def zobraz_HlavneOkno(self):
        pass

    #TO DO ROMAN : Gettery a Settery pre objekty Tkinter bude potrebny
    def getWindows(self):
        pass

class ScheduleWindow:
    # TO DO ROMAN : kontruktor triedy ktory zoberie vytvorené okno
    def __init__(self, window):
        pass

    # TO DO ROMAN : Pridaj tlacidlo ktore ktore načíta zoznam EXE suborov zo SharePointu a zobrazi ich v zozname
    def nacitaj(self):
        # TO DO ROMAN : Pridaj tlačidlo
        pass
        # if clicked: nacitaj zoznam EXE suborov

    # TO DO ROMAN : Pridaj tlacidlo kotre prida novy EXE subor do zoznamu EXE suborov
    def pridaj(self):
        # TO DO ROMAN : Pridaj tlačidlo
        pass
        # if clicked: zobraz okno add window

    # TO DO ROMAN : Zobraz zoznam EXE suborov v okne
    def zobraz(self, list):
        # TO DO ROMAN : Zobraz zoznam EXE suborov v okne aplikácie
        pass
        # TO DO ROMAN : Pridaj nazov EXE suboru do zoznamu
        # TO DO ROMAN : Pridaj dropdown na vyber firmy
        # TO DO ROMAN : Pridaj dropdown na vyber dňa v týždni
        # TO DO ROMAN : Pridaj dropdown na vyber času
        # TO DO ROMAN : Pridaj tlačidlo na vymazanie EXE suboru zo zoznamu
        # TO DO ROMAN : Pridaj tlačidlo na ručne spustenie EXE suboru
        # TO DO ROMAN : Pridaj checkbox na automatické spustenie EXE suboru
        # TO DO SIMON : Pridaj funkciu tlačidlam a checkboxu


    # TO DO ROMAN : Zobraz historiu spustenia EXE suborov v okne
    def zobraz_Historiu(self):
        pass
        # TO DO ROMAN : Pridaj nazov EXE suboru
        # TO DO ROMAN : Pridaj datum a čas spustenia EXE suboru

    # TO DO ROMAN : Pridaj graf do okna na zaklade firiem
    def zobraz_Graf(self):
        pass
        # TO DO ROMAN : Pridaj graf na zaklade firiem

class AddWindow:
    # TO DO ROMAN : kontruktor triedy ktory zoberie vytvorené okno
    def __init__(self, window):
        pass

    # TO DO ROMAN : pridaj inputy na nahratie suboru, nazov suboru, vyber firmy, vyber dňa v týždni, vyber času
    def pridaj(self):
        pass
        # TO DO ROMAN : Pridaj input na nahratie suboru
        # TO DO ROMAN : Pridaj input na nazov suboru
        # TO DO ROMAN : Pridaj dropdown na vyber firmy
        # TO DO ROMAN : Pridaj dropdown na vyber dňa v týždni
        # TO DO ROMAN : Pridaj funkciu tlačidlam a checkboxu

    # TO DO ROMAN : Pridaj tlačidlo na uloženie EXE suboru do SharePoint zoznamu
    def uloz(self):
        pass
        # TO DO ROMAN : if clicked: uloz EXE subor do SharePointu