import sqlite3

class Tietokanta():
    def __init__(self):
        self.db = sqlite3.connect("kurssit.db")
        self.db.isolation_level = None  
        self.c = self.db.cursor()

    def haeVuodenOpMaara(self,vuosi):
        self.c.execute("""
            SELECT SUM(K.laajuus)
            FROM Kurssit K, Suoritukset S
            WHERE K.id=S.kurssi_id AND SUBSTR(S.paivays,1,4)=?
        """,[vuosi])
        return self.c.fetchone()[0]

    def haeOpiskelijanSuoritukset(self,nimi):
        self.c.execute("""
            SELECT K.nimi, K.laajuus, S.paivays, S.arvosana
            FROM Suoritukset S, Kurssit K, Opiskelijat O
            WHERE S.kurssi_id=K.id AND S.opiskelija_id=O.id AND O.nimi=?
            ORDER BY S.paivays
        """,[nimi])
        return self.c.fetchall()

    def laskeKurssinKeskiarvo(self,kurssi):
        self.c.execute("""
        SELECT SUM(S.arvosana),COUNT(S.arvosana)
        FROM Suoritukset S, Kurssit K
        WHERE S.kurssi_id=K.id AND K.nimi=?
        """,[kurssi])
        output = self.c.fetchall()
        if (output[0][0]==None):
            return "Kurssia ei löytynyt"
        return round(output[0][0]/output[0][1],2)

    def naytaTopX(self,lkm):
        self.c.execute("""
            SELECT O.nimi, SUM(K.laajuus)
            FROM Opettajat O, Kurssit K, Suoritukset S
            WHERE O.id=K.opettaja_id AND S.kurssi_id=K.id
            GROUP BY O.id
            ORDER BY SUM(K.laajuus) DESC
            LIMIT ?
        """,[lkm])
        return self.c.fetchall()
