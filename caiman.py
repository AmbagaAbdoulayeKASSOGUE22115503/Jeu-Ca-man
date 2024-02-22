#### REPRESENTATION DES DONNEES
###initialisation de la grille et autres variables de jeu

#### REPRESENTATION GRAPHIQUE
### fonction affichage
def afficher_grille(grille):
    print('    ' + '+-----+-----+-----+-----+-----+-----+-----+-----+')
    valeur_ligne = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    print(' ' + ' ' + '  | ' + ' 1 ' + ' | ' + ' 2 ' + ' | ' + ' 3 ' + ' | ' + ' 4 ' + ' | ' + ' 5 ' + ' | ' + ' 6 ' + ' | ' + ' 7 ' + ' | ' + ' 8 ' + ' | ')
    print('----+-----+-----+-----+-----+-----+-----+-----+-----+')
    for i in range(len(grille)):
        print(valeur_ligne[i], "  |  ", end= '')
        for j in range(len(grille[0])):
            print(grille[i][j], " |  ", end='')
        print()
        print('----+-----+-----+-----+-----+-----+-----+-----+-----+')
    return ' '



# =====================================================================================================================#
# verification dans grille
def est_dans_grille(grille,message):
    if ( 0<=ord(message[0])-65<len(grille) and 0<=ord(message[1])-49<len(grille[0]) ):
        return True
    return False
# ======================================================================================================================#

## vérification de "est au bon format"
def est_au_bon_format(message):
    if len(message)!=2 :
        return False
    lettre = message[0]
    chiffre = message[1]
    if ord(lettre) not in range(65,91) and ord(lettre) not in range(97,123) :
        return False
    if ord(chiffre) not in range(48,58) :
        return False
    return True



# =====================================================================================================================#
###vérification de si la case est vide
def case_vide(grille, message):
    ligne = ord(message[0])-65   #####cette valeur vaut un réel######
    colonne = ord(message[1])-49
    if grille[ligne][colonne] != ' ':
        return False
    return True


####===================================================================================================================##
####fonction qui vérifie que le pion est jaune pour le jeu de saisie de coordonnées initialles#########
def pion_jaune(grille, message):
    ligne = ord(message[0]) - 65
    colonne = ord(message[1]) - 49
    if grille[ligne][colonne]=='♥':
        return True
    return False

######===fonction qui renvoie les coordonnées de la case intermédiare========================================================================================================================##
def coordonnee_case_precedente(grille, coordonnee_case_depart, coordonnee_case_arrivee):
    ligne_depart,colonne_depart= ord(coordonnee_case_depart[0])-65,ord(coordonnee_case_depart[1])-49
    ligne_arrivee,colonne_arrivee= ord(coordonnee_case_arrivee[0])-65,ord(coordonnee_case_arrivee[1])-49
    liste_case_arrivee = [(ligne_depart, colonne_depart + 2), (ligne_depart, colonne_depart - 2), (ligne_depart + 2, colonne_depart), (ligne_depart - 2,colonne_depart), (ligne_depart - 2, colonne_depart- 2), (ligne_depart+ 2, colonne_depart+ 2), (ligne_depart + 2, colonne_depart - 2),(ligne_depart- 2, colonne_depart + 2)]
    liste_case_intermediare= [(ligne_depart, colonne_depart + 1), (ligne_depart, colonne_depart - 1), (ligne_depart + 1, colonne_depart), (ligne_depart - 1,colonne_depart), (ligne_depart - 1, colonne_depart- 1), (ligne_depart+ 1, colonne_depart+ 1), (ligne_depart + 1, colonne_depart - 1),(ligne_depart- 1, colonne_depart + 1)]
    indice= 0
    for t,p in liste_case_arrivee:
        if est_dans_grille(grille,chr(t+65)+chr(p+49)) and t==ligne_arrivee and p==colonne_arrivee and case_vide(grille,chr(t+65)+chr(p+49)):
            intermediare= liste_case_intermediare[indice]
            ligne_intermediare,colonne_intermediare= chr(intermediare[0]+65),chr(intermediare[1]+49)
            if not case_vide(grille,ligne_intermediare+colonne_intermediare):
                return ligne_intermediare+colonne_intermediare
        indice+=1
    return ' '

