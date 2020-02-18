from Backend import gekleurde_pincode_input, gekleurde_pincode_genereren, lst_combinatie_genereren, pincodes_vergelijken,lijst_schrappen, gok_checken
import random

lijst_letters = ['A', 'B', 'C', 'D', 'E', 'F']
def spel_men_tegen_computer():
    '''
    Op basis van de input van men(pincode), gaat de computer de pincodes vergelijken
    '''
    secret_code = gekleurde_pincode_genereren()
    print(secret_code)
    i=0
    while i<= 10:
        gok = gekleurde_pincode_input()
        feedb = pincodes_vergelijken(secret_code, gok)
        if  feedb[0]==4 and feedb[1] ==0 :
            return('win')
        else:
            print('Wrong guess, try again: {}, {}'.format(gok, feedb))
            i+=1
    return 'lose'



def spel_computer_tegen_men():
    lijst_letters = ['A', 'B', 'C', 'D', 'E', 'F']



    secret_code = gekleurde_pincode_input()  # secret pincode van de speler
    lijst_alle_combinatie = lst_combinatie_genereren()

    i=0
    while i <=10:
        if i == 0:
            gok = ['A','A','B','C']
        else:
            gok= random.choice(lijst_alle_combinatie) # TODO ALgoritme vabn Algoritme.py implementeren
        gok, z_w_feedback = gok_checken(gok,secret_code,lijst_alle_combinatie)

        print(gok, z_w_feedback)

        if z_w_feedback == (4, 0):
                return ('win')
        else:
            lijst_alle_combinatie = lijst_schrappen(gok, z_w_feedback, lijst_alle_combinatie)
            i += 1
            continue
    return ('lose')




print(spel_computer_tegen_men())

