# Tento súbor obsahuje triedy a funkcie pre GUI aplikácie
# Na GUI použijem knižnicu Tkinter
#
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk





class LoginWindow:
    # TO DO ROMAN : konštruktor triedy GUI ktory vytvori prázdne okno
    def __init__(self, master=None):
        self.root = Tk()
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.canvas = Canvas(self.root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.list = [{'Subor': 'test.exe', 'Firma': 'AUTOCONT', 'Den': 'Pondelok', 'Cas': '10:00', 'Automaticky': 'True'},
                {'Subor': 'test2.exe', 'Firma': 'Doprastaav', 'Den': 'Utorok', 'Cas': '10:00', 'Automaticky': 'True'},
                {'Subor': 'test3.exe', 'Firma': 'TEHO', 'Den': 'Streda', 'Cas': '10:00', 'Automaticky': 'True'},
                {'Subor': 'test4.exe', 'Firma': 'KIA', 'Den': 'Štvrtok', 'Cas': '10:00', 'Automaticky': 'True'}, ]


    # TO DO ROMAN : Pridaj v ľavo logo
    def pridaj_Logo(self):
        my_image = PhotoImage(file="autocontLogo.png")
        myImage = self.canvas.create_image(175,175, image=my_image)

        self.root.mainloop()
        
    #TO DO ROMAN : Pridaj hlavny nadpis
    def pridaj_Nadpis(self):
        self.root.title("Login Window")


    # TO DO ROMAN : Pridaj do okna 2 input polia pre username a password a tlačidlo na prihlásenie
    def pridaj_Login(self, name):

        user_text_entry = Entry(self.canvas)
        password_text_entry = Entry(self.canvas)

        self.canvas.create_text(450, 25, text="Sharepoint Scheduler", fill="black", font=('Helvetica 12 bold'))
        self.canvas.create_text(405, 100, text="Username", fill="black", font=('Helvetica 12'))
        self.canvas.create_text(405, 190, text="Password", fill="black", font=('Helvetica 12'))
        
        self.canvas.create_window(445, 135, window=user_text_entry, height=25, width=150)
        self.canvas.create_window(445, 225, window=password_text_entry, height=25, width=150)

        button1 = Button(self.canvas, text="Login", command=lambda:self.skontroluj_Login(user_text_entry.get(), password_text_entry.get()))
        button1.configure(width=20, height=3, bd=3,activebackground="#33B5E5", relief=FLAT)
        button1_window = self.canvas.create_window(370, 270, anchor=NW, window=button1)
        self.canvas.pack()



        
    # TO DO ROMAN : Skontroluj ci username a password sú správne nastav username - admin password - admin
    def skontroluj_Login(self, username, password):
        if username == "admin" and password == "admin":
            self.canvas.destroy()
            self.zobraz_HlavneOkno()

            
        else:
            #Vypíš chybovú hlášku do okna a nezobraz hlavné okno ak sa prihlásenie nepodarilo
            self.canvas.create_text(460, 250, text="Nespravne heslo alebo username!", fill="red", font=('Helvetica 8 bold'))

    # TO DO ROMAN : Hlavne okno sa vytvori cez triedy ScheduleWindow
    def zobraz_HlavneOkno(self):

        schedule_window = ScheduleWindow(self.getWindows())
        schedule_window.nacitaj()
        schedule_window.pridaj()
        schedule_window.zobraz(self.list)
        schedule_window.zobraz_Historiu(self.list)
        schedule_window.zobraz_Graf(self.list)



    #TO DO ROMAN : Gettery a Settery pre objekty Tkinter bude potrebny
    def getWindows(self):
        #self.canvas.destroy()
        return self.root

class ScheduleWindow:
    # TO DO ROMAN : kontruktor triedy ktory zoberie vytvorené okno
    def __init__(self, window):
        self.window = window
        self.window.title("Scheduler Window")
        self.frame = Frame(self.window, width=600, height=400, background="white")
        share_label = ttk.Label(self.frame, text="Sharepoint Scheduler", background="white", font=("Helvetica 12"))

        share_label.place(x=30,y=15)

        self.frame.pack()



    # TO DO ROMAN : Pridaj tlacidlo ktore ktore načíta zoznam EXE suborov zo SharePointu a zobrazi ich v zozname
    def nacitaj(self):
        # TO DO ROMAN : Pridaj tlačidlo
        button_nacitaj = Button(self.frame, text="Nacitaj", command="", width=12, height=2, activebackground="#33B5E5",
                               relief=FLAT)
        button_nacitaj.place(x=490, y=6)



        # TO DO SIMON : Pridaj funkcionality tlačidla

    # TO DO ROMAN : Pridaj tlacidlo kotre prida novy EXE subor do zoznamu EXE suborov
    def pridaj(self):
        # TO DO ROMAN : Pridaj tlačidlo
        button_pridaj = Button(self.frame, text="Pridaj", command=lambda:self.pridaj_clicked(), width=12,height=2,activebackground="#33B5E5", relief=FLAT)

        button_pridaj.place(x=380, y=6)
        # if clicked: zobraz okno add window

    # TO DO ROMAN : Zobraz zoznam EXE suborov v okne
    def zobraz(self, list):
        # TO DO ROMAN : Zobraz zoznam EXE suborov v okne aplikácie
        # Všetky udaje na zobraenie su v liste
        # TO DO ROMAN : Pridaj nazov EXE suboru do zoznamu
        # TO DO ROMAN : Pridaj dropdown na vyber firmy
        # TO DO ROMAN : Pridaj dropdown na vyber dňa v týždni
        # TO DO ROMAN : Pridaj dropdown na vyber času
        # TO DO ROMAN : Pridaj tlačidlo na vymazanie EXE suboru zo zoznamu
        # TO DO ROMAN : Pridaj tlačidlo na ručne spustenie EXE suboru
        # TO DO ROMAN : Pridaj checkbox na automatické spustenie EXE suboru
        # TO DO SIMON : Pridaj funkciu tlačidlam a checkboxu

        self.frame.picture_del = PhotoImage(file="dele_button.png")
        self.frame.picture_ok = PhotoImage(file="ok_button.png")

        firma_values = []
        dni_values = []
        cas_values = []
        i=0
        for y in list:
            firma_values.append(y["Firma"])
            dni_values.append(y["Den"])
            cas_values.append(y["Cas"])
        for x in list:

            nazov_label = ttk.Label(self.frame, text=x["Subor"], background="white", font=("Helvetica 10"))
            combo_firma = ttk.Combobox(self.frame, width=15, values=firma_values)
            combo_firma.set(x["Firma"])
            combo_den = ttk.Combobox(self.frame, width=15, values=dni_values)
            combo_den.set(x["Den"])
            combo_cas = ttk.Combobox(self.frame, width=15, values=cas_values)
            combo_cas.set(x["Cas"])

            button_vymaz = Button(self.frame, image=self.frame.picture_del, text="Pridaj",
                                  command=lambda: self.pridaj_clicked(),
                                  activebackground="white", bg="white", relief=FLAT)

            button_ok = Button(self.frame, image=self.frame.picture_ok, text="Pridaj",
                               command=lambda: self.pridaj_clicked(), width=25, height=25,
                               activebackground="white", bg="white", relief=FLAT)

            check_box = Checkbutton(self.frame, background="white")

            nazov_label.place(x=30, y=100+i)
            combo_firma.place(x=120, y=100+i)
            combo_den.place(x=240, y=100+i)
            combo_cas.place(x=360, y=100+i)
            button_vymaz.place(x=480, y=95+i)
            button_ok.place(x=520, y=95+i)
            check_box.place(x=560, y=100+i)

            i+=30

    # TO DO SIMON : Vymaž EXE subor zo zoznamu
    def vymazSubor(self):
        pass

    # TO DO SIMON : Spusti EXE subor
    def spustiRucne(self):
        pass

    # TO DO SIMON : Spusti EXE subor automaticky
    def spustiAutomaticky(self):
        pass

    def zobraz_Historiu(self,zoznaHistoria):
        pass
        # TO DO ROMAN : Pridaj nazov EXE suboru
        # TO DO ROMAN : Pridaj datum a čas spustenia EXE suboru
        history_label = ttk.Label(self.frame, text="Historia", background="white", font=("Helvetica 12"))

        history_label.place(x=30, y=250)
        i=0
        for x in zoznaHistoria:

            nazov_label = ttk.Label(self.frame, text=x["Subor"], background="white", font=("Helvetica 10"))
            date_label = ttk.Label(self.frame, text=x["Cas"], background="white", font=("Helvetica 10"))
            nazov_label.place(x=30, y=280+i)
            date_label.place(x=80, y=280+i)
            i+=15


    # TO DO ROMAN : Pridaj graf do okna na zaklade firiem - neviem vlozit graf
    def zobraz_Graf(self,zoznaHistoria):
        pass

        # TO DO ROMAN : Pridaj graf na zaklade firiem
    def pridaj_clicked(self):
        self.frame.destroy()
        add_window = AddWindow(self.getWindow())
        add_window.pridaj()
        add_window.pridaj_CervenuFarbu()


    def getWindow(self):
        return self.window

class AddWindow:

    # TO DO ROMAN : kontruktor triedy ktory zoberie vytvorené okno
    def __init__(self, window):
        self.add_window = window
        self.add_window.title("Sharepoint Scheduler Window")
        self.add_window["bg"] = "white"

        self.frame = Frame(self.add_window, width=600, height=400, background="white")
        self.frame.pack()
        self.list = [{'Subor': 'test.exe', 'Firma': 'AUTOCONT', 'Den': 'Pondelok', 'Cas': '10:00', 'Automaticky': 'True'},
               {'Subor': 'test2.exe', 'Firma': 'Doprastaav', 'Den': 'Utorok', 'Cas': '10:00', 'Automaticky': 'True'},
               {'Subor': 'test3.exe', 'Firma': 'TEHO', 'Den': 'Streda', 'Cas': '10:00', 'Automaticky': 'True'},
               {'Subor': 'test4.exe', 'Firma': 'KIA', 'Den': 'Štvrtok', 'Cas': '10:00', 'Automaticky': 'True'}, ]

    # TO DO ROMAN : pridaj v pravo červenu farbu

    def pridaj_CervenuFarbu(self):

        pic_label = Label(self.frame, background="red", width=150, height=400)
        pic_label.place(x=450, y=0)

    # TO DO ROMAN : pridaj inputy na nahratie suboru, nazov suboru, vyber firmy, vyber dňa v týždni, vyber času
    def pridaj(self):
        # TO DO ROMAN : Pridaj input na nahratie suboru
        # TO DO ROMAN : Pridaj input na nazov suboru
        # TO DO ROMAN : Pridaj dropdown na vyber firmy
        # TO DO ROMAN : Pridaj dropdown na vyber dňa v týždni

        share_label = ttk.Label(self.frame,text="Sharepoint Scheduler", background="white", font=("Helvetica 12"))
        nahraj_label = ttk.Label(self.frame,text="Nahraj subor:", background="white", font=("Helvetica 10"))

        self.entry_nahraj_subor= tkinter.Entry(self.frame, width=33)

        firmy_list = ["Autocont", "Doprastav"]
        dni_list = ["Pondelok", "Utorok","Streda", "Stvrtok", "Piatok", "Sobota", "Nedela"]

        self.combo_firma = ttk.Combobox(self.frame, values=firmy_list, width=30)
        self.combo_firma.set("Vyber firmu")

        self.combo_dni = ttk.Combobox(self.frame, values=dni_list, width=30)
        self.combo_dni.set("Vyber den")

        button_pridaj = Button(self.frame, text="Pridaj", command=lambda: self.uloz(), width=12,height=2,activebackground="#33B5E5", relief=FLAT)
        button_spat = Button(self.frame, text="Spat", command=lambda: self.spat(), width=12, height=2,activebackground="#33B5E5", relief=FLAT)

        share_label.place(x=50, y=25)
        nahraj_label.place(x=50, y=75)

        self.entry_nahraj_subor.place(x=50,y=100)

        self.combo_firma.place(x=50,y=150)
        self.combo_dni.place(x=50, y=200)

        button_pridaj.place(x=50, y=270)
        button_spat.place(x=160, y=270)

    # TO DO ROMAN : Pridaj tlačidlo na uloženie EXE suboru do SharePoint zoznamu
    def uloz(self):
        if self.entry_nahraj_subor.get() != "" and self.combo_firma.current() != -1 and self.combo_dni.current() != -1:
            self.frame.destroy()
            schedule_window = ScheduleWindow(self.getWindow())
            schedule_window.nacitaj()
            schedule_window.pridaj()
            schedule_window.zobraz(self.list)
        else:
            messagebox.showinfo("Info","Neulozene")
        # TO DO ROMAN : if clicked skontoluj a ulž udaje do sharepointu -nemam este

    # TO DO ROMAN : Pridaj tlačidlo na vratenie sa do hlavného okna
    def spat(self):
        self.frame.destroy()
        schedule_window = ScheduleWindow(self.getWindow())
        schedule_window.nacitaj()
        schedule_window.pridaj()
        schedule_window.zobraz(self.list)
        schedule_window.zobraz_Historiu(self.list)

    def getWindow(self):
        return self.add_window
