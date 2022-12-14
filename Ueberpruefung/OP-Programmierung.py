
from enum import Enum
# Firma hat einen Namen, anzahl Mitarbeiter, anzahl Gruppenleiter, 

class Gender(Enum):
    Male = 0
    Female =  1


class Firma:
    def __init__(self, name, ustd_number, abteilungen):
        self.name = name
        self.ustd_number = ustd_number
        self.abteilungen = abteilungen
    
    def get_anzahl_Mitarbeiter(self):
        anz = 0
        for ab in self.abteilungen:
            anz += ab.get_anz_mitarbeiter()
        return anz
    
    def get_abteilungsleiter(self):
        abt = []
        for ele in self.abteilungen:
            abt.append(ele.abteilungsleiter)
        return abt
    
    def quote_Female_Male(self):
        dict_quote = {"Male" : 0, "Female" : 0, "Quote_Woman": 0}
        all_mit = []
        for ele in self.abteilungen:
            all_mit = all_mit + ele.mitarbeiter
            all_mit.append(ele.abteilungsleiter)
        for i in all_mit:
            if(i.geschlecht == Gender.Female):
                dict_quote["Female"] +=1
            else:
                dict_quote["Male"] += 1
        dict_quote["Quote_Woman"] = dict_quote["Female"]/self.get_anzahl_Mitarbeiter() 
        return dict_quote
        

    def get_biggest_department(self):
        biggest = 0
        name = ""
        for ab in self.abteilungen:
            if(ab.get_anz_mitarbeiter() > biggest):
                biggest = ab.get_anz_mitarbeiter()
                name = ab.name
        return name + "_" + str(biggest)

    def print(self):
        return self.name + "--" + str(self.ustd_number) + "--" + self.abteilungen

class Abteilung:
    def __init__(self, name, mitarbeiter, abteilungsleiter):
        self.name = name
        self.mitarbeiter = mitarbeiter
        self.abteilungsleiter = abteilungsleiter
    
    def print(self):
        return "Name: " + self.name +  " Abteilungsleiter: " + self.abteilungsleiter.print()

    def get_anz_mitarbeiter(self):
        return len(self.mitarbeiter) + 1 #only one Abteilungsleiter

class Person:
    def __init__(self, name, alter, geschlecht):
        self.name = name
        self.alter = alter
        self.geschlecht = geschlecht
    
    def print(self):
        return "Name: " + self.name + " Alter: " + str(self.alter) + " Geschlecht: " + str(self.geschlecht)
    

class Mitarbeiter (Person):
    def __init__(self, name, alter, gehalt, geschlecht):
        super().__init__(name, alter, geschlecht)
        self.gehalt = gehalt
    
    def __repr__(self) -> str:
        return self.__str__()
    #Wenn ein Mitarbeiter aufgerufen wird aus einer List

    def print(self):
        return super().print() + " Gehalt: " + str(self.gehalt)
    

class Abteilungsleiter (Mitarbeiter):
    def __init__(self, name, alter, gehalt, geschlecht, parkplatz_number):
        super().__init__(name, alter, geschlecht, gehalt)
        self.parkplatz_number = parkplatz_number
    
    def print(self):
        return super().print() + " Parkplatz-Number: " + str(self.parkplatz_number)



if __name__ == "__main__":
    mitarbeiter_a = [
        Mitarbeiter("Patrick", 18, 2005, Gender.Female),
        Mitarbeiter("Marcel", 18, 2005, Gender.Male),
        
    ]
    mitarbeiter_b = [
        Mitarbeiter("Paula", 18, 2005, Gender.Female),
        Mitarbeiter("Timo", 18, 2005, Gender.Male),
        Mitarbeiter("Noah", 18, 2005, Gender.Male)
    ]

    a1 = Abteilungsleiter("Hans", 50, Gender.Male, 2005, 20)
    a2 = Abteilungsleiter("Franzi", 50, Gender.Female, 2005, 20)

    a = Abteilung("Produktion", mitarbeiter_a, a1)
    b = Abteilung("Qualitätsmanagement", mitarbeiter_b, a2)

    firma = Firma("BMW", 2546, [a, b])
    
    #alle Mitarbeiter
    print("Anzahl Mitarbeiter", firma.get_anzahl_Mitarbeiter())
    
    #Die Abteilungsleiter
    for ele in firma.get_abteilungsleiter():
        print("Abteilungsleiter", ele.print())
    
    #alle Abteilungen
    for ele in firma.abteilungen:
        print("Abteilungen", ele.print())
    
    #Die größte Abteilung
    print("Größte Abteilung", firma.get_biggest_department())

    #Quote Frauen, Männer
    dict_quote = firma.quote_Female_Male()
    print(dict_quote)


