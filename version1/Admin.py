from Ticket import tous_les_tickets

#Classe Administrateur
class Admin():
    def __init__(self,adminID:int,name:str,email:str):
        self.adminID=adminID
        self.name=name
        self.email=email

#Fonction pour assigner un ticket a un utilisateur
    def assignTicket(self,ticket,user)->None:
        ticket.assignTo(user)   #assignation du ticket a l'utilisateur
#Fonction pour fermé un ticket
    def closeTicket(self,ticket)->None:
        ticket.updateStatus("TERMINÉ")   #mise a jour du statut
        print(f"Le ticket #{ticket.ticketID} est maintenant [TERMINÉ]")

#Fonction pour voir tout les tickets
    def viewAllTickets(self)->list:
        for ticket in tous_les_tickets:
            print(f" Ticket #{ticket.ticketID} : '{ticket.title}'  [{ticket.status}]  {ticket.priority} {ticket.updateDate}")
        
        return tous_les_tickets