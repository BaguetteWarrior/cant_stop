# CAN' STOP

from random import randint
import matplotlib.pyplot as plt


# Exemples de joueurs

def randy(pos, choix, oya):
    '''Joue au pif complet'''
    n = len(choix)
    return randint(0, n-1), [True, False][randint(0, 1)]


def randy2(pos, choix, oya):
    '''Joue au pif complet'''
    n = len(choix)
    return randint(0, n-1), [True, False, True][randint(0, 2)]



def prudent(pos, choix, oya):
    '''Continue si il n'a pas de risque'''
    grimpeurs = pos[oya]['grimpeurs']
    L = list(grimpeurs)
    n = len(choix)
    M = []
    for i in range(n):
        a, b = choix[i]
        M.append((len(set(L+[a, b])), i))
    M.sort()
    ng, no_choix = M[0]
    if ng < 3:
        return no_choix, True
    else:
        return no_choix, False


def humain(pos, choix, oya):
    s = ''
    for i in range(len(choix)):
        s = s + str(i) + ':' + str(choix[i]) + '  '
    print(s)
    s = int(input('Votre choix '))
    t = input('On continue ? O=Oui, N=Non ')
    return s, t == 'O' or t == 'o' or t == '0' or t == 'oui'


# Hauteur des voies

HAUT = {2:3, 3:5, 4:7, 5:9, 6:11, 7:13, 8:11, 9:9, 10:7, 11:5, 12:3}


def lancer_de():
    # lancer d'un dé
    return randint(1, 6)

d = {}
cntr = 0

for i1 in range(1,7):
    for i2 in range(1,7):
        for i3 in range(1,7):
            for i4 in range(1,7):
                
                cntr += 1
                
                a = [i1+i2,i3+i4]
                a.sort()
                a = tuple(a)
                    
                if a not in d:
                    d[a] = 1
                else:
                    d[a] = d[a] + 1
                    
                    
                b = [i1+i3,i2+i4]
                b.sort()
                b = tuple(b)
                
                if b not in d:
                    d[b] = 1
                else:
                    d[b] = d[b] + 1
                
                
                c = [i1+i4,i3+i2]
                c.sort()
                c = tuple(c)
                    
                if c not in d:
                    d[c] = 1
                else:
                    d[c] = d[c] + 1                
                
                


def ReadyPlayerOne(i1,i2,i3,c1,c2,c3):
    '''fonction qui determine si le jeu est necessaire base sur la position des 3 grimpeurs et du nombre de fois ou il ont ete solicitie ce tour'''
    
    d = {(2, 2): 3, (2, 3): 12, (2, 4): 18, (2, 5): 24, (2, 6): 30, (2, 7): 36, (3, 3): 12,\
         (3, 4): 36, (3, 5): 48, (3, 6): 60, (2, 8): 30, (3, 7): 72, (4, 4): 27, (4, 5): 72,\
         (4, 6): 90, (2, 9): 24, (4, 7): 108, (5, 5): 48, (5, 6): 120, (2, 10): 18, (5, 7): 144,\
         (6, 6): 75, (2, 11): 12, (6, 7): 180, (2, 12): 6, (7, 7): 108, (3, 8): 60, (3, 9): 48,\
         (4, 8): 90, (3, 10): 36, (5, 8): 120, (3, 11): 24, (6, 8): 150, (3, 12): 12, (7, 8): 180,\
         (4, 9): 72, (4, 10): 54, (5, 9): 96, (4, 11): 36, (6, 9): 120, (4, 12): 18, (7, 9): 144,\
         (5, 10): 72, (5, 11): 48, (6, 10): 90, (5, 12): 24, (7, 10): 108, (6, 11): 60, (6, 12): 30,\
         (7, 11): 72, (7, 12): 36, (8, 8): 75, (8, 9): 120, (8, 10): 90, (8, 11): 60, (8, 12): 30,\
         (9, 9): 48, (9, 10): 72, (9, 11): 48, (9, 12): 24, (10, 10): 27, (10, 11): 36, (10, 12): 18,\
         (11, 11): 12, (11, 12): 12, (12, 12): 3}
    p1 = 0
    for k in d:
