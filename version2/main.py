from Developpeur import Developpeur, tousLesDeveloppeurs
from Ticket import Ticket
from User import User
from Statut import Statut
from Priorite import Priorite
from TypeDescription import TypeDescription
from DescriptionFactory import DescriptionFactory
from GestionnaireTickets import GestionnaireTickets

def main() ->None:

    #creation du gestionnaire de tickets
    gestionnaire = GestionnaireTickets()

    #menu Principal 
    while True:
        print(" Menu Principal")
        print("\n1.Vous être un Utilisateur ?")
        print("2.Vous être un Developpeur ?")
        print("3.Quitter")
        #boucle pour verifier le choix
        while True:
            choix = input("Veuillez entrez une valeur (1-3) : ")
            if choix in ['1','2','3']:
                break
            else:
                print("Choix invalide, veuillez recommencer.")

        if choix == '1':
            print("\n Connexion Utilisateur")
            print("Entrez votre nom ")
            #saisie du nom
            name = input("Nom : ")
            print("Entrez votre email ")
            #saisie de l'email
            email = input("Email :")
            #creation d'utilisateur
            currentUser = User(name=name,email=email)
            while True:
                print(f"\nBienvenue {name} dans le menu utilisateur votre id est le #{currentUser.userId}")
                print("Que souhaité vous faire ?")
                print("1.Créé un Ticket ?")
                print("2.Voir un Ticket ?")
                print("3.Mettre a jour un Ticket ?")
                print("4.Retour au menu principal")
                #boucle pour verifier le choix
                while True:
                    choixUser = input("Veuillez entrez une valeur (1-4) : ")
                    if choixUser in ['1','2','3','4']:
                        break
                    else:
                        print("Choix invalide, veuillez recommencer.")

                if choixUser == '1':
                    print("Veuillez entrez votre Titre")
                    #saisie du titre
                    titre = input("Titre : ")
                    print("Veuillez choisir le type de description")
                    print("1.Texte")
                    print("2.Image")
                    print("3.Video")
                    #boucle pour verifier le type de description
                    while True:
                        typeChoix = input("Choix : ")
                        if typeChoix in ['1','2','3']:
                            break
                        else:
                            print("Choix invalide, veuillez recommencer.")
                    if typeChoix == '1':
                        typeDesc = TypeDescription.TEXTE
                        label = "Description"
                    elif typeChoix == '2':
                        typeDesc = TypeDescription.IMAGE
                        label = "Chemin de l'image"
                    else:
                        typeDesc = TypeDescription.VIDEO
                        label = "Chemin de la video"
                    #saisie du contenu ou du chemin
                    contenu = input(f"{label} : ")
                    #creation de la description via la factory
                    description = DescriptionFactory.createDescription(typeDesc,contenu)
                    #creation d'un nouveau ticket
                    nouveauTicket = Ticket(title=titre)
                    #ajout de la description dans le ticket
                    nouveauTicket.addDescription(description)
                    #creation du ticket par l'utilisateur
                    currentUser.createTicket(nouveauTicket)
                    #ajout du ticket dans le gestionnaire
                    gestionnaire.ajouter(nouveauTicket)

                elif choixUser == '2':
                    if not gestionnaire.tous():
                        print("Aucun ticket disponible.")
                    else:
                        #boucle pour verifier le numero du ticket
                        while True:
                            numero = input("Numéro du ticket : ")
                            if numero.isdigit():
                                ticketId = int(numero)
                                ticket = gestionnaire.trouverParId(ticketId)
                                if ticket is not None:
                                    break
                                else:
                                    print("Ticket introuvable, veuillez recommencer.")
                            else:
                                print("Veuillez entrer un nombre valide.")
                        #affichage du ticket par l'utilisateur
                        currentUser.viewTicket(ticket)

                elif choixUser == '3':
                    if not gestionnaire.tous():
                        print("Aucun ticket disponible.")
                    else:
                        #boucle pour verifier le numero du ticket
                        while True:
                            numero = input("Numero du ticket : ")
                            if numero.isdigit():
                                ticketId = int(numero)
                                ticket = gestionnaire.trouverParId(ticketId)
                                if ticket is not None:
                                    break
                                else:
                                    print("Ticket introuvable, veuillez recommencer.")
                            else:
                                print("Veuillez entrer un nombre valide.")
                        print("Veuillez choisir le type de description")
                        print("1.Texte")
                        print("2.Image")
                        print("3.Video")
                        #boucle pour verifier le type de description
                        while True:
                            typeChoix = input("Choix : ")
                            if typeChoix in ['1','2','3']:
                                break
                            else:
                                print("Choix invalide, veuillez recommencer.")
                        if typeChoix == '1':
                            typeDesc = TypeDescription.TEXTE
                        elif typeChoix == '2':
                            typeDesc = TypeDescription.IMAGE
                        else:
                            typeDesc = TypeDescription.VIDEO
                        #saisie du contenu ou du chemin
                        contenu = input("Contenu ou chemin : ")
                        #creation de la description via la factory
                        nouvelleDesc = DescriptionFactory.createDescription(typeDesc,contenu)
                        #ajout de la description dans le ticket
                        ticket.addDescription(nouvelleDesc)
                        #mise a jour du ticket par l'utilisateur
                        currentUser.updateTicket(ticket)

                elif choixUser == '4':
                    break

        elif choix == "2":
            print("\nConnexion Developpeur")
            print("Entrez votre nom ")
            #saisie du nom
            name = input("Nom : ")
            print("Entrez votre email ")
            #saisie de l'email
            email = input("Email :")
            #creation de developpeur
            currentDev = Developpeur(name=name,email=email)
            while True:
                print(f"\nBienvenue {name} dans le menu developpeur votre id est le #{currentDev.userId}")
                print("\n1. Voir tous les tickets")
                print("2. Assigner un ticket")
                print("3. Valider un ticket")
                print("4. Fermer un ticket")
                print("5. Retour au menu principal")
                #boucle pour verifier le choix
                while True:
                    choixDev = input("Choix : ")
                    if choixDev in ['1','2','3','4','5']:
                        break
                    else:
                        print("Choix invalide, veuillez recommencer.")

                if choixDev == "1":
                    #affichage de tout les tickets par le developpeur
                    currentDev.viewAllTickets(gestionnaire)

                elif choixDev == "2":
                    if not gestionnaire.tous():
                        print("Aucun ticket disponible.")
                    else:
                        #boucle pour verifier le numero du ticket
                        while True:
                            numero = input("Numéro du ticket à assigner : ")
                            if numero.isdigit():
                                ticketId = int(numero)
                                ticket = gestionnaire.trouverParId(ticketId)
                                if ticket is not None:
                                    break
                                else:
                                    print("Ticket introuvable, veuillez recommencer.")
                            else:
                                print("Veuillez entrer un nombre valide.")
                        #affichage de la liste des developpeurs disponibles
                        if not tousLesDeveloppeurs:
                            print("Aucun developpeur enregistré.")
                        else:
                            print("\nDeveloppeurs disponibles :")
                            for d in tousLesDeveloppeurs:
                                print(f"  #{d.userId} - {d.name} ({d.email})")
                            #boucle pour verifier l'id du developpeur a assigner
                            while True:
                                numero = input("ID du developpeur à assigner : ")
                                if numero.isdigit():
                                    devId = int(numero)
                                    assignedDev = None
                                    for d in tousLesDeveloppeurs:
                                        if d.userId == devId:
                                            assignedDev = d
                                            break
                                    if assignedDev is not None:
                                        break
                                    else:
                                        print("Developpeur introuvable, veuillez recommencer.")
                                else:
                                    print("Veuillez entrer un nombre valide.")
                            #assignation du ticket au developpeur par le developpeur
                            currentDev.assignTicket(ticket,assignedDev)

                elif choixDev == "3":
                    if not gestionnaire.tous():
                        print("Aucun ticket disponible.")
                    else:
                        #boucle pour verifier le numero du ticket
                        while True:
                            numero = input("Numéro du ticket à valider : ")
                            if numero.isdigit():
                                ticketId = int(numero)
                                ticket = gestionnaire.trouverParId(ticketId)
                                if ticket is not None:
                                    break
                                else:
                                    print("Ticket introuvable, veuillez recommencer.")
                            else:
                                print("Veuillez entrer un nombre valide.")
                        #validation du ticket par le developpeur
                        currentDev.validateTicket(ticket)

                elif choixDev == "4":
                    if not gestionnaire.tous():
                        print("Aucun ticket disponible.")
                    else:
                        #boucle pour verifier le numero du ticket
                        while True:
                            numero = input("Numéro du ticket à fermer : ")
                            if numero.isdigit():
                                ticketId = int(numero)
                                ticket = gestionnaire.trouverParId(ticketId)
                                if ticket is not None:
                                    break
                                else:
                                    print("Ticket introuvable, veuillez recommencer.")
                            else:
                                print("Veuillez entrer un nombre valide.")
                        #fermeture du ticket par le developpeur
                        currentDev.closeTicket(ticket)

                elif choixDev == "5":
                    break

        elif choix == "3":
            #sortie du programme
            print("Au revoir !")
            break

if __name__ == "__main__":
    main()