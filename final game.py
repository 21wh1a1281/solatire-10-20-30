from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import pygame

pygame.init()

def play_music(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()

w1 = tk.Tk()
w1.geometry("1900x900")

image = tk.PhotoImage(file = "SOLATIRE.png")
label = tk.Label(w1,image = image)
label.place(x=0,y=0,relwidth = 1,relheight = 1)

def cases():
    global case
    case = Tk()
    case.geometry("1900x1000")
    case.configure(background = "DarkCyan")
    
    text = tk.Text(case, height=2, width=22)
    text.insert(tk.END, "select your test case")
    text.config(state=tk.DISABLED)
    text.pack()
    def win():
        win_case = Tk()
        win_case.geometry("1900x1000")
        win_case.configure(background = "DarkCyan")
        
        label = tk.Label(win_case)
        label.pack()


    win_list = [2,6,5,10,10,4,10,10,10,4,5,10,4,5,10,9,7,6,1,7,6,9,5,3,10,10,4,10,9,2,1,10,1,10,10,10,3,10,9,8,10,8,7,1,2,8,6,7,3,3,8,2]
    loose_list = [4,3,2,10,8,10,6,8,9,5,8,10,5,3,5,4,6,9,9,1,7,6,3,5,10,10,8,10,9,10,10,7,2,6,10,10,4,10,1,3,10,1,1,10,2,2,10,4,10,7,7,10]
    draw_list = [10,5,4,3,5,7,10,8,2,3,9,10,8,4,5,1,7,6,7,2,6,9,10,2,3,10,3,4,4,9,10,1,1,10,5,10,10,1,8,10,7,8,10,6,10,10,10,9,6,2,10,10]
    

    btopen = Button(case,text = "win",width = 15,height = 3,command = lambda:open(win_list)).place(x = 700,y=400)

    btopen = Button(case,text = "loose",width = 15,height = 3,command = lambda:open(loose_list)).place(x = 700,y=500)

    btopen = Button(case,text = "draw",width = 15,height = 3,command = lambda:open(draw_list)).place(x = 700,y=600)

def generateRandomDeck():
    global nums
    nums = [i for i in range(1,11)]
    nums += [10,10,10]
    nums += nums + nums + nums
    random.shuffle(nums)
    open(nums)

def open(compare):
    
    w1.destroy()

    root = Tk()
    root.title('10-20-30')
    root.geometry("1900x1000")
    root.configure(background = "green")

    my_frame = Frame(root,bg = "green")
    my_frame.pack(pady = 20)

    my_frame2 = Frame(root,bg = "green")
    my_frame2.pack(pady = 20)

    my_frame3 = Frame(root,bg = "green")
    my_frame3.pack(pady = 20)

    result = Frame(root,bg = "green")
    result.pack(pady = 20)

    def condition(pile,cards):
        check = []
        for i in pile:
            check.append(i[0])
        print(check)
        if (sum(check[:2]) + check[-1]) % 10 == 0 :
            cards = cards + pile[:2]+[pile[-1]]
            new_pile = pile[2:-1]
            if(len(new_pile) > 2):
                return condition(new_pile,cards)
            return new_pile,cards
        elif (check[0] + sum(check[-2:])) % 10 == 0 :
            cards = cards+[pile[0]]+pile[-2:]
            new_pile = pile[1:-2]
            if(len(new_pile) > 2):
                return condition(new_pile,cards)
            return new_pile,cards
        elif sum(check[-3:]) % 10 == 0 :
            cards = cards+pile[-3:]
            new_pile = pile[:-3]
            if(len(new_pile) > 2):
                return condition(new_pile,cards)
            else :
                return new_pile,cards
        else:
            return pile,cards
        
    def cardname():
        suits = ["diamonds","clubs","hearts","spades"]
        values = [i for i in range(2,11)]
        global deck
        deck = []
        values = values
        for suit in suits:
            for value in values:
                deck.append([value,f'{value}_of_{suit}'])
        deck.extend([[1, '1_of_diamonds'],[1, '1_of_clubs'],[1, '1_of_hearts'],[1, '1_of_spades'],[10, '11_of_diamonds'], [10, '12_of_diamonds'], [10, '13_of_diamonds'], [10, '11_of_clubs'], [10, '12_of_clubs'], [10, '13_of_clubs'], [10, '11_of_hearts'], [10, '12_of_hearts'], [10, '13_of_hearts'], [10, '11_of_spades'], [10, '12_of_spades'], [10, '13_of_spades']])
        return deck
    deck_cards = cardname()

    def get_card(compare,deck_cards):
        random.shuffle(deck_cards)
        match_found = []
        for i in compare:
            match = [j for j in deck_cards if i == j[0]]
            if len(match) > 0:
                match_found.append(match[0])
                deck_cards.remove(match[0])
        print(len(match_found))
        return(match_found)
        
    def shuffle(compare):
        #compare = random_deck()
        #compare = [2,6,5,10,10,4,10,10,10,4,5,10,4,5,10,9,7,6,1,7,6,9,5,3,10,10,4,10,9,2,1,10,1,10,10,10,3,10,9,8,10,8,7,1,2,8,6,7,3,3,8,2]
        #compare = [4,3,2,10,8,10,6,8,9,5,8,10,5,3,5,4,6,9,9,1,7,6,3,5,10,10,8,10,9,10,10,7,2,6,10,10,4,10,1,3,10,1,1,10,2,2,10,4,10,7,7,10]
        #compare = [10,5,4,3,5,7,10,8,2,3,9,10,8,4,5,1,7,6,7,2,6,9,10,2,3,10,3,4,4,9,10,1,1,10,5,10,10,1,8,10,7,8,10,6,10,10,10,9,6,2,10,10]
        num_of_piles = 7
        cards_1 = get_card(compare,cardname())
        print(cards_1)
        #cards = [[4,'4_of_diamonds'],[3,'3_of_diamonds'],[2,'2_of_diamonds'],[10,'10_of_diamonds'],[8,'8_of_diamonds'],[10,'10_of_diamonds'],[6,'6_of_diamonds'],[8,'8_of_diamonds'],[9,'9_of_diamonds'],[5,'5_of_diamonds'],[8,'8_of_diamonds'],[10,'10_of_diamonds'],[5,'5_of_diamonds'],[3,'3_of_diamonds'],[5,'5_of_diamonds'],[4,'4_of_diamonds'],[6,'6_of_diamonds'],[9,'9_of_diamonds'],[9,'9_of_diamonds'],[1,'14_of_diamonds'],[7,'7_of_diamonds'],[6,'6_of_diamonds'],[3,'3_of_diamonds'],[5,'5_of_diamonds'],[10,'10_of_diamonds'],[10,'10_of_diamonds'],[8,'8_of_diamonds'],[10,'10_of_diamonds'],[9,'9_of_diamonds'],[10,'10_of_diamonds'],[10,'10_of_diamonds'],[7,'7_of_diamonds'],[2,'2_of_diamonds'],[6,'6_of_diamonds'],[10,'10_of_diamonds'],[10,'10_of_diamonds'],[4,'4_of_diamonds'],[10,'10_of_diamonds'],[1,'14_of_diamonds'],[3,'3_of_diamonds'],[10,'10_of_diamonds'],[1,'14_of_diamonds'],[1,'14_of_diamonds'],[10,'10_of_diamonds'],[2,'2_of_diamonds'],[2,'2_of_diamonds'],[10,'10_of_diamonds'],[4,'4_of_diamonds'],[10,'10_of_diamonds'],[7,'7_of_diamonds'],[7,'7_of_diamonds'],[10,'10_of_diamonds']]
        pile = []
        check = []
        global result
        result = []
        global display_list
        display_list = []
        for i in range(0,7):
            pile = pile + [[cards_1[i]]]
        cards_1 = cards_1[7:]
        j = 0
        count = 7
        while pile != [[],[],[],[],[],[],[]]:
            while(pile[j] == []):
                j = j+1
                if j == num_of_piles:
                    lastCardInPile = [j[-1] if j != [] else [30,"empty_pile"] for j in pile]
                    display_list += [lastCardInPile + [cards_1[1] if cards_1 != [] else [30,"empty_pile"]]]
                    j = 0
            if all (x==[] for x in pile):
                break
            pile[j] = pile[j] + [cards_1[0]]
            count+=1
            if len(pile[j]) > 2:
                pile[j],cards_1 = condition(pile[j],cards_1)
            if j >= num_of_piles-1:
                lastCardInPile = [j[-1] if j != [] else [30,"empty_pile"] for j in pile]
                display_list += [lastCardInPile + [cards_1[1] if cards_1 != [] else [30,"empty_pile"]]]
                j = 0
            else :
                j = j+1
            if pile in result:
                return display_list,2
            else:
                check += pile
                start = 0
                end = len(check)
                step = 7
                for i in range(start,end,step):
                    x = i
                    result.append(check[x:x+step])
            cards_1 = cards_1[1:]
            if(cards_1 == []):
                return display_list,0
        if pile == [[],[],[],[],[],[],[]]:
            return display_list,1

    def random_deck():
        win_deck = [2,6,5,10,10,4,10,10,10,4,5,10,4,5,10,9,7,6,1,7,6,9,5,3,10,10,4,10,9,2,1,10,1,10,10,10,3,10,9,8,10,8,7,1,2,8,6,7,3,3,8,2]
        lose_deck = [4,3,2,10,8,10,6,8,9,5,8,10,5,3,5,4,6,9,9,1,7,6,3,5,10,10,8,10,9,10,10,7,2,6,10,10,4,10,1,3,10,1,1,10,2,2,10,4,10,7,7,10]
        draw_deck = [10,5,4,3,5,7,10,8,2,3,9,10,8,4,5,1,7,6,7,2,6,9,10,2,3,10,3,4,4,9,10,1,1,10,5,10,10,1,8,10,7,8,10,6,10,10,10,9,6,2,10,10]
        decks = [win_deck] + [lose_deck] + [draw_deck]
        index = random.randint(0,2)
        return decks[index]
    
    res,num = shuffle(compare)

    def res_open():
        try:
            card = res[0]
            res.remove(res[0])
            pic = card[0][1]
            global photo_1
            photo_1 = PhotoImage(file = f"{pic}.png")
            photo_1 = photo_1.subsample(6,6)
            dealer_label_1.config(image = photo_1)
            
            pic = card[1][1]
            global photo_2
            photo_2 = PhotoImage(file = f"{pic}.png")
            photo_2 = photo_2.subsample(6,6)
            dealer_label_2.config(image = photo_2)
            
            pic = card[2][1]
            global photo_3
            photo_3 = PhotoImage(file = f"{pic}.png")
            photo_3 = photo_3.subsample(6,6)
            dealer_label_3.config(image = photo_3)
            
            pic = card[3][1]
            global photo_4
            photo_4 = PhotoImage(file = f"{pic}.png")
            photo_4 = photo_4.subsample(6,6)
            dealer_label_4.config(image = photo_4)
            
            pic = card[4][1]
            global photo_5
            photo_5 = PhotoImage(file = f"{pic}.png")
            photo_5 = photo_5.subsample(6,6)
            dealer_label_5.config(image = photo_5)
            
            pic = card[5][1]
            global photo_6
            photo_6 = PhotoImage(file = f"{pic}.png")
            photo_6 = photo_6.subsample(6,6)
            dealer_label_6.config(image = photo_6)
            
            pic = card[6][1]
            global photo_7
            photo_7 = PhotoImage(file = f"{pic}.png")
            photo_7 = photo_7.subsample(6,6)
            dealer_label_7.config(image = photo_7)
            
            pic = card[7][1]
            global photo_8
            photo_8 = PhotoImage(file = f"{pic}.png")
            photo_8 = photo_8.subsample(6,6)
            res_label_1.config(image = photo_8)
            
        except:
            if num == 2:
                root.destroy()
                sec_window("draw.png")
            elif num == 1:
                root.destroy()
                sec_window("won.png")
            else:
                root.destroy()
                sec_window("loose.png")
    
    deck = LabelFrame(result,text = "deck",bd = 0,background="green")
    deck.grid(row=4,column = 0,padx = 40,ipadx = 40)

    dealer_frame1 = LabelFrame(my_frame,text = "pile1",bd = 0,background="green")
    dealer_frame1.grid(row=5,column = 0,padx = 40,ipadx = 40)

    dealer_frame2 = LabelFrame(my_frame,text = "pile2",bd = 0,background="green")
    dealer_frame2.grid(row=5,column = 1,padx = 40,ipadx = 40)

    dealer_frame3 = LabelFrame(my_frame,text = "pile3",bd = 0,background="green")
    dealer_frame3.grid(row=5,column = 2,padx = 40,ipadx = 40)

    dealer_frame4 = LabelFrame(my_frame,text = "pile4",bd = 0,background="green")
    dealer_frame4.grid(row=5,column = 3,padx = 40,ipadx = 40)

    dealer_frame5 = LabelFrame(my_frame2,text = "pile5",bd = 0,background="green")
    dealer_frame5.grid(row=5,column = 0,padx = 40,ipadx = 40)

    dealer_frame6 = LabelFrame(my_frame2,text = "pile6",bd = 0,background="green")
    dealer_frame6.grid(row=5,column = 1,padx = 40,ipadx = 40)

    dealer_frame7 = LabelFrame(my_frame2,text = "pile7",bd = 0,background="green")
    dealer_frame7.grid(row=5,column = 2,padx  = 40,ipadx = 40)

    res_label_1 = Label(deck,image = "",bg = "green")
    res_label_1.pack(pady = 20)

    dealer_label_1 = Label(dealer_frame1,image = '',bg = "green")
    dealer_label_1.pack(pady = 20)

    dealer_label_2 = Label(dealer_frame2,image = "",bg = "green")
    dealer_label_2.pack(pady = 20)

    dealer_label_3 = Label(dealer_frame3,image = "",bg = "green")
    dealer_label_3.pack(pady = 20)

    dealer_label_4 = Label(dealer_frame4,image = "",bg = "green")
    dealer_label_4.pack(pady = 20)

    dealer_label_5 = Label(dealer_frame5,image = "",bg = "green")
    dealer_label_5.pack(pady = 20)

    dealer_label_6 = Label(dealer_frame6,image = "",bg = "green")
    dealer_label_6.pack(pady = 20)

    dealer_label_7 = Label(dealer_frame7,image = "",bg = "green")
    dealer_label_7.pack(pady = 20)

    
    def both_commands():
        res_open()
        play_music("shuffle.mp3")
        
    res_button = Button(root,text = "Get Cards",font = ("Helvetica",14),command = both_commands)
    res_button.pack(pady = 10)
    res_button.place(x=200, y=600)
    
def sec_window(card):
    
    global pic
    draw = tk.Tk()
    draw.title("result")
    draw.geometry("1900x1000")

    pic = tk.PhotoImage(file = card)
    label = tk.Label(draw,image = pic)
    label.place(x=0,y=0,relwidth = 1,relheight = 1)
    
        
def instructions():
    game_instructions_window = Tk()
    game_instructions_window.title("10-20-30 Game Instructions")
    game_instructions_window.geometry("1900x1000")

    instructions_label = tk.Label(game_instructions_window, text="Instructions:",font=("Arial", 12))
    instructions_label.pack()

    instructions_text = tk.Text(game_instructions_window, height=30, width=500,font = ("Helvetica",14),bg = "green")
    instructions_text.insert(tk.END, "Instructions:\n\n1. Deal seven cards, left to right forming seven piles.\n2. Play a card on the rightmost pile.\n3. Check the pile for any three card combinations that total 10, 20, or 30.\n4. Pick up the three cards and place them on the bottom of the deck.\n5. Continue picking up cards until no more sets of three can be picked up from the pile.\n6. If a pile contains only three cards that sum to 10, 20, or 30, the pile disappears.\n7. You win if all the piles disappear. You lose if you are unable to deal a card.\n8.If the state of game repeate itself then it is a draw.\n9.Have fun")
    instructions_text.config(state=tk.DISABLED)
    instructions_text.pack()

    ok_button = tk.Button(game_instructions_window, text="OK", command=game_instructions_window.destroy)
    ok_button.pack(pady = 10)
    
def start_command():
    generateRandomDeck()
    play_music("button.mp3")

img = PhotoImage(file = "start.png")
btopen = Button(w1,text = "start game",image = img,width = 100,height = 40,command = start_command).place(x = 750,y=600)

def game_command():
    instructions()
    play_music("button.mp3")
img_1 = PhotoImage(file = "inst_buttons.png")
btopen = Button(w1,text = "game rules",width = 100,image = img_1,height = 40,command = game_command).place(x = 590,y=600)

def test_command():
    cases()
    play_music("button.mp3")
img_2 = PhotoImage(file = "test_button.png")
btopen = Button(w1,text = "test cases",image = img_2,width = 100,height = 40,command = test_command).place(x = 900,y=600)



w1.mainloop()