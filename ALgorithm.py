from Backend import lst_combinatie_genereren, pincodes_vergelijken, join_string
'''
1.
'''
def f_noname1(i, combinatielijst):
    'lijst geeft met de mogelijkheden van 1 element met alle mog combinatie'
    lst= []
    for j in combinatielijst:
        noname_var = pincodes_vergelijken(i,j)
        if noname_var == (4,0):
            continue
        else:
            lst.append(noname_var)
    return lst

def categoriseren_dict(i, lst):
    # TODO bedenk een manier om code korter te maken
    dict = {
        (3, 0): 0,
        (2, 2): 0,
        (2, 1): 0,
        (2, 0): 0,
        (1, 4): 0,
        (1, 3): 0,
        (1, 2): 0,
        (1, 1): 0,
        (1, 0): 0,
        (0, 4): 0,
        (0, 3): 0,
        (0, 2): 0,
        (0, 1): 0,
        (0, 0): 0,
    }

    for j in lst[i]:
        if j == (3, 0):
            dict[(3, 0)] += 1
        elif j == (2, 2):
            dict[(2, 2)] += 1
        elif j == (2, 1):
            dict[(2, 1)] += 1
        elif j == (2, 0):
            dict[(2, 0)] += 1
        elif j == (1, 3):
            dict[(1, 3)] += 1
        elif j == (1, 2):
            dict[(1, 1)] += 1
        elif j == (1, 0):
            dict[(1, 0)] += 1
        elif j == (0, 4):
            dict[(0, 4)] += 1
        elif j == (0, 3):
            dict[(0, 3)] += 1
        elif j == (0, 2):
            dict[(0, 2)] += 1
        elif j == (0, 1):
            dict[(0, 1)] += 1
        elif j == (0, 0):
            dict[(0, 0)] += 1
        else:
            continue
    return dict


def lijst():
    possible_combination_feedbacks = []
    pincode = []
    a = lst_combinatie_genereren()
    for i in a:
        fb = f_noname1(i, a) # geeft een lijst met de feedbacks van i en alle combinatie uit de lijst
        possible_combination_feedbacks.append(fb) # krijgt een nested list van alle feedb
        pincode.append(i)
    return pincode, possible_combination_feedbacks



def lijst_categoriseren():
    'Elke lijst van feedbacks categoriseren '
    dict_res= {}
    code,possible_combination_feedbacks = lijst()

    for i in code:
        for j in range(0,len(possible_combination_feedbacks)):
            dct = categoriseren_dict(j,possible_combination_feedbacks)
            dict_res[join_string(i)] = dct

    return dict_res

d = lijst_categoriseren()
print(list(d.items())[0:2])




