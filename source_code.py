#cards = [4,3,2,10,8,10,6,8,9,5,8,10,5,3,5,4,6,9,9,1,7,6,3,5,10,10,8,10,9,10,10,7,2,6,10,10,4,10,1,3,10,1,1,10,2,2,10,4,10,7,7,10]
cards = [10,5,4,3,5,7,10,8,2,3,9,10,8,4,5,1,7,6,7,2,6,9,10,2,3,10,3,4,4,9,10,1,1,10,5,10,10,1,8,10,7,8,10,6,10,10,10,9,6,2,10,10]
num_of_piles = 7
def pile(cards,num_of_piles):
    pile = []
    check = []
    result = []
    for i in range(0,7):
        pile = pile + [[cards[i]]]
    cards = cards[7:]
    j = 0
    count = 7
    while pile != [[],[],[],[],[],[],[]]:
        while(pile[j] == []):
            j = j+1
            if j == num_of_piles:
                j = 0
        if all (x==[] for x in pile):
            break
        pile[j] = pile[j] + [cards[0]]
        count+=1
        if len(pile[j]) > 2:
            pile[j],cards = condition(pile[j],cards)
        if j >= num_of_piles-1:
            j = 0
        else :
            j = j+1
        if pile in result:
            print("draw")
            break
        else:
             check += pile
             start = 0
             end = len(check)
             step = 7
             for i in range(start,end,step):
                 x = i
                 result.append(check[x:x+step])
        cards = cards[1:]
        if(cards == []):
            print("loose")
            break
    if pile == [[],[],[],[],[],[],[]]:
        print("WON")
    print("no.of deals =",count)
def condition(pile,cards):
    if (sum(pile[:2]) + pile[-1]) % 10 == 0 :
        cards = cards + pile[:2]+[pile[-1]]
        new_pile = pile[2:-1]
        if(len(new_pile) > 2):
            return condition(new_pile,cards)
        return new_pile,cards
    elif (pile[0] + sum(pile[-2:])) % 10 == 0 :
        cards = cards+[pile[0]]+pile[-2:]
        new_pile = pile[1:-2]
        if(len(new_pile) > 2):
            return condition(new_pile,cards)
        return new_pile,cards
    elif sum(pile[-3:]) % 10 == 0 :
        cards = cards+pile[-3:]
        new_pile = pile[:-3]
        if(len(new_pile) > 2):
            return condition(new_pile,cards)
        else :
            return new_pile,cards
    else:
        return pile,cards
        
pile(cards,num_of_piles)



