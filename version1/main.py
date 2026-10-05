from Admin import Admin
from Ticket import Ticket, tous_les_tickets
from User import User

def main() ->None:

    #menu Principal 
    while True:
        print(" Menu Principal")
        print("\n1.Vous être un Utilisateur ?")
        print("2.Vous être un Administrateur ?")
        print("3.Quitter")
        choix= input("Veuillez entrez une valeur (1-3) : ")

        if choix == '1':
            print("\n Connexion Utilisateur")
            print("Entrez votre nom ")
            #saisie du nom
            name = input("Nom : ")
            print("Entrez votre email ")
            #saisie de l'email
            email= input("Email :")
            print("Entrez votre rôle 'Utilisateur' / 'Developpeur' ")
            #saisie du role
            role=input("Role :")
            #creation d'utilisateur
            currentUser= User(userID=1,name=name,email=email,role=role)
            while True:
                print(f"\nBienvenue {name} dans le menu utilisateur votre id est le #{currentUser.userID}")
                print("Que souhaité vous faire ?")
                print("1.Créé un Ticket ?")
                print("2.Voir un Ticket ?")
                print("3.Mettre a jour un Ticket ?")
                print("4.Retour au menu principal")

                choixuser= input("Veuillez entrez une valeur (1-4) : ")
                if choixuser == '1':
                    print("Veuillez entrez votre Titre")
                    #saisie du titre
                    titre = input("Titre : ")
                    print("Veuillez entrez la description")
                    #saisie de la description
                    desc= input("Description : ")
                    #creation d'un nouveau ticket
                    nouveauTicket=Ticket(ticketID=len(tous_les_tickets)+1,title=titre,description=desc,status="OUVERT",priority="NORMALE")
                    #creation du ticket par l'utilisateur
                    currentUser.createTicket(nouveauTicket)
                    #ajout du ticket dans la liste
                    tous_les_tickets.append(nouveauTicket)
                elif choixuser == '2':
                    if not tous_les_tickets:
                        print("Aucun ticket disponible.")
                    else:
                        #saisie du numero du ticket
                        index= int(input("Numéro du ticket : "))-1
                        #affichage du ticket par l'utilisateur
                        currentUser.viewTicket(tous_les_tickets[index])
                elif choixuser == '3':
                    if not tous_les_tickets:
                        print("Aucun ticket disponible.")
                    else:
                        #saisie du numero du ticket
                        index = int(input("Numero du ticket : "))-1
                        print("Veuillez entrez votre commentaire")
                        #saisie du commentaire
                        comm = input("Commentaire : ")
                        #ajout du commentaire au ticket
                        tous_les_tickets[index].addComment(comm)
                elif choixuser == '4':
                            break

        elif choix == "2":
            print("\nConnexion Administrateur")
            print("Entrez votre nom ")
            #saisie du nom
            name = input("Nom : ")
            print("Entrez votre email ")
            #saisie de l'email
            email= input("Email :")
            #creation d'administrateur
            currentAdmin = Admin(adminID=1, name=name, email=email)
            while True:
                print(f"\nBienvenue {name} dans le menu administrateur votre id est le #{currentAdmin.adminID}")
                print("\n1. Voir tous les tickets")
                print("2. Assigner un ticket")
                print("3. Fermer un ticket")
                print("4. Retour au menu principal")
                #saisie de l'action
                choixadmin = input("Choix : ")

                if choixadmin == "1":
                    #affichage de tout les tickets par l'administrateur
                    currentAdmin.viewAllTickets()

                elif choixadmin == "2":
                    if not tous_les_tickets:
                        print("Aucun ticket disponible.")
                    else:
                        #saisie du numero du ticket a assigner
                        index = int(input("Numéro du ticket à assigner : ")) - 1
                        print("Entrez le nom de l'utilisateur à assigner ")
                        #saisie du nom de l'utilisateur a assigner
                        uname = input("Nom : ")
                        print("Entrez votre email ")
                        #saisie de l'email de l'utilisateur a assigner
                        uemail = input("Email :")
                        print("Entrez votre rôle 'utilisateur' / 'developpeur' ")
                        #saisie du role de l'utilisateur a assigner
                        urole = input("Role :")
                        #creation d'utilisateur a assigner
                        assignedUser = User(userID=2, name=uname, email=uemail, role=urole)
                        #assignation du ticket a l'utilisateur par l'administrateur
                        currentAdmin.assignTicket(tous_les_tickets[index], assignedUser)

                elif choixadmin == "3":
                    if not tous_les_tickets:
                        print("Aucun ticket disponible.")
                    else:
                        #saisie du numero du ticket a fermer
                        index = int(input("Numéro du ticket à fermer : ")) - 1
                        #fermeture du ticket par l'administrateur
                        currentAdmin.closeTicket(tous_les_tickets[index])

                elif choixadmin == "4":
                    break

        elif choix == "3":
            #sortie du programme
            print("Au revoir !")
            break

        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()