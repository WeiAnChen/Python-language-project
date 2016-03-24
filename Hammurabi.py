import random

def print_intro( ):

       print '''Congrats, you are the newest ruler of ancient Samaria, elected for a ten year term
of office. Your duties are to distribute food, direct farming, and buy and sell land
as needed to support your people. Watch out for rat infestations and the resultant
plague! Grain is the general currency, measured in bushels. The following will help
you in your decisions:\n

(a) Each person needs at least 20 bushels of grain per year to survive.
(b) Each person can farm at most 10 acres of land.
(c) It takes 2 bushels of grain to farm an acre of land.
(d) The market price for land fluctuates yearly.\n

Rule wisely and you will be showered with appreciation at the end of your term. Rule
poorly and you will be kicked out of office!
'''

def Hammurabi():
       starved = 0
       immigrants = 5
       population = 100
       harvest = 3000  # total bushels harvested        
       bushels_per_acre = 3  # amount harvested for each acre planted
       rats_ate = 200  # bushels destroyed by rats
       bushels_in_storage = 2800
       acres_owned = 1000
       cost_per_acre = 19  # each acre costs this many bushels
       plague_deaths = 0
       acres = 0
       year_num = 1
       
       print_intro()


       # year loop
       for year_num in range(1,11):
              print 'O great Hammurabi!'
              print 'You are in year','<', year_num,'>','of your ten year rule.'
              print 'In the previous year','<', starved,'>','people starved to death.'
              print 'In the previous year','<', immigrants,'>','people entered the kingdom.'
              print 'The population is now','<',population,'>','.'
              print 'We harvested','<',harvest,'>','at', '<',bushels_per_acre,'>','bushels per acre.'
              print 'Rats destroyed','<',rats_ate,'>','bushels, leaving','<',bushels_in_storage,'>','bushels in storage.'
              print 'The city owns', '<',acres_owned,'>','acres of land.'
              print 'Land is currently worth','<', cost_per_acre,'>','bushels per acre.'
              print 'There were','<',plague_deaths,'>','deaths form the plague.'

              print '\n'
              

              # bushels and cost are used within functions
              bushels = bushels_in_storage   
              cost = cost_per_acre

              
              ## Ask four questions to get variables for the following functions
              ## Ex. is_plague, num_starving...
              
              # The 1st question
              acres = ask_to_buy_land(bushels,cost)

              # update acres_owned, bushels after the 1st question
              acres_owned += acres  # if buying land, using plus acres
              bushels = bushels-acres*cost


              #The 2nd question
              if acres==0:  # execute 2nd question only when we did not buy land
                     acres = ask_to_sell_land(acres,acres_owned)
                     # update acres_owned, bushels after 1st question
                     acres_owned -= acres  # if selling land, using substract acres
                     bushels = bushels + acres*cost
                     
              

              #The 3rd question
              grain_feed = ask_to_feed(bushels)
              bushels = bushels-grain_feed
              
              
              #The 4th question
              acres_to_plant = ask_to_cultivate(acres,population,bushels,acres_owned)
              bushels = bushels - acres_to_plant*2  # plant 1 acre of land takes 2 bushels

       
              print ''

              
              ## plague happens or not
              #is_plague() # call is_plague function
              #print 'is_plague returns', is_plague()
              if is_plague() == True:
                     plague_deaths = 0.5*population
                     plague_deaths = int(plague_deaths)
                     # update population
                     population = population - plague_deaths
              else:
                     plague_deaths = 0
                     population = population - plague_deaths


              ## How many people starved?
              starved = num_starving(population, grain_feed) # call num_starving function
              # if starvation is too serious, larger than 45% of the population --> kick out 
              if starved>0.45*population:
                     print 'O Hammurabi, you are a bad king.', int(starved),'people are starved to death','You lose!'
                     break
              # if not, update variables starved and population
              starved = int(starved)
              population = population - starved

              
              ## How many immigrants move into this country?
              grain_in_storage = bushels # I change variable-bushels into grain_in_storage for num_immigrants function
              # call num_immigrant function
              immigrants = num_immigrants(acres_owned,grain_in_storage, population, starved)
              # update population
              immigrants = int(immigrants)
              population = population + immigrants
              

              ## How good the harvest is?
              # call get_harvest function-->returns a random number
              bushels_per_acre = get_harvest()
              # update variable harvest and grain_in_storage
              harvest = bushels_per_acre*acres_to_plant
              grain_in_storage += harvest

 
              ## rat ruin and extent of rats damaged
              # call do_rats_infest function
              #do_rats_infest()
              
              if do_rats_infest()== True: # rat ruin will happen or not
                     # destroy_area is a decimal number between 0.1 to 0.3
                     # destroy_area = percent_destroyed()
                     rats_ate = percent_destroyed()*grain_in_storage
              else:
                     rats_ate = 0
              # update variables rats_ate, bushels_in_storage
              rats_ate = int(rats_ate)      
              grain_in_storage -= rats_ate
              bushels_in_storage = grain_in_storage


              ## how much land costs next year
              cost_per_acre = price_of_land()



              ## turn population into an integer number
              population = int(population)

              
              print '\n'

       # print out evaluation for winners(out of for loop)
       if starved<=0.45*population:
              print 'O great Hammurabi! You are a great king. Your hard working on allocation has made a',population,'civilization country.'
              print 'Also, your kingdom owns',acres_owned,'acres of land.','These records made you pass the ten-year trial and would keep the history. Congrats!'
       

