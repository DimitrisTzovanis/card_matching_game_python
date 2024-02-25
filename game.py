from random import shuffle
from ex import deck,checkvalid
end = False
found = [] #edo 8a prosti8entai ta stoixeia pou exoun bre8ei. An len(found)==len(deck) to paixnidi teleionei
playerpoints = []
print("Καλωσήλθατε στο Matching Game")
begin = input("Πατήστε ENTER για να ξεκινήσει το παιχνίδι ")
while True:
    players = str(input("Δώστε αριθμό παικτών (από 2 και πάνω): "))
    if players.isdigit() and players >= '2':
        break
    else:
        print("ΠΑΡΑΚΑΛΩ ΔΩΣΤΕ ΕΓΚΥΡΕΣ ΤΙΜΕΣ")
        continue
players = int(players)
while True:
    level = str(input("Δώστε επίπεδο δυσκολίας Εύκολο (1), Μέτριο (2), Δύσκολο (3): "))
    if level.isdigit() and '1' <= level <= '3' and level < '10':
        break
    else:
        print("ΠΑΡΑΚΑΛΩ ΔΩΣΤΕ ΕΓΚΥΡΕΣ ΤΙΜΕΣ")
        continue
level = int(level)
if level == 1:
    deck = deck(10) #ta stoixeia apo to 10 kai meta
    al = 4 #xrisimopoieitai stin anaparastasi tou paixnidiou
elif level == 2:
    deck = deck(1,11) #ta stoixeia apo ton asso mexri kai to 10
    al = 10
else:
    deck = deck()
    al = 13
shuffle(deck)
listx = []
for i in deck:
    listx.append('X') #xrisimopoietai stin anaparastasi tou paixnidiou, ka8e stoixeio anaparista mia karta. Me 'X' symbolizontai oi kleistes kartes
numbers = '' #kataskeuazoume tous deiktes twn kartwn (blepe sinartisi table)
for i in range(1,al+1):
    if al == 13 and i == 10:
        numbers += f'{i:5}'
    else:
        numbers += f'{i:4}'
def table(tablelist=listx):
    """Kataskeuastis table (pinakas paixnidiou, opou emfanizontai oi kartes).

    Epistrefei anaparastasi pinaka paixnidiou, xrisimopoiwntas ta stoixeia tis listx.

    Stin proti seira ektiponetai mia seira ari8mwn (numbers) apo to 1 mexri to al.
    Os al exei oristei pote "spaei" h anaparastasi sthn epomeni seira (px 4 gia epipedo 1, 10 gia epipedo 2 klp)
    Stis epomenes seires ektiponontai ta stoixeia tis listx (antistoixa h seira "spaei" ka8e al (4, 10 h 13) theseis)
    Anamesa se ka8e stoixeio tis listx mesolabei ena keno analoga me to mikos tou (gia na mhn xalaei h diataxi tou pinaka)
    Stin proti 8esi ka8e seiras (ektos apo tin numbers) brisketai o ari8mos tis seiras (1, 2, 3, 4, xrisimopoioume tin metabliti k)
    Se ka8e periptosi ektiponontai 4 seires (5 mazi me ti seira numbers)"""
    print(numbers)
    j=None
    k=1
    for x in tablelist:
        if j==al or j==None:
            if j != None:
                print('\n')
            j=0
            print(k, end='  ')
            k+=1
        if len(x) == 1:
            print(x, end='   ')
        elif len(x) == 2:
            print(x, end='  ')
        else:
            print(x, end=' ')
        j+=1
    print('\n')
liseis = listx.copy()
for i in range(len(liseis)):
    liseis[i] = deck[i][3]
table(liseis) #xrisimopoieitai i sinartisi table prokeimenou na ektipothoun oi liseis tou paixnidiou (anoixtes kartes)
table()
for p in range(players):
    playerpoints.append(0) #arxikopoihsh twn pontwn ka8e paikth
