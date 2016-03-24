# Racko game
import random

def main():
       
       
       # create a list of integers that represents a deck
       deck = [56, 57, 29, 58, 34, 37, 7, 22, 52, 35, 48, 44, 3, 47, 59, 32, 51, 4, 30, 13, 28, 12, 23, 33, 36, 50, 39, 6, 43, 14, 45, 31, 15, 27, 19, 11, 21, 17, 40, 49, 5, 18, 41, 25, 38, 2, 54, 46, 8, 9, 10, 24, 55, 53, 42, 26, 20, 60, 16, 1]
       random.shuffle(deck)
       # create an empty discard pile
       discard = []

       # execute shuffle function
       shuffle(deck,discard)

       
       # create two hands for computer and user by deal_initial_hands function
       # hands is a tuple
       hands = deal_initial_hands(deck)


       # assign one element of this tuple as the user's hand
       # assign the other element of the tuple as computer's hand
       AI_hand = hands[0]
       user_hand = hands[1]


       # test racko 
       whether_user = check_racko_user(user_hand)
       whether_AI = check_racko_AI(AI_hand)

       # print out user_hand in vertical form       
       print_top_to_bottom_user(user_hand)

       # reveal one card to start the discard pile
       new_card = get_top_card_deck(deck)
       discard.append(new_card)
       print 'started discard pile:',discard
       print '\n'
       
             
       # start while loop
       # while nobody has racko(use check_racko function)
       
       while (check_racko_user(user_hand) or check_racko_AI(AI_hand))!=True:
              
              print 'user turn'
              # user plays first
              # ask the user if they want this card in discard pile
              print 'card from top of the discard pile:',discard[len(discard)-1]  # show discard pile
              user_ans = raw_input('Do you want this card in discard pile? Please type in Yes or No.')
              while user_ans != 'Yes' and user_ans !='No':
                            print 'Please type in Yes or No'
                            user_ans = raw_input('Do you want this card in discard pile? Please type in Yes or No.')
              if user_ans == 'Yes':
                     # ask the user for the card(number) they want to kick out (must initialize card_to_ve_replaced)
                     card_to_be_replaced = input('Which card in your hand that you want to kick out? Please enter the card number.')
                     while card_to_be_replaced not in user_hand:
                            print 'This card does not exist in your hand. Please ensure that this card is in your hand.'
                            card_to_be_replaced = input('Which card in your hand that you want to kick out? Please enter the card number.') 

                     # modify user's hand and discard pile
                     new_card = discard.pop()
                     find_and_replace(new_card,card_to_be_replaced,user_hand,discard)
                     add_card_to_discard(card_to_be_replaced, discard)

                     #print the user's hand in vertical form like a stack
                     print ''
                     print_top_to_bottom_user(user_hand)
                     
              elif user_ans == 'No':
                     # if the ans is No, then user choose deck's top card
                     new_card = get_top_card_deck(deck)
                     
                     # print this card from deck to show the answer they got
                     print 'Card from deck:', new_card

                     # ask the user if they want this card
                     secondChoice = raw_input('Do you want to keep this card?(from the deck pile)')
                     while secondChoice != 'Yes' and secondChoice !='No':
                            print 'Please type in Yes or No'
                            secondChoice = raw_input('Do you want to keep this card?(from the deck pile)')

                     if secondChoice == 'Yes':
                            # ask kick out
                            
                            # ask the user for the card(number) they want to kick out (must initialize card_to_ve_replaced)
                            card_to_be_replaced = input('Which card in your hand that you want to kick out? Please enter the card number.')
                            while card_to_be_replaced not in user_hand:
                                   print 'This card does not exist in your hand. Please ensure that this card is in your hand.'
                                   card_to_be_replaced = input('Which card in your hand that you want to kick out? Please enter the card number.') 

                            # modify user's hand and discard pile
                            find_and_replace(new_card,card_to_be_replaced,user_hand,discard)
                            add_card_to_discard(card_to_be_replaced, discard)

                            # print user's hand in vertical form
                            print ''
                            print_top_to_bottom_user(user_hand)
              
                     else:
                            # Add the top card of the deck to discard pile
                            discard.append(new_card)
                            # print the user's hand
                            print ''
                            print 'users hand:',user_hand
                            print_top_to_bottom_user(user_hand)

              if check_racko_user(user_hand)==True:
                     print '\n'
                     print 'Rack-O! user wins'
                     print 'This is your final hand!'
                     print_top_to_bottom_user(user_hand)
                     break
              print ''
              print "It is AI's turn"
              #print_top_to_bottom_AI(AI_hand)  (Don't print out AI's hand)
              print "AI finished this turn.\n"
              computer_play(AI_hand, deck, discard)  # need to be modify
              
              # check and make sure there are still some cards in the deck
              # else reshuffle the discard and restart
              shuffle(deck,discard)

       # print out AI's hand only if the computer wins
       if check_racko_AI(AI_hand)==True and check_racko_user(user_hand)==False:
              print 'Rack-O! Computer wins'
              print 'AI hand looks like this.'
              print_top_to_bottom_AI(AI_hand)

         
