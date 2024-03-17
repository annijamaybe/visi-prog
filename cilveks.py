class Cilvēks:
     def __init__(self, vards, vecums, dzimums):
        self.age = vecums
        self.name = vards
        self.sex = dzimums
        self.nauda = 0

     def dzimsanas_diena(self):
        self.age += 1

     def mainit_vardu(self, jaunais_vards):
        self.name = jaunais_vards

     def pastastit_par_sevi(self):
        if self.sex == "s":
            dz ="sieviete"
        elif self.sex == "v":
            dz = "vīrietis"
        else:
            dz = self.sex
        print("Mani sauc {}, man ir {} gadi, es esmu {}, man ir {}$".format(self.name, self.age, dz, self.nauda))

     def nopelnit(self, nopelnita_nauda):
        self.nauda += nopelnita_nauda

     def uztaisit_spamu(self, spama_mape):
        faila_nosaukums = spama_mape + "spams" + self.name + str(self.age) + ".txt"
        if self.sex == "s":
            sveiki_galotne = "a"
            laimets_galotne = "usi"
        elif self.sex == "v":
            sveiki_galotne = "s"
            laimets_galotne = "is"
        else:
            sveiki_galotne = "i"
            laimets_galotne = "is"

        laimets = self.age*35
        teksts = "Sveik{}, {}! Tu esi laimēj{} {}€!".format(sveiki_galotne, self.name, laimets_galotne, laimets)
        with open(faila_nosaukums, "w", encoding="utf-8") as spams:
            spams.write(teksts) 
        self.nopelnit(laimets)
        self.pastastit_par_sevi()
        


persona1 = Cilvēks("Marta", 32, "s")
persona1.pastastit_par_sevi()
persona1.dzimsanas_diena()
persona1.pastastit_par_sevi()
persona1.nopelnit(30)
persona1.pastastit_par_sevi()
persona1.uztaisit_spamu("oop/spams/")

#turpinat = "t"
#Cilveki = []
#while turpinat == "t":
    #vards = input("Ievadiet vārdu")
    #vecums = input("Ievadiet vecumu")
    #dzimums = input("Ievadiet dzimumu (s/v)!")
    #Cilveki.append( Cilvēks(vards, vecums, dzimums))
    #turpinat = input("Ja vēlies pieveinot vēl vienu cilvēku")

#for viens in Cilveki:
    #print(viens.age)


     