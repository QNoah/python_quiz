import os
import webbrowser

naam = input("Hallo en welkom bij de quiz voer je naam in! \n")
punten = 10

def punten_uitslag():
        print('Bij elkaar heb jij ' + str(punten) + ' verdiend')
        if punten < 5:
            print('Niet zo lekker bezig')
        elif punten == 5:
            print('Een voldoende')
        elif punten >5:
            print('Goed bezig')
        elif punten == 10:
            print('Je bent te goed')

        print(' \n Wil je een muziekje horen? \n')
        print('1. Ja')
        print('2. Nee')
        antwoord = input()
        if antwoord.lower() == '1':
            webbrowser.open('https://www.youtube.com/watch?v=-dn7FtPVvoA')
        else:
            print('Bedankt voor het mee doen aan de quiz!')
            exit()

os.system('cls')
print("Welkom " + naam + " klaar voor om de quiz te spelen? \n")
print('1. Ja \n')
print('2. Nee \n')
antwoord = input()
if antwoord.lower() == '1':
    os.system('cls')
    print('Oke laten we beginnen!')
    
    antwoord =input('Vraag 1. Wie is de rapper die bekent staat als zijn naam: "SlowFlowAnimal"? \n')
    if antwoord.lower() == 'kevin':
        os.system('cls')
        print('Goed geantwoord!')
    else:
        punten -= 1
        os.system('cls')
        print('Fout geantwoord -1')
    
    antwoord =input('Vraag 2. Met welk nummer is Kevin viraal gegaan? \n')
    if antwoord.lower() == 'op de block':
        os.system('cls')
        print('Goed geantwoord!')
    else:
        punten -= 1
        os.system('cls')
        print('Fout geantwoord -1')
    
    antwoord =input('Vraag 3. Welke bekende persoon produceert en rapt op zijn eigen muziek en heeft wel eens een ft gehad met Lijpe en JoeyAK? \n')
    if antwoord.lower() == 'esko':
        os.system('cls')
        print('Goed geantwoord!')
    else:
        punten -= 1
        os.system('cls')
        print('Fout geantwoord -1')
    
    antwoord =input('Vraag 4. Waar komt de rapper Jack vandaan? \n')
    if antwoord.lower() == 'rotterdam':
        os.system('cls')
        print('Goed geantwoord!')
    else:
        punten -= 1
        os.system('cls')
        print('Fout geantwoord -1')
    
    antwoord =input('Vraag 5. Hoe heet het album van: Hef, Crooks & Adje samen? \n')
    if antwoord.lower() == 'boys in de hood 2':
        os.system('cls')
        print('Goed geantwoord!')
    else:
        punten -= 1
        os.system('cls')
        print('Fout geantwoord -1')
    
    print('Vraag 6. Met wie heeft Kevin de meeste records verbroken? \n')
    print('1. Yade Lauren')
    print('2. Lijpe')
    print('3. Josylvio')
    antwoord = input()
    if antwoord.lower() == '1':
        os.system('cls')
        print('Goed geantwoord!')
    else:
        punten -= 1
        os.system('cls')
        print('Fout geantwoord -1')
    
    antwoord =input('Vraag 7. Wat was het meest gestreamde nummer van Kevin & Yade samen? \n')
    if antwoord.lower() == 'als ik je niet zie':
        os.system('cls')
        print('Goed geantwoord!')
    else:
        punten -= 1
        os.system('cls')
        print('Fout geantwoord -1')
    
    antwoord =input('Vraag 8. Welke Amerikaanse rapper staat er om bekend dat hij zoveel blowt? \n')
    if antwoord.lower() == 'snoopdogg':
        os.system('cls')
        print('Goed geantwoord!')
    else:
        punten -= 1
        os.system('cls')
        print('Fout geantwoord -1')
    
    antwoord =input('Vraag 9. Wie is de rapper "The Woo"? \n')
    if antwoord.lower() == 'pop smoke':
        os.system('cls')
        print('Goed geantwoord!')
    else:
        punten -= 1
        os.system('cls')
        print('Fout geantwoord -1')
    
    antwoord =input('Vraag 10. Wie heeft het nummer Lucid Dreams gemaakt"? \n')
    if antwoord.lower() == 'juice wrld':
        os.system('cls')
        print('Goed geantwoord!')
    else:
        punten -= 1
        os.system('cls')
        print('Fout geantwoord -1')
    
    print('Dat was de quiz \n')
    print('Wil je misschien je punten zien?')
    print('1. Ja \n')
    print('2. Nee')
    antwoord = input()
    if antwoord.lower() == '1':
        os.system('cls')
        punten_uitslag()
    else:
        os.system('cls')
        print('Bedankt voor het mee doen aan de quiz!')
        exit()

else: print('Oke sukkel')
