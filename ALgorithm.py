import random
from Backend import pincodes_vergelijken, lst_combinatie_genereren


lijst_letters = ['A', 'B', 'C', 'D', 'E', 'F']
lst = lst_combinatie_genereren(lijst_letters)
secret_code = ['A', 'F', 'D', 'E']
print(secret_code)
#print(simple_strategy(secret_code, lst))