#=======verification de déplacement simple pour distance=================================================================================================================##
def verif_deplacement_simple(grille, coordonnee_case_depart, coordonnee_case_arrivee):
    ligne_depart, colonne_depart = ord(coordonnee_case_depart[0]) - 65, ord(coordonnee_case_depart[1]) - 49
    ligne_arrivee, colonne_arrivee = ord(coordonnee_case_arrivee[0]) - 65, ord(coordonnee_case_arrivee[1]) - 49
    liste_possible_case_arrivee = [(ligne_depart, colonne_depart + 1), (ligne_depart, colonne_depart - 1),(ligne_depart + 1, colonne_depart), (ligne_depart - 1, colonne_depart),(ligne_depart - 1, colonne_depart - 1), (ligne_depart + 1, colonne_depart + 1),(ligne_depart + 1, colonne_depart - 1), (ligne_depart - 1, colonne_depart + 1)]
    for t,p in liste_possible_case_arrivee:
        if est_dans_grille(grille,chr(t+65)+chr(p+49)) and  case_vide(grille,chr(t+65)+chr(p+49)) and t==ligne_arrivee and p==colonne_arrivee:
            return True
    return False

####fonction qui verifie la distance entre la case d'arrivée et la vase de depart et verifie un booleen en tenant compte de la direction################################
def distance_valide(grille, coordonnee_case_depart, coordonnee_case_arrivee) :
    coordonnees_intermediares= coordonnee_case_precedente(grille, coordonnee_case_depart, coordonnee_case_arrivee)
    if coordonnees_intermediares!=' ' or verif_deplacement_simple(grille, coordonnee_case_depart, coordonnee_case_arrivee):
        return True
    return False
#===================================================================================================================================#
####fonction qui calcul le nombre de pion pion jaune pour l'arrêt de la boucle#######################
def nb_pion_est_valide(grille):
    NB_pion = 0
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j]!=' ':
                NB_pion+= 1
    if NB_pion>1:
        return True
    else:
        return False

##########=====fonction qui vérifie la possibilité d'enchaînement==================================================================================================#######
def enchainement_possible(grille,coordonnees_case_depart):
    i,j=ord(coordonnees_case_depart[0])-65,ord(coordonnees_case_depart[1])-49
    liste_poosible_enchainement= liste = [(i, j + 2), (i, j - 2), (i + 2, j), (i - 2, j), (i - 2, j - 2), (i + 2, j + 2), (i + 2, j - 2),(i - 2, j + 2)]
    for t,p in liste_poosible_enchainement:
        coordonnees_case_arrivee= chr(t+65)+chr(p+49)
        coordonnees_intermediares= coordonnee_case_precedente(grille, coordonnees_case_depart, coordonnees_case_arrivee)
        if coordonnees_intermediares!=' ':
            return coordonnees_case_arrivee
    return ' '

####=======fonction qui va tout simplement être utilisée qu'une fois dans la fonction qui va suivre pour pouvoir verifier et retourner les coordonnées d'arrivées de deplacement simple===================##
def saut_possible_sans_capture(grille):
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j] == '♥':
                liste_secondaire=[(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j), (i - 1, j - 1), (i + 1, j + 1), (i + 1, j - 1),(i - 1, j + 1)]  ##Va à chaque fois contenir les priorité sescondaire##
                for t,p in liste_secondaire:
                    if distance_valide(grille, chr(i + 65) + chr(j + 49), chr(t + 65) + chr(p + 49)):
                        return chr(i+65)+chr(j+49),chr(t+65)+chr(p+49)
    return ' '

######fonction qui parcours tout le plateau et vérifie s'il existe un pion jaune qui peut se deplacer et on renvoie ses coordonnées######"
def saut_possible_pion_jaune(grille):
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j]=='♥':
                liste_prioritaire = [(i, j + 2), (i, j - 2), (i + 2, j), (i - 2, j), (i - 2, j - 2), (i + 2, j + 2), (i + 2, j - 2),(i - 2, j + 2)]  ###on joue sur la priorité de capture###
                for t, p in liste_prioritaire:
                    if distance_valide(grille, chr(i + 65) + chr(j + 49), chr(t + 65) + chr(p + 49)):
                        return chr(i+65)+chr(j+49),chr(t+65)+chr(p+49)
    return saut_possible_sans_capture(grille)

