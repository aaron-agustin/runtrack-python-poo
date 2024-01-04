class Student:
    def __init__(self, name, last_name, student_number) -> None:
        self.__name = name
        self.__last_name = last_name
        self.__student_number = student_number
        self.__credit_amount = 0
        self.__level = self.__studentEval()
    
    def add_credits(self,amount):
        if amount > 0:
            self.__credit_amount += amount
            self.__level = self.__studentEval()
        
    def get_name(self):
        return self.__name
    def get_last_name(self):
        return self.__last_name
    def get_student_number(self):
        return self.__student_number
    def get_credit_amount(self):
        return self.__credit_amount
    def get_level(self):
        return self.__level
    
    def afficher_credits(self):
        print(f"Le nombre de crédits de {self.get_name()} {self.get_last_name()} est de {self.get_credit_amount()}")
    def studentInfo(self):
        print(f"Nom = {self.get_last_name()}")
        print(f"Prénom = {self.get_name()}")
        print(f"id = {self.get_student_number()}")
        print(f"Niveau = {self.get_level()}")
    
    def __studentEval(self):
        if self.get_credit_amount() >= 90:
            return "Excellent"
        elif self.get_credit_amount() >= 80:
            return "Très bien"
        elif self.get_credit_amount() >= 70:
            return "Bien"
        elif self.get_credit_amount() >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
            
etudiant = Student("Doe", "Jhon", 145)
etudiant.add_credits(15)
etudiant.afficher_credits()
etudiant.studentInfo()
etudiant.add_credits(20)
etudiant.add_credits(50)
etudiant.studentInfo()