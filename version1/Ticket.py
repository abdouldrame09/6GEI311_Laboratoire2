from datetime import date

#liste globale de tout les tickets (externe aux classes)
tous_les_tickets = []

#Classe Ticket
class Ticket():
    def __init__(self,ticketID:int,title:str,description:str,status:str,priority:str):
        self.ticketID=ticketID
        self.title=title
        self.description=description
        self.status=status
        self.priority=priority
        self.creationDate=date.today()
        self.updateDate=date.today()
        

#Fonction pour assigner un ticket a un utilisateur
    def assignTo(self,user):
        self.status="ASSIGNÉ"     #mise a jour du statut
        self.updateDate=date.today()  #mise a jour de la date
        print(f"Le ticket #{self.ticketID} a été assigné à {user.name} ({user.role}).")

#Fonction pour mettre a jour le status d'un ticket
    def updateStatus(self,status):
        self.status=status   #mise a jour du statut
        self.updateDate=date.today() #mise a jour de la date
        print(f"Le statut du ticket #{self.ticketID} à été mise à jour au statut {self.status}")

#Fonction pour ajouter un commentaire  pour la description du ticket
    def addComment(self,comment):
        self.updateDate=date.today()  #mise a jour de la date
        print(f"Commentaire ajouté au ticket #{self.ticketID} : {comment}")