# SpellChecker

def main():


       # 1. prompt user to give the name for spell check
       
       given_raw_name = raw_input("Please name the file.You don't need to add .txt")
       given_file_name = given_raw_name+'.txt'

       # given_raw_name = open('jabberwocky.txt','r')
       

       # 2. database
       fileName = 'engDictionary.txt'
       
       
       # 3-1 read the input file
       update_file = open(given_file_name,'r')
       update_lines = update_file.readlines()  
       print 'update_lines',update_lines


       # create new file
       checked_file_name =  given_raw_name + '-chk.txt'
       checked_file = open(checked_file_name,'w')
       
       # 4. loop user file
       for item in update_lines:  # loop though the whole dic by line
              x = []
              count = 0
              strip_line = item.strip('\n')
              s_s_line = strip_line.split()
              
              if s_s_line != []: # deal with every single line
                     for word_raw in s_s_line:  # loop though every string in one line 
                            word = ignoreCaseAndPunc(word_raw)  # get appropriate word as input
                            x.append(word)       # append into list firstly
                            count += 1
                            index = count-1
                            # transform into an appropriate input of word
                            in_dict = findWordInDictionary(word, fileName)
                            if in_dict == False:
                                   # start the conversation
                                   print 'The word',"'",word,"'",'is misspelled.'
                                   print 'The following suggestions are available.'

                                   # execture getCombinedWordSuggestions func to offer some choices
                                   choice_lst = getCombinedWordSuggestions(word,fileName)

                                   # There's no choice in the lst
                                   if len(choice_lst)==0:
                                          print 'There are 0 suggestions in our dictionary for this word.'
                                          choice = raw_input("Press 'a' for accept as is, 't' for type in manually.")
                                          while choice!='a' and choice!='t':
                                                 choice = raw_input("Press 'a' for accept as is, 't' for type in manually.")
                         
                                          if choice == 'a':
                                                 x[index]=word

                                          else:
                                                 type_manually = raw_input('Please type the word that will be used as the replacement in the output file')
                                                 x[index]= type_manually
                                                 # output word = type_manually
                                           
                                          
                                   # print out some decisions
                                   else:
                                          prettyPrint(choice_lst)
                                          choice = raw_input("Press 'r' for replace, 'a' for accept as is, 't' for type in manually.")
                                          # safely input
                                          while choice!='a' and choice!='t' and choice!='r':
                                                 choice = raw_input("Press 'r' for replace, 'a' for accept as is, 't' for type in manually.")
                                                 
                                          if choice == 'r':
                                                 print 'Your word will now be replaced with one of the suggestions.'
                                                 choice_r = input('Enter the number corresponding to the word that you want to use for replacement.')
                                                 while choice_r not in range(1,len(choice_lst)+1):
                                                        choice_r = input('Enter the number corresponding to the word that you want to use for replacement.')
                                                 
                                                 for num in range(0,len(choice_lst)):
                                                        if num+1 == choice_r:
                                                               #output word = choice_lst[num]
                                                               x[index]=choice_lst[num]
                                                               print 'x[index]:',x[index]
                                                        
                                          elif choice == 'a':
                                                 # output word = word
                                                 x[index]=word
                                                 

                                          else:
                                                 type_manually = raw_input('Please type the word that will be used as the replacement in the output file')
                                                 # output word = type_manually
                                                 x[index]=type_manually
              

                     print 'x:',x  # x should be ['the','happy','is','hi']
                            
                     for i in x:
                            checked_file.write(i)
                            checked_file.write(' ')
                            
                     checked_file.write('\n')

              else:
                     checked_file.write('\n')

       checked_file.close()
                                                 
       
'''
       ## execute findWordInDictionary
       is_infile = findWordInDictionary(word, fileName)
       print 'is in file or not: ',is_infile


       ## execute getWordsOfSimLength function
       sim_word_lst = getWordsOfSimLength('ging', 'oed.txt', 1)


       ## execute getWordsWithSameStart function
       wordList = ['ban','bang','gang','aa','mange']
       word_same_start = getWordsWithSameStart('ging',wordList,1)

       ## execute getWordsWithCommonLetters function
       word_com_let = getWordsWithCommonLetters('clang',wordList,3)

       ## execute getSimilarityMetric function
       average = getSimilarityMetric('oblige','oblivion')

       ## execute getSimilarityDict(word, wordList)
       D = getSimilarityDict(word, wordList)
'''