numvaledes = None
rigades = False
def messages(text='την πρώτη'):
    """Η συνάρτηση, κάνοντας χρήση της συνάρτησης checkvalid, πραγμοτοποιεί
    τους απαραίτητους ελέγχους εγκυρότητας για τις θέσεις των καρτών που επιλέγει ο χρήστης"""
    invalid = False
    while True:
        check = 4
        while True:
            if check == 1 or check == 3:
                break
            else:
                if invalid == True:
                    print("ΠΑΡΑΚΑΛΩ ΔΩΣΤΕ ΕΓΚΥΡΕΣ ΤΙΜΕΣ")
                x, y = input(f"Παίκτη {p+1}: Επιλέξτε {text} κάρτα με τη μορφή \n[Γραμμή - κενό - Στήλη]: ").split()
                check = checkvalid(x,y,al,deck)                 
                invalid = True
        if check != 3:
            break
        else:
            print("Η κάρτα που επιλέξατε είναι ήδη ανοικτή!")
            table()
    x=int(x)-1
    y=int(y)-1
    card = x*al + y
    listx[card] = deck[card][3] #oi kartes "anoigoun"
    deck[card][4] = 'open'
    table()
    return card
def correct(card1, card2):
    print("ΣΩΣΤΑ")
    playerpoints[p] += deck[card1][2]
    print(playerpoints[p],'ΠΟΝΤΟΙ')
    found.append(deck[card1])
    found.append(deck[card2])
while end != True:
    for p in range(players):
        if end == True:
            continue
        if p != numvaledes and numvaledes != None:
            continue
        else:
            numvaledes = None
        if rigades == True:
            rigades = False
            continue
        for i in range(2):
            if i == 0:
                firstcard = messages()
            else:
                secondcard = messages('τη δεύτερη')
        if deck[firstcard][0] == deck[secondcard][0]:
            correct(firstcard, secondcard)
            if len(deck) == len(found):
                end = True
                winner = p+1
                winnerpoints = max(playerpoints)
            if deck[firstcard][0] == 'J' and end != True:
                numvaledes = p
                print(f"O ΠΑΙΚΤΗΣ {p+1} ΑΝΟΙΞΕ ΔΥΟ ΒΑΛΕΔΕΣ ΚΑΙ ΞΑΝΑΠΑΙΖΕΙ!")
            if deck[firstcard][0] == 'K' and end != True:
                rigades = True
                print(f"O ΠΑΙΚΤΗΣ {p+1} ΑΝΟΙΞΕ ΔΥΟ ΡΗΓΑΔΕΣ. Ο ΕΠΟΜΕΝΟΣ ΠΑΙΚΤΗΣ ΧΑΝΕΙ ΤΗ ΣΕΙΡΑ ΤΟΥ")
        elif (deck[firstcard][0] == 'K' and deck[secondcard][0] == 'Q') or (deck[firstcard][0] == 'Q' and deck[secondcard][0] == 'K'):
            print(f"O ΠΑΙΚΤΗΣ {p+1} ΑΝΟΙΞΕ ΕΝΑΝ ΡΗΓΑ ΚΑΙ ΜΙΑ ΝΤΑΜΑ!\nΜΠΟΡΕΙ ΝΑ ΕΠΙΛΕΞΕΙ ΚΑΙ ΤΡΙΤΗ ΚΑΡΤΑ!")
            thirdcard=messages('την τρίτη')
            if deck[firstcard][0] == deck[thirdcard][0]:
                correct(firstcard, thirdcard)
                listx[secondcard] = 'X'
                deck[secondcard][4] = 'closed'
                table()
            elif deck[secondcard][0] == deck[thirdcard][0]:
                correct(secondcard, thirdcard)
                listx[firstcard] = 'X'
                deck[firstcard][4] = 'closed'
                table()
            else:
                listx[firstcard] = listx[secondcard] = listx[thirdcard] = 'X' #Se periptosi lathous, oi kartes xanakleinoun
                deck[firstcard][4] = deck[secondcard][4] = deck[thirdcard][4] = 'closed'
                table()
        else:
            listx[firstcard] = listx[secondcard] = 'X' #Se periptosi lathous, oi kartes xanakleinoun
            deck[firstcard][4] = deck[secondcard][4] = 'closed'
            print("ΛΑΘΟΣ")
            table()
print(f"ΝΙΚΗΤΗΣ ΕΙΝΑΙ Ο ΠΑΙΚΤΗΣ {winner} ΜΕ: {winnerpoints} ΠΟΝΤΟΥΣ")