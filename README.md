# 6GEI311 – Lab 2 : Système de Gestion de Tickets

Abdramane Dramé (DRAA04070300)

Ce dépôt contient le travail du Lab 2 pour le cours 6GEI311 – Architecture des logiciels.

---

## 1. Installation et utilisation

### Installation

Il faut juste **Python 3.8 ou plus récent**.

bash
git clone https://github.com/abdouldrame09/6GEI311-Lab2-SOL.git
cd 6GEI311-Lab2-SOL

## Utilisation


bash
cd version2
python main.py

Le programme propose un menu pour :

Utilisateur : créer, voir et modifier des tickets.



Développeur : voir, assigner, valider et fermer des tickets.



Contenu du dépôt :

version1/ : code de la partie 1

version2/ : code de la partie 2

DiagrammeUML.png : diagramme de classes final

codeplantuml.txt : code PlantUML

Rapport lab2.pdf : rapport complet

## 2. Ce que j'ai appris

Ce lab m'a permis de comprendre l'importance de bien analyser l'énoncé avant de concevoir un diagramme.

J'ai appliqué les principes GRASP :

Expert en information : placer chaque responsabilité dans la bonne classe.

Fabrication pure : créer des classes utilitaires (DescriptionFactory, GestionnaireTickets).

Faible couplage : éviter les dépendances directes entre classes.

Indirection : utiliser un intermédiaire pour accéder aux tickets.

Protégé des variations : utiliser des énumérations et le polymorphisme.

Forte cohésion : une classe = une responsabilité claire.

J'ai aussi appris à utiliser le polymorphisme pour gérer plusieurs types de descriptions (texte, image, vidéo) de manière uniforme.

## 3. Résultats


### 3.1 Fonctionnalités

-Création de tickets (texte, image, vidéo)	
-Affichage des tickets et descriptions	
-Assignation à un développeur	
-Validation et fermeture	
-Vérification des entrées	

### 3.2 Diagramme UML — Partie 1
  
Diagramme initial avec plusieurs problèmes : classe Admin incohérente, god class Ticket, méthodes vides, types inadaptés.

<img width="951" height="703" alt="diagramme_partie1" src="https://github.com/user-attachments/assets/e80a6888-2ffb-4490-894b-9e73c10ab7a7" />
  

### 3.3 Diagramme UML — Partie 2
Diagramme final avec :
Héritage Developpeur → User
Classe abstraite DescriptionTicket + sous-classes
DescriptionFactory et GestionnaireTickets
Enums Statut, Priorite, TypeDescription
Voir DiagrammeUML.png et codeplantuml.txt.
<img width="1446" height="1334" alt="DiagrammeUML" src="https://github.com/user-attachments/assets/b6ab1d9a-3310-48f4-ab8f-41c8aede6b7d" />


### Captures d'écran

https://captures/menu_principal.png
https://captures/creation_ticket.png
https://captures/voir_tickets.png
https://captures/assignation.png

Abdramane Dramé – abdouldrame09