####==============================================================================================================================================####
########fonction qui applique le deplacement et retourne la grille modifiée#####################################################################
def appliquer_deplacement(grille, coordonnee_case_depart, coordonnee_case_arrivee):
    CSI = "\x1B["
    case_precedente = coordonnee_case_precedente(grille, coordonnee_case_depart, coordonnee_case_arrivee)   ######on commence par bien initialiser nos coordonnées de depart et nos coordonnés d'arrivées#############
    ligne_depart,colonne_depart = ord(coordonnee_case_depart[0])-65,ord(coordonnee_case_depart[1])-49
    ligne_arrivee, colonne_arrivee= ord(coordonnee_case_arrivee[0]) - 65,ord(coordonnee_case_arrivee[1]) - 49
    pion=' '    ##pour bien calculer le score, on va identifier de quel pion s'agit-il pour calculer sa valeur########
    if case_precedente != ' ':                                                      #######s'il ya eu capture , on enlève dans la grille le pion capturer########
        ligne_case_precedente,colonne_case_precedente = ord(case_precedente[0]) - 65,ord(case_precedente[1]) - 49
        pion = grille[ligne_case_precedente][colonne_case_precedente]
        grille[ligne_case_precedente][colonne_case_precedente] = ' '
    grille[ligne_arrivee][colonne_arrivee] = CSI + "31;31m" + "♥" + CSI + "0m"     ####ensuite on deplace le pion vers le coordonnées d'arrivée qui est toujours un pion jaune en mettant la couleur jaune pour amméliorer la visibilité#########
    grille[ligne_depart][colonne_depart] = ' '
    valeur_pion = 0
    if pion=='♥':
        valeur_pion  = 1
    elif pion=='♣':
        valeur_pion  = 3
    elif pion=='♦':
        valeur_pion = 2
    return grille, valeur_pion                                                   #####et on renvoie la nouvelle grille et le score obtenu lors du cours du jeu############


#=====================================================================================================================####
def demander_arreter_jeu():
    CSI = "\x1B["
    choix= str(input((CSI + "36;36m" + "☺ SOUHAITEZ-VOUS ABANDONNER LA PARTIE (OUI ou NON ): " + CSI+ "0m" )))
    while ( choix!='OUI' and choix!='NON'):
        choix = str(input((CSI + "30;41m" + "Vous devez saisir l'un des touches suivants: (OUI ou NON): " + CSI + "0m")))

    return choix


###LA FONCTION QUI SAISIE LES COORDONNÉES DE LA CASE DE DEPART========================================================##
def saisir_coordonnees_case_depart(grille):
    CSI = "\x1B["
    ligne=str(input(CSI + "35;35m" + "Saisir la ligne:" + CSI + "0m"))
    colonne = str(input(CSI + "35;35m" + "Saisir la colonne:" + CSI + "0m"))
    message=ligne + colonne
    while not ( est_au_bon_format(message) and est_dans_grille(grille,message) and pion_jaune(grille, message) ):
            print(CSI + "30;41m" + "⚠️ LES COORDONNÉES DE LA CASE DE DEPART NE SONT PAS VALIDE, VEUILLEZ LES RESSAISIR" + CSI + "0m")
            ligne = str(input(CSI + "35;35m" + "Saisir la ligne:" + CSI + "0m"))
            colonne = str(input(CSI + "35;35m" + "Saisir la colonne:" + CSI + "0m"))
            message = ligne + colonne

    if est_au_bon_format(message) and est_dans_grille(grille,message) and pion_jaune(grille, message):
        print(CSI + "35;35m" + "LES COORDONNÉES DE LA CASE DE DEPART SONT VALIDES; VOILA LES COORDONNÉES:" + CSI + "0m",message)
        return message

####============================================================================================================================================#####
####=====LA FONCTION QUI SAISIE LES COORDONNÉES DE LA CASE D'ARRIVÉE==================================================##
def saisir_coordonnees_case_arrivee(grille, coordonnee_case_depart):
    CSI = "\x1B["
    ligne = str(input(CSI + "35;35m" + "Saisir la ligne:" + CSI + "0m"))
    colonne = str(input(CSI + "35;35m" + "Saisir la colonne:" + CSI + "0m"))
    message = ligne + colonne
    while not ( est_au_bon_format(message) and est_dans_grille(grille,message) and case_vide(grille, message) and distance_valide(grille ,coordonnee_case_depart, message ) ):
        print(CSI + "30;41m" + "⚠️ LES COORDONNÉES DE LA CASE D'ARRIVÉE NE SONT PAS VALIDE, VEUILLEZ LES RESSAISIR" + CSI + "0m")
        ligne = str(input(CSI + "35;35m" + "Saisir la ligne:" + CSI + "0m"))
        colonne = str(input(CSI + "35;35m" + "Saisir la colonne:" + CSI + "0m"))
        message = ligne + colonne
    if ( est_au_bon_format(message) and est_dans_grille(grille,message) and case_vide(grille,message) and distance_valide(grille, coordonnee_case_depart, message) ):
        print(CSI + "35;35m" + "LES COORDONNÉES DE LA CASE D'ARRIVÉES SONT VALIDES; VOILA LES COORDONNÉES:" + CSI + "0m",message)
        return message