def ask_to_buy_land(bushels, cost):
       
       '''Ask user how many bushels to spend buying land.'''
       acres = input('How many acres of land to buy?')
       while acres*cost>bushels:
              print"O great Hammurabi, we have but", bushels,'bushels of grain!'
              acres = input('How many acres of land to buy?')
       while acres<0:
              print"O great Hammurabi, we can not buy negative number of bushels of grain."
              acres = input('How many acres of land to buy?')
       
       return acres


def ask_to_sell_land(acres,acres_owned):
       
       '''Ask user how much land they want to sell.'''
       acres = input('How many acres of land to sell?')
       while acres>acres_owned:
              print'O great Hammurabi, we have but', int(acres_owned),'acres of the land.'
              acres = input('How many acres of land to sell?')      
       while acres<0:
              print"O great Hammurabi, we can not sell negative number of bushels of grain."
              acres = input('How many acres of land to sell?')   
       return acres


def ask_to_feed(bushels):
       
       '''Ask user how many bushels they want to use for feeding.'''
       grain_feed = input('How much grain to feed the people?')
       while grain_feed>bushels:
              print"O great Hammurabi, we have but", int(bushels),'bushels of grain!'
              grain_feed = input('How much grain to feed the people?')
       while grain_feed<0:
              print"O great Hammurabi, we can not feed negative number of bushels of grain."
              grain_feed = input('How much grain to feed the people?')
       return grain_feed

def ask_to_cultivate(acres, population, bushels, acres_owned):
       '''Ask user how much land they want to plant seed in.'''
       acres_to_plant = input('How many acres to plant with seed?')
       while acres_to_plant*2>bushels:
              print"O great Hammurabi, we have but", int(bushels),'bushels of grain!'
              acres_to_plant = input('How many acres to plant with seed?')
       while acres_to_plant > acres_owned:
              print"O great Hammurabi, we have but", int(acres_owned),'acres of land!'
              acres_to_plant = input('How many acres to plant with seed?')            
       while acres_to_plant>population*10:
              print"O great Hammurabi, we have but", int(population),'people to plant with seed.'
              acres_to_plant = input('How many acres to plant with seed?')
       while acres_to_plant<0:
              print"O great Hammurabi, we can not plant negative number of acres of land."
              acres_to_plant = input('How many acres of land to buy?')
              
       return acres_to_plant


# If there is a plague

def is_plague():
       '''
          This function should return a boolean by using die variable to determine
          the probability of plague happening.
          (int)--> boolean
              
       '''
       # die is a integer random between 1 to 100
       die = random.randint(1,100)
       #print 'die is', die
       # There is a 15% of probability that plague would happen
       if (die<=15 and die>=1):
              return True
       else:
              return False

# How many people starved
def num_starving(population,grain_feed):
       '''
       This function returns an integer gives the number of people starved
       '''
       if population*20>grain_feed:
              starved = (population*20-grain_feed)/20.0
              return starved                                  
       else:
              starved = 0
              return starved


# How many people came to the city 
def num_immigrants(acres_owned, grain_in_storage, population, starved):
       '''
       (number,number,number,number)-->number
       This function returns a number of immigrants come to this country
       '''
       if starved == 0:
              immigrants = float((20*acres_owned+ grain_in_storage))/(100*population+1)        
       else:
              immigrants = 0
              
       return immigrants


# How good the harvest is?
def get_harvest():
       '''
       -->int
       This function returns a random number between 1 to 8.
       It means the number of grain harvest per acre for each year.
       '''
       bushels_per_acre = random.randint(1,8)
       return bushels_per_acre


# whether or not rats ruin bushels
def do_rats_infest():
       '''
       This function returns boolean to determine whether rats would ruin grains or not this year
       ()-->boolean
       '''
       ruin_rand = random.randint(1,100)
       #print 'ruin_rand is', ruin_rand
       # There should be a probability of 40% for rats to ruin grains each year.
       if (ruin_rand<=40 and ruin_rand>=1):
              return True
       else:
              return False

# more about rat damaged(How seriously)
def percent_destroyed():
       '''
       This function returns a random decimal number between 0.1 to 0.3.
       ()--> number
       '''
       destroy_rand = random.randint(10,30)
       destroy_area = destroy_rand/100.0
       return destroy_area

       
# land cost next year
def price_of_land():
       '''
       ()-->(16,22)
       This function returns a random value from 16 to 22.
       '''
       cost_per_acre = random.randint(16,22)
       return cost_per_acre
       
            
              




              
              
              
       