#         print(i1)
#         print(k)
        if i1 in k:
            p1 += d[k]
    p1 = p1/1296    

    p2 = 0
    for k in d:
        if i2 in k:
            p2 += d[k]
    p2 = p2/1296

    p3 = 0
    for k in d:
        if i3 in k:
            p3 += d[k]
    p3 = p3/1296
    
    w1 = 1 / p1
    w2 = 1 / p2
    w3 = 1 / p3
    

    p11 = d[(i1,i1)] / 1296
    p22 = d[(i2,i2)] / 1296
    p33 = d[(i3,i3)] / 1296
    
    if i1 <= i2:
        p12 = d[(i1,i2)] / 1296
    else:
        p12 = d[(i2,i1)] / 1296
    
    if i1 <= i3:
        p13 = d[(i1,i3)] / 1296
    else:
        p13 = d[(i3,i1)] / 1296
    
    if i2 <= i3:
        p23 = d[(i2,i3)] / 1296
    else:
        p23 = d[(i3,i2)] / 1296
        
    
    PlayYesNo = p1 * (w1 * (c1 + 1) + w2 * c2 + w3* c3) +\
            p2 * (w1 * c1 + w2 * (c2 + 1) + w3 * c3) +\
            p3 * (w1 * c1 + w2 * c2 + w3 * (c3 + 1)) +\
            p12 * (w1 * (c1 + 1) + w2 * (c2 + 1) + w3 * c3) +\
            p13 * (w1 * (c1 + 1) + w2 * c2 + w3 * (c3 + 1)) +\
            p23 * (w1 * c1 + w2 * (c2 + 1) + w3 * (c3 + 1)) +\
            p11 * (w1 * (c1 + 2) + w2 * c2 + w3 * c3) +\
            p22 * (w1 * c1 + w2 * (c2 + 2) + w3 * c3) +\
            p33 * (w1 * c1 + w2 * c2 + w3 * (c3 + 2)) +\
            (1 - (p1 + p2 + p3 + p12 + p13 + p11 + p22 + p33 + p23))*40\
            > w1 * c1+ w2 * c2 + w3 * c3
#     print((p1 * (w1 * (c1 + 1) + w2 * c2 + w3* c3) +\
#             p2 * (w1 * c1 + w2 * (c2 + 1) + w3 * c3) +\
#             p3 * (w1 * c1 + w2 * c2 + w3 * (c3 + 1)) +\
#             p12 * (w1 * (c1 + 1) + w2 * (c2 + 1) + w3 * c3) +\
#             p13 * (w1 * (c1 + 1) + w2 * c2 + w3 * (c3 + 1)) +\
#             p23 * (w1 * c1 + w2 * (c2 + 1) + w3 * (c3 + 1)) +\
#             p11 * (w1 * (c1 + 2) + w2 * c2 + w3 * c3) +\
#             p22 * (w1 * c1 + w2 * (c2 + 2) + w3 * c3) +\
#             p33 * (w1 * c1 + w2 * c2 + w3 * (c3 + 2)) +\
#             (1 - (p1 + p2 + p3 + p12 + p13 + p11 + p22 + p33 + p23))*0\
#             , w1 * c1+ w2 * c2 + w3 * c3))
    return PlayYesNo

def addicted_to_the_shindig(pos,choix,oya):
#     print(pos)
    climbers = pos[oya]['grimpeurs']
    milestone = pos[oya]['camps']
    L = []
    dd = {}
    Mcoef = 0
    
    Lkeys = list(climbers.keys()) #list of keys for the climbers dict
        
        
        
        
    h = {2:3, 3:5, 4:7, 5:9 ,6:11 ,7:13 ,8:11 ,9:9 ,10:7 ,11:5 ,12:3 }

    if len(climbers) < 3:
#         print("if")
        for j in range(2,8):
            for i in range(len(choix)):
                if choix[i][0] == j or choix[i][0] == j-7:
#                     print(str(i) + ' retour')
                    return i,True
        return(0,True) # fail safe A RESOUDRE (l'enlever)
        
    else:
#         print("else")
#         for per in climbers:
#             L.append(climbers[per])
#             if climbers[per]/h[per] > Mcoef:
#                 Mcoef = climbers[per]/h[per]
#                 Mnum = per
#         print(Lkeys)
#         print(climbers)
        for i in range(len(Lkeys)):
            dd[str(Lkeys[i])] = climbers[Lkeys[i]]/h[Lkeys[i]] * 100