def ignoreCaseAndPunc(word_raw):
       '''
       (string)->(string)
       This function should be given an string s input then
       return a string that is entirely in lower case and
       all ounctuation removed
       
       >>> ignoreCaseAndPunc('Actually,')
       'actually'
       >>> ignoreCaseAndPunc('variables.')
       'variables'
       '''
       
       # lower the word
       word_lower = word_raw.lower()

       # strip any unwanted punc
       word_fixed = ''
       
       for i in word_lower:
              if i == '.'or i == ','or i == ':'or i == ';'or i == '!'or i == '?':
                     word_fixed += ''
              else:
                     word_fixed += i

       return word_fixed



def findWordInDictionary(word, fileName):
       '''(str,str)->bool
       This function used to check and see if the word is present in the
       fileName file. It's required to run ignoreCaseAndPinc func firstly.
       
       >>> findWordInDictionary('Africa', 'engDictionary.txt')
       True
       >>> findWordInDictionary('linsanity', 'engDictionary.txt')
       False
       
       '''
       # initialize variable enable to check whether the word exist in the file
       count = 0
       
       # read the file
       file_Name = open(fileName,'r')
       lines = file_Name.readlines()

       
       # run for loop to see if the word present in fileName
       for i in lines:
              i_stripped = i.strip().strip('\n')
       
              if i_stripped == word:
                     count += 1


       if count ==0:
              return False
       else:
              return True
              
             

def getWordsOfSimLength(word, fileName, n):
       '''(str,str,int)->list
       This function used as return a list of words form the fileName
       that all have the length +/- a value n.

       >>> getWordsOfSimLength('ging', 'oed.txt', 1)
       ['ban', 'bang', 'gang', 'mange']
       
       '''
       # initialize variable
       sim_word = ''
       sim_word_lst = []
       
       # readlines form fileName
       file_Name = open(fileName,'r')
       lines = file_Name.readlines()

       for j in lines:
              j_stripped = j.strip().strip('\n')
              if len(j_stripped) <=len(word)+n and len(j_stripped) >=len(word)-n:
                     sim_word = j_stripped
                     sim_word_lst.append(sim_word)
                     

       return sim_word_lst
                     
              


def getWordsWithSameStart(word,wordList,n):
       '''(str,lst,int)->list
       This function use a given word and a list of words
       return a list of words that have at least the first
       n characters the same.

       >>> getWordsWithSameStart('ging',['ban','bang','gang','mange'],1)
       ['gang']
       >>> getWordsWithSameStart('band', ['ban','bang','gang','mange'],2)
       ['ban', 'bang']
       '''
       
       # initialize necessary variables
       count = 0
       x = []
       
       for word_1 in wordList:
              count = 0
              for i in range(0,n):
                     if word[i]==word_1[i]:
                            count += 1
                     else:
                            count+=0
              if count >= n:
                     x.append(word_1)

       word_same_start = x

       return word_same_start
       
         

def getWordsWithCommonLetters(word,wordList,n):
       '''(str,list,int)->list
       This function should be given a word returns
       a list of words that have n or more letters in common.
       
       >>> getWordsWithCommonLetters('clang',['ban','bang','gang','aa','mange'],3)
       ['bang', 'gang', 'mange']
       >>> getWordsWithCommonLetters('immediate',['ban','bang','gang','aa','mange'],3)
       ['mange']
       '''
       
       # initialize variable
       x = []
       
       for word_1 in wordList:
              count = 0
              s = ''
              for j in word_1:
                     if j in word not in s:
                            s+=j
                            count += 1
                            #print 'count:',count
                     else:
                            s+=''
                            count += 0
               
                     
              if count >= n:
                     x.append(word_1)
                     
       word_com_let = x

       return word_com_let
              

def getSimilarityMetric(word1,word2):
       '''(str,str)->float
       This function use the given word1 and word2 to compute two
       measures of similarity and returns the average
       
       >>> getSimilarityMetric('oblige','oblivion')
       2.5
       >>> getSimilarityMetric('aghast','gross')
       1.5
       '''
       # initialize variable
       set_1 = []
       set_2 = []
       set_3 = [] # 3,4 for right
       set_4 = []
       
       # leftsimilarity

       for i in word1:
              set_1.append(i)


       for i in word2:
              set_2.append(i)


       ls = 0

       if len(set_1)<=len(set_2):
              for i in range(0,len(set_1)):
                     if set_1[i]==set_2[i]:
                            ls+=1
                     else:
                            ls+=0

       else:
              for i in range(0,len(set_2)):
                     if set_2[i]==set_1[i]:
                            ls+=1
                     else:
                            ls+=0


       ## rightsimilarity
       # reverse the order of the words

       for i in word1:
              set_3.append(i)

       set_3.reverse()
       #print set_3

       for i in word2:
              set_4.append(i)


       set_4.reverse()


       rs = 0

       if len(set_3)<=len(set_4):
              for i in range(0,len(set_3)):
                     if set_3[i]==set_4[i]:
                            rs+=1
                     else:
                            rs+=0

       else:
              for i in range(0,len(set_4)):
                     if set_4[i]==set_3[i]:
                            rs+=1
                     else:
                            rs+=0


       average = (ls+rs)/2.0

       return average