#####FONCTION QUI DECLARE LE GAGNANT###########################################################################################
def declarer_gagant(grille, score1, score2, joueur1, joueur2, joueur,choix):
    CSI = "\x1B["
    if choix=='OUI':
        if joueur==joueur1:
            print(CSI + "34;34m" + "LE JOUEUR " + CSI + "0m", joueur2, CSI + "34;34m" + "A GAGNÉ " + CSI + "0m")
            return ' '
        elif joueur==joueur2:
            print(CSI + "34;34m" + "LE JOUEUR " + CSI + "0m", joueur1, CSI + "34;34m" + "A GAGNÉ " + CSI + "0m")
            return ' '
    valeur_pion_restant_sur_plateau = 0
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j] == '♥':
                valeur_pion_restant_sur_plateau += 1
            if grille[i][j] == '♦':
                valeur_pion_restant_sur_plateau += 2
            if grille[i][j] == '♣':
                valeur_pion_restant_sur_plateau += 3
    if joueur == joueur2:
        score1 -= valeur_pion_restant_sur_plateau
    elif joueur == joueur1:
        score2 -= valeur_pion_restant_sur_plateau
    if score1 > score2:
        print(CSI + "34;34m" + "LE JOUEUR "+ CSI + "0m",joueur1, CSI + "34;34m" + "A GAGNÉ "+ CSI + "0m")
    elif score1 < score2:
        print(CSI + "34;34m" + "LE JOUEUR "+ CSI + "0m",joueur2, CSI + "34;34m" + "A GAGNÉ "+ CSI + "0m")
    return ' '
#####FONCTION JOUEUR CONTRE JOUEUR ###############################################################################################

def joueur_contre_joueur(grille):
    CSI = "\x1B["
    joueur = '1'
    score_joueur1 = 0
    score_joueur2 = 0
    afficher_grille(grille)
    while saut_possible_pion_jaune(grille)!=' ' and nb_pion_est_valide(grille):
        print(CSI + "33;33m" + "joueur" + CSI + "0m",joueur,CSI + "33;33m" + "joue!" + CSI + "0m")
        choix_continuer= demander_arreter_jeu()
        if  choix_continuer== 'OUI':
            break
        print(CSI + "35;35m" + "☺ VEUILLEZ SAISIR LES COORDONNÉES DE LA CASE DE DEPART" + CSI + "0m")
        coordonnee_case_depart = saisir_coordonnees_case_depart(grille)
        print(CSI + "35;35m" + "☺ VEUILLEZ SAISIR LES COORDONNÉES DE LA CASE D'ARRIVÉE" + CSI + "0m")
        coordonnee_case_arrivee = saisir_coordonnees_case_arrivee(grille, coordonnee_case_depart)
        grille, valeur_pion = appliquer_deplacement(grille, coordonnee_case_depart, coordonnee_case_arrivee)
        if joueur== '1':
            score_joueur1+= valeur_pion
        elif joueur=='2':
            score_joueur2+= valeur_pion
        while enchainement_possible(grille,coordonnee_case_arrivee)!=' ' and valeur_pion!=0 : #####car pour enchaîner, il faut avoir capturer au préalable##########"
            afficher_grille(grille)
            grille[ord(coordonnee_case_arrivee[0])-65][ord(coordonnee_case_arrivee[1]) - 49] = '♥' ###pour la visibilité dans la case; je remets en couleur blache le pion precedemment choisit par le joueur##
            print(CSI + "31;31m" + "☻ IL Y A POSSIBILITÉ D'ENCHAÎNEMENT; JOUEUR" + CSI + "0m", joueur,CSI + "31;31m" + "JOUE!. TU VEUX ENCHAÎNER VERS QUELLE CASE?" + CSI + "0m")
            print(CSI + "35;35m" + "☺ SAISIR LES COORDONNÉES DE LA CASE D'ARRIVÉE" + CSI + "0m")
            coordonnee_case_depart = coordonnee_case_arrivee
            coordonnee_case_arrivee = saisir_coordonnees_case_arrivee(grille, coordonnee_case_depart)
            grille, valeur_pion = appliquer_deplacement(grille, coordonnee_case_depart, coordonnee_case_arrivee)

            if joueur == '1':
                score_joueur1 += valeur_pion
            elif joueur == '2':
                score_joueur2 += valeur_pion
        afficher_grille(grille)
        grille[ord(coordonnee_case_arrivee[0])-65][ord(coordonnee_case_arrivee[1]) - 49] = '♥'
        if joueur == '1':
            print("SCORE_JOUEUR_1=", score_joueur1)
            joueur = '2'
            print()
        elif joueur == '2':
            print("SCORE_JOUEUR_2=", score_joueur2)
            joueur = '1'
            print()


    print(CSI + "30;31m" + "☻ LE JEU EST TERMINÉ" + CSI + "0m")
    print()
    declarer_gagant(grille, score_joueur1, score_joueur2, '1', '2', joueur,choix_continuer)