#         print(dd)
        dd1 = dict(sorted(dd.items(), key=lambda x: x[1], reverse=True))
#         print(dd1)
        Lcoefs = list(dd1.keys())
#         print(Lcoefs)
#             if climbers[Lkeys[i]]/h[Lkeys[i]] > Mcoef:
#                 Mcoef = climbers[Lkeys[i]]/h[Lkeys[i]]
#                 Mnum = Lkeys[i]
                
#                 IMPORTANT REWORK: make a list of the keys in order of highest coef (see line 211)

        
#       determine the progress of climbers
        for i in range(3):
#             print(L[0])
#             print(climbers)
#             print(climbers[Lkeys[0]])
            if Lkeys[0] not in milestone:
                c1 = climbers[Lkeys[0]]
            else:
                c1 = climbers[Lkeys[0]] - milestone[Lkeys[0]]
                
            if Lkeys[1] not in milestone:
                c2 = climbers[Lkeys[1]]
            else:
                c2 = climbers[Lkeys[1]] - milestone[Lkeys[1]]
                
            if Lkeys[2] not in milestone:
                c3 = climbers[Lkeys[2]]
            else:
                c3 = climbers[Lkeys[2]] - milestone[Lkeys[2]]
                
#         print('caca')        
#         print(Lcoefs)
#         print(choix)

        for i in range(len(choix)):
            if int(Lcoefs[0]) in choix[i]:
                print(str(i) + " + " + str(ReadyPlayerOne(Lkeys[0],Lkeys[1],Lkeys[2],c1,c2,c3)))
                return i, ReadyPlayerOne(Lkeys[0],Lkeys[1],Lkeys[2],c1,c2,c3)
        for i in range(len(choix)):
            if int(Lcoefs[1]) in choix[i]:
                print(str(i) + " + " + str(ReadyPlayerOne(Lkeys[0],Lkeys[1],Lkeys[2],c1,c2,c3)))
                return i, ReadyPlayerOne(Lkeys[0],Lkeys[1],Lkeys[2],c1,c2,c3)
        for i in range(len(choix)):
            if int(Lcoefs[2]) in choix[i]:
                print(str(i) + " + " + str(ReadyPlayerOne(Lkeys[0],Lkeys[1],Lkeys[2],c1,c2,c3)))
                return i, ReadyPlayerOne(Lkeys[0],Lkeys[1],Lkeys[2],c1,c2,c3)
        
#         print("caca2")
        return 0,False  # c'est perdu rip le calcul
                
                
            
        
        




def cant_stop(joueur0, joueur1, verbose=False):
    '''renvoie 0 si le joueur0 gagne, 1 si le joueur1 gagne'''
    # position initiale
    # voies gagnees numero:bool
    # camps de bases numero: hauteur
    # grimpeurs en cours numero:hauteur
    pos0 = {'voies':{}, 'camps':{}, 'grimpeurs':{}}
    pos1 = {'voies':{}, 'camps':{}, 'grimpeurs':{}}

    pos = [pos0, pos1]

    joueurs = [joueur0, joueur1]

    oya = 0 # joueur dont s'est le tour

    while len(pos[0]['voies']) < 3 and len(pos[1]['voies']) < 3:
        if verbose:
            affiche_position(pos)
        # -------- LANCER DES DES -------------
        des = [lancer_de() for _ in range(4)]
        if verbose:
            print("Résultats des dés :", *des)
        choix = []
        S = sum(des)
        for i in range(1, 4):
            (a, b) = (des[0] + des[i], S - des[0] - des[i])
            choix.append((a, b))
            choix.append((b, a)) # le premier est le prioritaire
        choix = list(set(choix))
        if verbose:
            print('POSSIBILITES :', *choix)

        joueur = joueurs[oya]

        # ----------- L'OYA FAIT SON CHOIX ------------
        if verbose:
            print("Au tour de ", joueur.__name__)
        reponse = joueur(pos, choix, oya) # le joueur répond le couple: no du choix, stop_ou_encore (True = on continue, False = Stop)
        try:
            no_choix, encore = reponse
        except:
#             print(reponse)
            print("boo2")
            return 1 - oya # coup non comforme, le joueur perd
        if (no_choix < 0 or no_choix > len(choix) - 1) or not isinstance(encore, bool):
            print(no_choix)
            print(len(choix))
            print("boo1")
            # coup illégal, le joueur perd immédiatement
            return 1-oya

        # On prend en compte le choix
        des = choix[no_choix]
        if verbose:
            print(joueurs[oya].__name__, ' joue ', des)
        voies = pos[oya]['voies']
        voies_adv = pos[1-oya]['voies']
        grimpeurs = pos[oya]['grimpeurs']
        camps = pos[oya]['camps']
        camps_adv = pos[1-oya]['camps']
        avance = False # si on réussit à avancer un grimpeur
        for de in des:
            if de not in voies and de not in voies_adv:
                if de in grimpeurs:
                    if grimpeurs[de] < HAUT[de]:
                        avance = True
                        grimpeurs[de] += 1
                elif len(grimpeurs) < 3:
                    if de in camps:
                        grimpeurs[de] = camps[de] + 1
                    else:
                        grimpeurs[de] = 1
                    avance = True

        if not avance: # C'est la chute !
            if verbose:
                print('Aaaaaaaaaaaaaahhhhhhhhhhhhhhhhh')
            pos[oya]['grimpeurs'] = {}
            oya = 1 - oya
        elif not encore:
            if verbose:
                print('STOP !!!')
            # On encaisse
            for g in grimpeurs:
                if grimpeurs[g] == HAUT[g]:
                    voies[g] = True
                    if g in camps:
                        del camps[g]
                    if g in camps_adv:
                        del camps_adv[g]
                else:
                    camps[g] = grimpeurs[g]
            pos[oya]['grimpeurs'] = {}
            oya = 1 - oya
        else:
            if verbose:
                print('ENCORE !')
        # On continue avec le même joueur



    # ---------- IL FAUT BIEN UN VAINQUEUR ---------------
    if verbose:
        affiche_position(pos)
    if len(pos[0]['voies']) >= 3:
        vainqueur = 0
    else:
        vainqueur = 1
    if verbose:
        print(joueurs[vainqueur].__name__, ' a gagné !!!')
    return vainqueur


def affiche_position(pos):

    for hauteur in range(13, 0, -1):
        ligne = ''
        for v in range(2, 13):
            if HAUT[v] < hauteur:
                ligne = ligne + ' '*4
            else:
                L = ['*', '*', '*']
                for i in range(2):
                    if v in pos[i]['voies']:
                        L[1] = str(i)
                    if v in pos[i]['grimpeurs'] and pos[i]['grimpeurs'][v] == hauteur:
                        L[2*i] = 'g'
                    if v in pos[i]['camps'] and pos[i]['camps'][v] == hauteur:
                        L[2*i] = str(i)


                ligne = ligne + ' ' + ''.join(L)
        print(ligne)
    ligne = ''
    for v in range(2, 13):
        ligne = ligne + '  ' + str(v)
        if v < 10:
            ligne = ligne + ' '
    print(ligne)


def tournoi(liste_joueurs, nb_parties=500):
    '''1000 rencontres entre chaque joueur
    1 victoire = 1pt
    '''
    n = len(liste_joueurs)
    assert n > 1, "pas assez de joueurs en lice"

    nb_points = [0] * n
    nom_joueurs = [joueur.__name__ for joueur in liste_joueurs]
    plt.ion()
    for i in range(nb_parties):
        for i0 in range(n):
            for j0 in range(n):
                if i0 != j0:
                    r = cant_stop(liste_joueurs[i0], liste_joueurs[j0], verbose=False)
                    nb_points[[i0, j0][r]] += 1
        plt.pie(nb_points, labels=nom_joueurs, autopct='%1.1f%%')
        plt.text(0.8, 0.8, str(i+1) + ' parties')
        plt.pause(0.01)
        plt.cla()
    return list(zip(nom_joueurs, nb_points))

# Exemples de jeux
# cant_stop(humain, randy2)
# cant_stop(randy2, randy3, verbose=False)
# En tournoi :
# tournoi([randy, randy2, prudent])
