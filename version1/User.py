from datetime import date
#Classe utilisteur
class User():
    def __init__(self,userID : int ,name:str,email:str,role:str):
        self.userID= userID
        self.name= name
        self.email=email
        self.role=role

#Fonction pour cree un tiket
    def createTicket(self,ticket):
        print(f"L'utilisateur {self.name} ({self.role}) a créé le ticket #{ticket.ticketID} : '{ticket.title}'.")

#Fonction pour voir tout les tickets
    def viewTicket(self,ticket):
         print(f" Ticket #{ticket.ticketID} : '{ticket.title}'  {ticket.status}  {ticket.priority} {ticket.updateDate}")

#Fonction pour mettre a jour un ticket
    def updateTicket(self,ticket):
        ticket.updateDate = date.today()
        print(f"L'utilisateur {self.name} a mis à jour le ticket #{ticket.ticketID}.")