######fonction joueur contre ordinateur#################################################################################

def joueur_contre_ordinateur(grille):
    CSI = "\x1B["
    joueur_courant = 'joueur'
    score_joueur = 0
    score_ordinateur = 0
    afficher_grille(grille)
    while saut_possible_pion_jaune(grille)!=' ' and nb_pion_est_valide(grille):
        if joueur_courant== 'joueur':
            print(CSI + "33;33m" + "C'est à votre tour de jouer joueur!" + CSI + "0m")
            choix_continuer = demander_arreter_jeu()
            if choix_continuer == 'OUI':
                break
            print(CSI + "35;35m" + "☺ VEUILLEZ SAISIR LES COORDONNÉES DE LA CASE DE DEPART" + CSI + "0m")
            coordonnee_case_depart = saisir_coordonnees_case_depart(grille)
            print(CSI + "35;35m" + "☺ VEUILLEZ SAISIR LES COORDONNÉES DE LA CASE D'ARRIVÉE" + CSI + "0m")
            coordonnee_case_arrivee = saisir_coordonnees_case_arrivee(grille, coordonnee_case_depart)
            grille, valeur_pion = appliquer_deplacement(grille, coordonnee_case_depart, coordonnee_case_arrivee)
            score_joueur += valeur_pion
            while enchainement_possible(grille,coordonnee_case_arrivee)!=' ' and valeur_pion != 0:
                afficher_grille(grille)
                grille[ord(coordonnee_case_arrivee[0])-65][ord(coordonnee_case_arrivee[1]) - 49] = '♥'
                print(CSI + "31;31m" + "☻ IL Y A POSSIBILITÉ D'ENCHAÎNEMENT JOUEUR; TU VEUX ENCHAÎNER VERS QUELLE CASE?" + CSI + "0m")
                coordonnee_case_depart = coordonnee_case_arrivee
                coordonnee_case_arrivee = saisir_coordonnees_case_arrivee(grille, coordonnee_case_depart)
                grille, valeur_pion = appliquer_deplacement(grille, coordonnee_case_depart,coordonnee_case_arrivee)
                score_joueur += valeur_pion
            joueur_courant ='ORDINATEUR'
            afficher_grille(grille)
            grille[ord(coordonnee_case_arrivee[0])-65][ord(coordonnee_case_arrivee[1]) - 49] = '♥'
            print("SCORE_JOUEUR=",score_joueur)
            print()
        elif joueur_courant=='ORDINATEUR':
            print()
            print(CSI + "33;33m" + "L'ORDINATEUR EST ENTRAIN DE JOUER...." + CSI + "0m")
            coordonnees= saut_possible_pion_jaune(grille)
            coordonnee_case_depart = coordonnees[0]
            coordonnee_case_arrivee = coordonnees[1]
            grille, valeur_pion= appliquer_deplacement(grille, coordonnee_case_depart, coordonnee_case_arrivee)
            score_ordinateur+= valeur_pion
            afficher_grille(grille)
            grille[ord(coordonnee_case_arrivee[0])-65][ord(coordonnee_case_arrivee[1]) - 49] = '♥'
            print(CSI + "33;33m" + "L'ordinateur a joué de la case " + CSI + "0m",coordonnee_case_depart, CSI + "33;33m" + "vers la case " + CSI + "0m",coordonnee_case_arrivee)
            while enchainement_possible(grille,coordonnee_case_arrivee)!=' ' and valeur_pion != 0:
                grille[ord(coordonnee_case_arrivee[0])-65][ord(coordonnee_case_arrivee[1]) - 49] = '♥'
                coordonnee_case_depart = coordonnee_case_arrivee
                coordonnee_case_arrivee= enchainement_possible(grille,coordonnee_case_arrivee)
                grille, valeur_pion = appliquer_deplacement(grille,coordonnee_case_depart, coordonnee_case_arrivee)
                score_ordinateur += valeur_pion
                print()
                afficher_grille(grille)
                grille[ord(coordonnee_case_arrivee[0])-65][ord(coordonnee_case_arrivee[1]) - 49] = '♥'
                print(CSI + "33;33m" + "L'ordinateur a joué de la case " + CSI + "0m",coordonnee_case_depart,CSI + "33;33m" + "vers la case " + CSI + "0m",coordonnee_case_arrivee)
            print(" SCORE_ORDINATEUR=", score_ordinateur)
            print()
            joueur_courant = 'joueur'
    declarer_gagant(grille, score_joueur, score_ordinateur, 'joueur', 'ORDINATEUR', joueur_courant,choix_continuer)
    return ' '
