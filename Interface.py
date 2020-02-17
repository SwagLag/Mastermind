from Spel import spel_men_tegen_computer, spel_computer_tegen_men


while True:
    print('''

        Mastermind
        Je kan kiezen voor 
        1.men: je speelt tegen de coomputer
        2 computer:computer speelt tegen jou
        3.Exit/quit
        ''')
    ans = input('Welke kies je voor? ')
    if ans =='1':
        uitslag = spel_men_tegen_computer()
        if uitslag == 'win':
            print('Gefeliciteerd, je hebt gewonnen')
            break
        elif uitslag == 'lose':
            print('Jammer, je hebt verloren')
            break
        else:
            print('Error')
    elif ans == '2':
        uitslag = spel_computer_tegen_men()
        if uitslag == 'win':
            print('Computer heeft gewonnen')
        elif uitslag == 'lose':
            print('Computer heeft verloren')
            break
        else:
            print('Error')
    elif ans =='3':
        break
        print('\n Goodbye')
    elif ans !='':
        print('\n Not Valid Choice Try again')


