class Personne:
    def __init__(self,nom,age,date):
        self.__nom = nom
        self.__age = age
        self.__date = date
    def Afficher(self):
        print(f"my name is {self.__nom}, and my age is {self.__age} and i born on {self.__date}.")

class Employé(Personne):
    def __init__(self, nom, age, date, salaire):
        super().__init__(nom, age, date)
        self.salaire = salaire
    def Afficher(self):
        return super().Afficher()

class Chef(Employé):
    def __init__(self, nom, age, date, salaire , serviceAccompagné):
        super().__init__(nom, age, date, salaire)
        self.serviceAccompagné = serviceAccompagné
    def Afficher(self):
        return super().Afficher()

class Directeur(Chef):
    def __init__(self, nom, age, date, salaire, serviceAccompagné, sociétéAccompagné):
        super().__init__(nom, age, date, salaire, serviceAccompagné)
        self.sociétéAccompagné = sociétéAccompagné
    def Afficher(self):
        return super().Afficher()
    