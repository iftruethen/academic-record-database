from tietokanta import Tietokanta

class Kayttoliittyma():
    def kaynnista(self):
        self.tk = Tietokanta()
        self.lueSyote()

    def printHelp(self):
        print("""
        Toimintokomennot, syötä numero valitaksesi toiminnon:
        1 - Tulosta kaikkien myönnettyjen opintopisteiden määrän valitulta vuodelta
        2 - Tulosta valitun opiskelijan opintosuoritukset
        3 - Tulosta valitun kurssin myönnettyjen suoritusten keskiarvo
        4 - Tulosta lista eniten opintopisteitä myöntäneistä opettajista
        5 - Lopeta ohjelma
        """)


    def lueSyote(self):
        self.printHelp()
        while True:
            syote = input("Valitse toiminto: ")

            if (syote == "1"):
                sVuosi = input("Anna vuosi: ")
                print("Opintopisteiden määrä: " + 
                	str(self.tk.haeVuodenOpMaara(str(sVuosi))))

            elif (syote == "2"):
                sNimi = input("Anna opiskelijan nimi: ")
                output = self.tk.haeOpiskelijanSuoritukset(sNimi)
                if (len(output) == 0):
                    print("Opiskelijaa ei löytynyt")
                else:
                    self.print_table(output,[("kurssi","op","päiväys","arvosana")])

            elif (syote == "3"):
                sKurssi = input("Anna kurssin nimi: ")
                print("Keskiarvo: " + str(self.tk.laskeKurssinKeskiarvo(sKurssi)))

            elif (syote == "4"):
                sLkm = input("Anna opettajien määrä: ")
                output = self.tk.naytaTopX(sLkm)
                self.print_table(output,[("opettaja","op")])

            elif (syote == "5"):
                exit()

            else:
                print("Tarkista syöte")

    def print_table(self,table,otsakkeet):
        col_width = [max(len(str(x)) for x in col) for col in zip(*table)]
        for otsake in otsakkeet:
            print ("" + " \t".join("{0:{1}}".format(x, col_width[i])
                                    for i, x in enumerate(otsake)) + "")
        for line in table:
            print ("" + " \t".join("{0:{1}}".format(x, col_width[i])
                                    for i, x in enumerate(line)) + "")