def computer_play(AI_hand,deck,discard):

       
       # divide AI_list into six part
       Slot10= AI_hand[0]  # correspond to s[54:] 
       Slot9 = AI_hand[1]  # s[48:54]
       Slot8 = AI_hand[2]  # s[42:48] 
       Slot7 = AI_hand[3]  # s[36:42]
       Slot6 = AI_hand[4]  # s[30:36]
       Slot5 = AI_hand[5]  # s[24:30]
       Slot4 = AI_hand[6]  # s[18:24]
       Slot3 = AI_hand[7]  # s[12:18]
       Slot2 = AI_hand[8]  # s[6:12]
       Slot1 = AI_hand[9]  # s[0:6]

       # create list of 1-60
       s = []
       for i in range(1,61):
           s.append(i)
           
       # determine whether to take the discard-pile card
       new_card = discard[-1]
       whether_take = whether_to_take_card(new_card,s,Slot10,Slot9,Slot8,Slot7,Slot6,Slot5,Slot4,Slot3,Slot2,Slot1)
    
       # if computer have to take discard
       if (whether_take == True):
              # shown the discard to AI
              new_card = discard[-1]
       
              # determine which slot should insert card_be_replaced
              # modify AI's hand (AI pop and AI insert)
              card_be_replaced = find_and_replace_AI(new_card,AI_hand,discard,s,Slot10,Slot9,Slot8,Slot7,Slot6,Slot5,Slot4,Slot3,Slot2,Slot1)
              

              # modify discard pile 
              discard.pop()  # (-) form discard top
              add_card_to_discard_AI(card_be_replaced, discard) # (-) add card_be_replaced from AI_hand
              # print_top_to_bottom_AI(AI_hand) only print if AI wins

              
           
       # if AI not to take discard 
       else:
              #if AI not take discard, then AI choose deck's top card (or keep)
              new_card = get_top_card_deck(deck) # new card is the top of the deck

              # determine whether to take deck card
              whether_take = whether_to_take_card(new_card,s,Slot10,Slot9,Slot8,Slot7,Slot6,Slot5,Slot4,Slot3,Slot2,Slot1)
              
              
              # new_card fit the previously index of keeping card-->take it
              if (whether_take == True):
                     # determine slot to insert card_be_replaced (by fin_and_replaced function)
                     # modify AI's hand
                     card_be_replaced = find_and_replace_AI(new_card,AI_hand,discard,s,Slot10,Slot9,Slot8,Slot7,Slot6,Slot5,Slot4,Slot3,Slot2,Slot1)

                     # modify deck
                     add_card_to_discard_AI(card_be_replaced, discard) #(+) discard the card to be replaced
                                         

              else:  # not to take card from deck
                     discard.append(new_card)  #(+) top of deck card to discard
                     
                     # print the AI's hand

                     

              
              
## AI's subfunction
def whether_to_take_card(new_card,s,Slot10,Slot9,Slot8,Slot7,Slot6,Slot5,Slot4,Slot3,Slot2,Slot1):
       '''
           (new_card,s,lst_num,whether_take)-->  boolean 
       '''
       
       # once receive a new card, no matter from discard or deck
       # check the new card's slot, if the original card in the slot is already in an appropriate range
       # not to take the card
       # vice cersa
       if new_card in s[54:]:
              if Slot10 in s[54:]:
                     whether_take = False
              else:
                     whether_take = True
                     
              return whether_take
      
       elif new_card in s[48:54]:
              if Slot9 in s[48:54]:
                     whether_take = False
              else:
                     whether_take = True
                     
              return whether_take
       
       elif new_card in s[42:48]:
              if Slot8 in s[42:48]:
                     whether_take = False
              else:
                     whether_take = True
                     
              return whether_take
      
       elif new_card in s[36:42]:
              if Slot7 in s[36:42]:
                     whether_take = False
              else:
                     whether_take = True
                     
              return whether_take
      
       elif new_card in s[30:36]:
              if Slot6 in s[30:36]:
                     whether_take = False
              else:
                     whether_take = True
                     
              return whether_take

       elif new_card in s[24:30]:
              if Slot5 in s[24:30]:
                     whether_take = False
              else:
                     whether_take = True
                     
              return whether_take
      
       elif new_card in s[18:24]:
              if Slot4 in s[18:24]:
                     whether_take = False
              else:
                     whether_take = True
                     
              return whether_take

       elif new_card in s[12:18]:
              if Slot3 in s[12:18]:
                     whether_take = False
              else:
                     whether_take = True
                     
              return whether_take
      
       elif new_card in s[6:12]:
              if Slot2 in s[6:12]:
                     whether_take = False
              else:
                     whether_take = True
                     
              return whether_take
      
       elif new_card in s[0:6]:
              if Slot1 in s[0:6]:
                     whether_take = False
              else:
                     whether_take = True
                     
              return whether_take
       
       else:
              whether_take = False
              return whether_take

           
