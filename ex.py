def deck(min=1,max=14):
    """Kataskeuastis deck (trapoula paixnidiou).

    min -- arxiko stoixeio tis trapoulas
    max -- teleutaio stoixeio tis trapoulas

    Epistrefei mia lista listwn (nested lists, mia gia ka8e fillo),
    h opoia exei mikos analogo me tis parametrous min kai max.

    Ta min kai max ri8mizoun poia stoixeia apoteloun meros tis listas
    px gia min=1, max=14 ta stoixeia ekteinontai apo to "A" (assos) ews to "K" (rigas)
    
    H sinartisi, xekinontas apo to stoixeio min, dimiourgei 4 diaforetikes nested lists
    gia ka8e stoixeio, mia gia kathe katigoria ("heart", "spade", "club", "diamond")

    Diladi, gia min=10, max=14 epistrefei lista mikous 16 (periexei 4*4=16 stoixeia typou list)
    Gia min=1, max=11 epistrefei lista mikous 40 (periexei 4*10=40 stoixeia typou list)
    Gia tis orismenes times, epistrefei lista mikous 52 (periexei 4*14=52 stoixeia typou list)

    Ka8e nested list sti lista exei 5 theseis index (apo 0 mexri 4), opou ka8e mia anaparista vasika
    stoixeia gia ti leitourgia tou paixnidiou.

    index[0] : symvolo fillou (px "2","3",..."A" kok)
    index[1] : katigoria fillou (px "heart", "spade", "club", "diamond")
    index[2] : pontoi fillou
    index[3] : emfanisi fillou
    index[4] : katastasi fillou ("open" h "closed")

    Paradeigmata:

    >>> deck = deck(13)
    >>> len(deck)
    4
    >>> deck == [["K", "club", 10, "K"+"\u2663", "closed"], ["K", "heart", 10, "K"+"\u2665", "closed"], \
    ["K", "spade", 10, "K"+"\u2660", "closed"], ["K", "diamond", 10, "K"+"\u2666", "closed"]]
    True
    >>> deck[0][0]
    'K'
    """
    element = []
    for j in range(4):
        if j == 0 :
            cat = "club"
            sym = "\u2663"
        elif j == 1 :
            cat = "heart"
            sym = "\u2665"
        elif j == 2 :
            cat = "spade"
            sym = "\u2660"
        else :
            cat = "diamond"
            sym = "\u2666"
        for i in range(min, max) :
            if i == 1:
                element.append(["A", cat, i, "A" + sym, "closed"])
            elif 1 < i <= 10 :
                element.append([str(i), cat, i, str(i) + sym, "closed"])
            else:
                if i == 11 :
                    a = "J"
                elif i == 12 :
                    a = "Q"
                else :
                    a = "K"
                element.append([a, cat, 10, a + sym, "closed"])
    return element

element=deck(10)
element[4][4] = 'open'
#"Xtizoume" to deck element gia tous skopous tou doctest tis checkvalid
# 8etoume mia karta ws 'open' (anoikth) gia na epibebaiosoume oti o xrhsths den mporei na tin anoixei (afou einai hdh anoikth) (8o test tis checkvalid)

def checkvalid(a,b,al=4,deck=element): #i ana8esi timwn stis metablites al kai deck ginetai gia eukolotero doctest
    """Elegxei an o xrhsths dinei egkyrh timh
    
    Akolou8oun paradeigmata pou efarmozontai sto eukolo epipedo (16 kartes)
    gia ta zeugi timwn '100','4' '4','Tolis', '1','1' kai elegxou oti o xrhsths epilegei mia kleisth karta:

    >>> checkvalid('4','Tolis')
    2
    >>> checkvalid('Nikos','4')
    2
    >>> checkvalid('1','1')
    1
    >>> checkvalid('400','4')
    2
    >>> checkvalid('4','400')
    2
    >>> checkvalid('-1','1')
    2
    >>> checkvalid('1','-1')
    2
    >>> checkvalid('2','1')
    3"""
    if a.isdigit() and b.isdigit() and a<='4' and b<=str(al) and a>'0' and b>'0':
        if deck[(int(a)-1)*al + int(b)-1][4] == 'open':
            return 3 #an i karta einai hdh anoikth
        return 1 #an i karta einai egkyrh
    else:
        return 2 #an i karta einai akyrh