def getSimilarityDict(word, wordList):
       '''(str,list)->Dict
       This function use word and wordList to return a dictionary
       with individual words in wordList as keys and the return value
       of getSimilarityMetric function.
       unordered...dictionary
       >>> getSimilarityDict('band', ['ban','bang','gang','aa','mange'])
       {'ban': 1.5, 'aa': 0.5, 'bang': 3.0, 'gang': 2.0, 'mange': 1.0}
       '''
 
       D = {}
       
       # create key and value for the dict
       for key in wordList:
              D[key]= getSimilarityMetric(word,key)

       return D
       

'''

import doctest
doctest.testmod()  

'''

def getBestWords(D, n):
       '''(Dict,int)->list
       This function takes a similarityDictionary produced by
       the above function and it returns the top n in terms of
       the similarity
       
       >>> getBestWords({'ban': 1.5, 'aa': 0.5, 'bang': 3.0, 'gang': 2.0, 'mange': 1.0},2)
       ['bang', 'gang']
       '''
       # make dict into a list
       list_of_tuples = D.items()

       # create sortIn2D function used for cmp-->-1,0,1
       
       def sortIn2D(tup1,tup2):
              '''(tup,tup)->int
              This function use the two input tuples to create
              comparison value for sort function.

              >>> sortIn2D(('Harry',22),('Linda',25))
              -1
              >>> sortIn2D(('Harry',20),('Linda',15))
              1
              >>> sortIn2D(('Harry',22),('Linda',22))
              0
              '''
              if tup1[-1]<tup2[-1]:
                     return -1
              elif tup1[-1]==tup2[-1]:
                     return 0
              else:
                     return 1

       # sort the list according to similarity
       list_of_tuples.sort(sortIn2D,reverse=True)

       # create getListOfFirstComponents
       def getListOfFirstComponents(list_of_tuples):
              '''(list of tuples)->list
              This function takes in list_of_tuples and then
              returns another list which has the first components
              of the tuples.
              
              >>> getListOfFirstComponents([(1,2),(3,4)])
              [1, 3]
              '''
              # initilize variables
              emp_lst = []

              # take out first component from list of tuples
              for comp in list_of_tuples:
                     emp_lst.append(comp[0])
                     
              # print 'emp_lst:',emp_lst

              return emp_lst
       
       return getListOfFirstComponents(list_of_tuples)[0:n]


## function created for no.8 function

def getListOfFirstComponents(list_of_tuples):
              '''(list of tuples)->list
              This function takes in list_of_tuples and then
              returns another list which has the first components
              of the tuples.
              
              >>> getListOfFirstComponents([(1,2),(3,4)])
              [1, 3]
              '''
              # initilize variables
              emp_lst = []

              # take out first component from list of tuples
              for comp in list_of_tuples:
                     emp_lst.append(comp[0])
                     
              # print 'emp_lst:',emp_lst

              return emp_lst
       



def sortIn2D(tup1,tup2):
       '''(tup,tup)->int
       This function use the two input tuples to create
       comparison value for sort function.

       >>> sortIn2D(('Harry',22),('Linda',25))
       -1
       >>> sortIn2D(('Harry',20),('Linda',15))
       1
       >>> sortIn2D(('Harry',22),('Linda',22))
       0
       '''
       if tup1[-1]<tup2[-1]:
              return -1
       elif tup1[-1]==tup2[-1]:
              return 0
       else:
              return 1