def find_and_replace_AI(new_card,AI_hand,discard,s,Slot10,Slot9,Slot8,Slot7,Slot6,Slot5,Slot4,Slot3,Slot2,Slot1):
       '''
       find and replace card in user's hand
       '''

       
       # determine which slot insert card_to_be_replaced
       if new_card in s[54:]:
              kick = AI_hand.pop(0)
              AI_hand.insert(0,new_card)
       elif new_card in s[48:54]:
              kick = AI_hand.pop(1)
              AI_hand.insert(1,new_card)
       
       elif new_card in s[42:48]:
              kick = AI_hand.pop(2)
              AI_hand.insert(2,new_card)
              
       elif new_card in s[36:42]:
              kick = AI_hand.pop(3)
              AI_hand.insert(3,new_card)
               
       elif new_card in s[30:36]:
              kick = AI_hand.pop(4)
              AI_hand.insert(4,new_card)
              
       elif new_card in s[24:30]:
              kick = AI_hand.pop(5)
              AI_hand.insert(5,new_card)
              
       elif new_card in s[18:24]:
              kick = AI_hand.pop(6)
              AI_hand.insert(6,new_card)
              
       elif new_card in s[12:18]:
              kick =  AI_hand.pop(7)
              AI_hand.insert(7,new_card)
               
       elif new_card in s[6:12]:
              kick = AI_hand.pop(8)
              AI_hand.insert(8,new_card)
       
       elif new_card in s[0:6]:
              kick = AI_hand.pop(9)
              AI_hand.insert(9,new_card)
               
       else:
              print 'error'

       return kick



def add_card_to_discard_AI(card_be_replaced,discard):
       '''
       add the card(integer) to the top of the discard pile
       '''
       discard.append(card_be_replaced)  # discard (+) the card kick out by the user



def print_top_to_bottom_AI(AI_hand):
       print 'The hand for computer:'
       for i in AI_hand:
              print i
              
             
                      
## user's sub function       

def shuffle(deck,discard):
       '''
       for i in range(1,61):
              deck = deck+[i]

       random.shuffle(deck)
       '''
       
       
       if len(deck)<=0:
              deck.extend(discard)
              print deck
              discard = []
              random.shuffle(deck)
              random.shuffle(discard)
       

              

                    
def check_racko_AI(AI_hand):
       '''
       (list) --> boolean
       This function determine whether Racko achieved or not.
       rack needed to be specified as AI_hand or user_hand
       '''
       
       i = 0
       while AI_hand[i]>AI_hand[i+1]:
              if i > 7 and AI_hand[i]>AI_hand[i+1]:
                     return True
                     break
             
              else:
                     i=i+1  
       
       return False

      
def check_racko_user(user_hand):
       '''
       (list) --> boolean
       This function determine whether Racko achieved or not.
       rack needed to be specified as AI_hand or user_hand
       '''
       # use while loop to check the order of the cards
       j = 0
       while user_hand[j]>user_hand[j+1]:
              if j > 7 and user_hand[j]>user_hand[j+1]:
                     return True
                     break
              else:
                     j=j+1

       return False



def get_top_card_deck(deck):
       '''
       (list)-->int
       The integer means the value of the card which got from top of
       the deck or discard pile.
       '''
       card = deck.pop()
       return card


def get_top_card_discard(discard,new_card):
       '''
       Add top card of the deck to discard pile when user or computer choose deck's card 
       '''
       discard.append(new_card)
       top_of_discard = discard[-1]
       
       return top_of_discard



def deal_initial_hands(deck):
       '''
       (list)-->(list1,list2)
       This function dealt two hands of 10 cards for computer and user
       individually.Computer get dealt firstly.
       '''
       AI_hand = []
       user_hand = []
       for card_num in range(1,21,2):
              
              # computer dealt turn: take one card from the deck for computer player
              AI_hand.append(deck[len(deck)-1])
              get_top_card_deck(deck)
   
              # user dealt turn: take one card from the deck for user player
              user_hand.append(deck[len(deck)-1])
              get_top_card_deck(deck)
              

       return (AI_hand,user_hand)

       
def print_top_to_bottom_user(user_hand):
       '''
       print user hand in vertical way to be like stack
       '''
       print 'The hand for user:'
       for user_i in user_hand:
              print user_i

             



def find_and_replace(new_card,card_to_be_replaced,user_hand,discard):
       '''
       find and replace card in user's hand
       '''
       index = 0
       
       # find index for the kick out
       for i in user_hand:
              if i!= card_to_be_replaced:
                     index+=1
              else:
                     break
      

       # modify user's hand      
       user_hand.remove(card_to_be_replaced)
       user_hand.insert(index,new_card)
       



def add_card_to_discard(card_to_be_replaced,discard):
       '''
       add the card(integer) to the top of the discard pile
       '''
       discard.append(card_to_be_replaced)  # discard (+) the card kick out by the user
      

if __name__ == '__main__':
       main()       