######FONCTION GENERALE DE TEST####################################################################################
def test_fonction_unitaire():
    ###############POUR EST_DANS_GRILLLE#############################"""
    assert not est_dans_grille([[' ','♦','♥','☺'],['☺',' ','♥','♦'],[' ','♦','♦','♥'],[' ','☺','☺','♥'],['♦','☺','♥','♥'],['♦','♦','♦','♦']],'&2'), "Erreur symbole"
    assert not est_dans_grille([[' ','♦','♥','☺'],['☺',' ','♥','♦'],[' ','♦','♦','♥'],[' ','☺','☺','♥'],['♦','☺','♥','♥'],['♦','♦','♦','♦']],'A0'), " Erreur valeur inferieur"
    assert not est_dans_grille([[' ','♦','♥','☺'],['☺',' ','♥','♦'],[' ','♦','♦','♥'],[' ','☺','☺','♥'],['♦','☺','♥','♥'],['♦','♦','♦','♦']],"X1"), "Erreur valeur superieur"
    assert est_dans_grille([[' ','♦','♥','☺'],['☺',' ','♥','♦'],[' ','♦','♦','♥'],[' ','☺','☺','♥'],['♦','☺','♥','♥'],['♦','♦','♦','♦']],"B2"), "Erreur code"
    #####################POUR EST_AU_FORMAT########################
    assert not est_au_bon_format('AA1') ,"Erreur longeur"
    assert not est_au_bon_format('&1'), "Erreurn symbole"
    assert not est_au_bon_format('11'), "Erreur caractère"
    assert not est_au_bon_format('DD'), "Erreur caractère"
    assert est_au_bon_format('A4') , "Erreur code"
    ########################POUR CASE_VIDE###########################################
    assert case_vide([['A',' ','Z'],['B','A',' '],['B','Z','A'],['A','Z','B'],[' ','B','A']], 'A2'), "ERREUR code"
    assert not case_vide([['A',' ','Z'],['B','A',' '],['B','Z','A'],['A','Z','B'],[' ','B','A']], 'B1') , "Erreur1 case non vide"
    assert not case_vide([['A',' ','Z'],['B','A',' '],['B','Z','A'],['A','Z','B'],[' ','B','A']], 'E3'), "Erreur2 case non vide"
    ############################POUR PION_JAUNE##########################################################
    assert not pion_jaune([[' ','♦','♥','☺'],['☺',' ','♥','♦'],[' ','♦','♦','♥'],[' ','☺','☺','♥'],['♦','☺','♥','♥'],['♦','♦','♦','♦']], 'A1'), "Erreur pion est vide"
    assert not pion_jaune([[' ','♦','♥','☺'],['☺',' ','♥','♦'],[' ','♦','♦','♥'],[' ','☺','☺','♥'],['♦','☺','♥','♥'],['♦','♦','♦','♦']], 'B4'), "Erreur pion n'est pas jaune"
    assert pion_jaune([[' ','♦','♥','☺'],['☺',' ','♥','♦'],[' ','♦','♦','♥'],[' ','☺','☺','♥'],['♦','☺','♥','♥'],['♦','♦','♦','♦']], 'C4'), "Erreur pion est jaune"
    assert not pion_jaune([['A', ' ', 'Z'], ['B', 'A', ' '], ['B', 'Z', 'A'], ['A', 'Z', 'B'], [' ', 'B', 'A']],'B1'), "Erreur pion n'est pas dans la grille"
    #####################################POUR DISTANCE VALIDE###########################################################################################################
    #assert not distance_valide([[' ','♦','♥','☺'],['☺',' ','♥','♦'],[' ','♦','♦','♥'],[' ','☺','☺','♥'],['♦','☺','♥','♥'],['♦','♦','♦','♦']], 'D4','A1'), "Erreur distance colonne très longue"
    assert not distance_valide([[' ', '♦', '♥', '☺'], ['☺', ' ', '♥', '♦'], [' ', '♦', '♦', '♥'], [' ', '☺', '☺', '♥'], ['♦', '☺', '♥', '♥'],['♦', '♦', '♦', '♦']], 'F4', 'A1'), "Erreur pion de depart hors de grille"
    assert not distance_valide([[' ', '♦', '♥', '☺'], ['☺', ' ', '♥', '♦'], [' ', '♦', '♦', '♥'], [' ', '☺', '☺', '♥'], ['♥', '☺', '♥', '♥'],['♦', '♦', '♦', '♦']], 'E1', 'C1'), "Erreur case precedente de la ligne d'arrivée est vide"
    assert  distance_valide([[' ', '♦', '♥', '☺'],['☺', ' ', '♥', '♦'],['♦', '☺', '♥', '♥'],['♦', '♦', '♦', '♦']], 'C1', 'A1'), "Erreur code car case qui precede la case d'arrivee est vide"
    ###########POUR TERMINER LE JEU( SAUT POSSIBLE AVEC PION JAUNE) ################################################################################################################################################
    assert saut_possible_pion_jaune([[' ', '♦', '♥', '☺'],['☺', ' ', '♥', '♦'],[' ', '♦', '♦', '♥'],[' ', '☺', '☺', '♥'],['♦', '☺', '♥', '♥'],['♦', '♦', '♦', '♦']])!=' ' ," Erreur code ici le saut est possible"
    assert saut_possible_pion_jaune([['☺', '♦', '♥', '☺'], ['☺', '☺', '♥', '♦'], ['☺', '♦', '♦', '♥'], ['☺', '☺', '☺', '♥'], ['♦', '☺', '♥', '♥'],['♦', '♦', '♦', '♦']])==' ', "Erreur ici un pion jaune ne peu plus se deplacer"
    ###################POUR TERMINER LE JEU( NOMBRE DE PION JAUNE)###############################################################################################################################
    assert not nb_pion_est_valide([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', '♥', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ']]) ,"Erreur y a qu'un pion sur ce plateau"
    assert nb_pion_est_valide([[' ', '♦', '♥', '☺'], ['☺', ' ', '♥', '♦'], [' ', '♦', '♦', '♥'], [' ', '☺', '☺', '♥'], ['♦', '☺', '♥', '♥'],['♦', '♦', '♦', '♦']]) , "Erreur le nombre de pion est superieur à 1"
    print("LE TEST EST OK!")
    return  ' '