## 9
def getWordSuggestionsV1(word, fileName, n, commonPercent, topN):
       '''(str,str,float,int)->lst
       given an incorrect word return a list of topN of
       legal word suggestion as per an algorithm given.
       Safely assume this function will only be called
       with a word that is not present in the dictionary.
       (should be stated in main function)
       (a) +/- n length.
       (b) have at least commonPercent% of the letters in common

       >>> getWordSuggestionsV1('ging', 'oed.txt', 1, 50, 2)
       ['gang','bang']
       '''
       
       # (a) +/- in length
       lst_after_a = getWordsOfSimLength(word, fileName, n)
       # print 'lst_after_a:',lst_after_a  (check)
       lst_select_b = []
       
       
       # (b) have at least commonPercent% of the letters in common
       
       for str_b in lst_after_a:
              count = 0
              s = ''
              for j in str_b:
                     jInWord = j in word
                     jInS = j in s
                     if jInWord==True and jInS==False:
                            s+=j
                            count += 1
                            #print 'count:',count 
                     else:
                            s+=''
                            count += 0
               
              if len(str_b)<=len(word):
                     # Percent should be 0-100
                     Percent = (count/float(len(word)))*100
                     # print 'Percent for str_b<word:',Percent (check)
                     if Percent>=commonPercent:
                            lst_select_b.append(str_b)
                            

              else:
                     Percent = (count/float(len(str_b)))*100
                     # print 'Percent for str_b>word:',Percent (check)
                     if Percent>=commonPercent:
                            lst_select_b.append(str_b)
                            
       
       # choose topN number from lst_select_b
       # order lst based on similarity metric
       sim_dict = getSimilarityDict(word,lst_select_b)
       topN_sug = getBestWords(sim_dict,topN)


       return topN_sug
                     

##10                     
def getWordSuggestionsV2(word, fileName, n, topN):
       '''(str,str,int,int)->list
       This function used word and return a list of word
       suggestions that can all be found the file provided
       by fileName based on the algorithm.
       
       >>> getWordSuggestionsV2('biger', 'engDictionary.txt', 2, 2)
       ['bigger', 'biker',.....]
       '''
       # initialize
       lst_select = []
       
       # 1. find words within +/- 1 in length w.r.t word
       lst_after_1 = getWordsOfSimLength(word, fileName, 1)
       

       # 2. find words begin with the same n letters as the given word
       lst_after_2 = getWordsWithSameStart(word,lst_after_1,n)
       
       
       # 3. find words that end with the same n letters as the given word
       # create getwordsWithSameEnd firstly
       def getWordsWithSameEnd(word,wordList,n):
              '''(str,list,int)->list

              >>> getWordsWithSameEnd('ging',['ban','bang','gang','aa','mange'],1)
              ['bang', 'gang']
              '''
              count = 0
              x = []
              
              for word_2 in wordList:
                     count = 0
                     for i in range(0,n):
                            word_r = word[::-1]
                            word_2_r = word_2[::-1]
                            if word_r[i]== word_2_r[i]:
                                   count += 1
                            else:
                                   count+=0
                     if count >= n:
                            x.append(word_2)
              word_same_end = x

              return word_same_end     

       # execute
       lst_after_3 = getWordsWithSameStart(word,lst_after_2,n)
       # print 'lst_after_3:', lst_after_3 (check)
       
       # order the list based on the word similarity measure
       sim_dict_V2 = getSimilarityDict(word,lst_after_3)  
       topN_sug_V2 = getBestWords(sim_dict_V2,topN)
       
       return topN_sug_V2
       

# 11
def getCombinedWordSuggestions(word,fileName):
       '''(str,str)->list
       This function combined the list of suggestions provided
       by the two functions above in the following manner.
       Take 7 suggestions from each function. Use 75% as the threshold
       for the first algorithm.

       >>> getCombinedWordSuggestions('paul','engDictionary.txt')
       ['pail', 'haul', 'pall', 'plug', 'pats', 'peel', 'pals', 'past', 'palm', 'pass']
       
       '''
       
       lst1 = getWordSuggestionsV1(word,fileName,2,75,7) # 75% in common

       lst2 = getWordSuggestionsV2(word,fileName,1,7)


       # (a) combine the two list and remove duplicates
       lst_total = lst1 + lst2
       selected_lst = []

       for item in lst_total:
              if item not in selected_lst:
                     selected_lst.append(item)

       

       # (b) rank this new list using getSimilarityDict and getBestWords
       Dict_after_sim = getSimilarityDict(word, selected_lst)  # getSimilarityDict returns dict

       # (b) by getBestWords
       lst_after_BW = getBestWords(Dict_after_sim,10)

       return lst_after_BW

       
# 12

def prettyPrint(lst):
       '''
       This function help user identify the suggestion with a number.
       >>> prettyPrint(['biker','tiger','bigger'])
       1. biker
       2. tiger
       3. bigger
       '''
       
       for num in range(0,len(lst)):
              print num+1,'.',lst[num]
       
       
              
 