def pions_du_jeu():
    pion_jaune= "♥"
    pion_rouge= "♦"
    pion_noire= "♣"

def menu_de_jeu_caiman():
    CSI = "\x1B["
    reset = CSI + "m"
    print(CSI + "30;43m" + "BIENVENUE DANS LE JEU DE CAÏMAN!☻☻☻" + CSI + "0m")
    print("...")
    test = str(input(CSI + "34;34m" + "SI VOUS VOULEZ LANCER LA FONCTION DE TEST GÉNÉRALE MAINTENANT, (SAISISSEZ: lancer_test); SI NON, (SAISISSEZ: continuer):  " + CSI + "0m"))
    while ( test!= 'lancer_test' and test!= 'continuer'):
        test= str(input((CSI + "30;41m" + "⚠ Vous devez saisir l'un des touches suivants:lancer_test ou  continuer: " + CSI + "0m")))
    if test=='lancer_test':
        test_fonction_unitaire()
    elif test=='continuer':
        print("☺ VOUS AVEZ DECIDÉ DE NE PAS LANCER LA FONCTION DE TEST GÉNÉRALE...")
    print()
    print(CSI + "30;42m" + "AVANT DE COMMENCER SACHEZ QUE ( ♥==pion_jaune; ♦==pion_rouge; ♣==pion_noire; Configuration_Initiale= I; Configuration_Du_Milieu= M; Configuration_Finale= F)...   " + CSI + "0m")
    print(CSI + "30;42m" + "DANS CE JEU IL Y'A DEUX TYPES DE JOUER: JOUEUR CONTRE JOUEUR ET JOUEUR CONTRE ORDINATEUR...                                                                        " + CSI + "0m")
    print()
    print(CSI + "30;42m" + "VEUILLEZ BIEN LIRE LES CONSIGNES AVANT D'EXÉCUTER UNE ACTION ☺☻..." + CSI + "0m")
    print()
    Type_de_jeu = str(input(CSI + "35;35m" + "Veuillez choisir contre qui vous voulez jouer( JOUEUR OU ORDINATEUR)?: " + CSI + "0m"))
    while (Type_de_jeu != 'JOUEUR' and Type_de_jeu != 'ORDINATEUR'):
        Type_de_jeu = str(input(CSI + "30;41m" + "Vous devez saisir l'un des touches suivants: JOUEUR (si vous voulez jouer avec un joueur ) ou ORDINATEUR ( si vous voulez jouer avec l'ordinateur : " + CSI + "0m"))
    print()
    print(CSI + "36;36m" + "☺ Vous avez choisi de jouer avec un" + CSI + "0m",Type_de_jeu,"!...")
    configuration_grille=str(input(CSI + "35;35m" + "Voulez-vous faire la partie avec quelle configuration(I ou M ou F)? :" + CSI + "0m"))
    print(CSI + "36;36m" + "☺ Vous avez choisi la configuration" + CSI + "0m",configuration_grille,"!..." )
    print()
    while ( configuration_grille!='I' and configuration_grille!='M' and configuration_grille!='F'):
        configuration_grille= str(input((CSI + "30;41m" + "⚠️ Vous devez saisir l'un des touches suivants: I ( pour initiale) ou M ( pour milieu) ou F ( pour finale): " + CSI + "0m")))
    if configuration_grille=='I':
        grille = [
                 ['♥', '♣', '♥', '♦', '♦', '♥', '♥', '♥'],
                 ['♥', '♦', ' ', '♥', '♣', '♥', '♥', '♣'],
                 ['♦', '♥', '♦', '♦', '♥', '♥', '♣', '♥'],
                 ['♣', '♥', '♥', '♣', '♥', '♣', '♥', '♦'],
                 ['♥', '♦', '♦', '♥', '♦', ' ', '♦', '♥'],
                 ['♣', '♥', '♥', '♦', '♣', '♥', '♥', '♦'],
                 ['♥', '♦', '♥', '♦', '♥', '♦', '♥', '♦'],
                 ['♦', '♦', '♥', '♥', '♣', '♥', '♦', '♥']
                                                         ]
    elif configuration_grille=='M':
        grille = [
                 [' ', ' ', ' ', ' ', '♦', ' ', '♥', ' '],
                 ['♥', '♦', ' ', ' ', ' ', '♥', '♥', ' '],
                 [' ', '♥', ' ', ' ', '♥', ' ', ' ', '♥'],
                 [' ', '♥', ' ', ' ', '♥', ' ', '♥', ' '],
                 ['♥', ' ', ' ', ' ', ' ', '♦', ' ', ' '],
                 [' ', '♥', '♥', ' ', '♣', '♥', '♦', '♦'],
                 ['♥', ' ', ' ', '♦', '♥', ' ', '♣', ' '],
                 ['♦', '♦', '♥', '♥', '♣', '♥', '♦', ' ']
                                                         ]
    elif configuration_grille=='F':
        grille = [
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', '♦', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', '♦', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', '♥', ' ', '♦', '♦'],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', '♣', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', '♣', ' '],
                 [' ', '♦', ' ', ' ', ' ', ' ', ' ', ' ']
                                                         ]
    if Type_de_jeu=='JOUEUR':
        joueur_contre_joueur(grille)
    elif Type_de_jeu=='ORDINATEUR':
        joueur_contre_ordinateur(grille)
menu_de_jeu_caiman()






