import unittest
import spellChecker

class test_spellChecker(unittest.TestCase):
       #1
       def test_ignoreCaseAndPunc_1(self):
              actual = spellChecker.ignoreCaseAndPunc('Actually,')
              expected = 'actually'
              self.assertEqual(actual,expected)

       def test_ignoreCaseAndPunc_2(self):
              actual = spellChecker.ignoreCaseAndPunc('variables.')
              expected = 'variables'
              self.assertEqual(actual,expected)
       #2
       def test_findWordInDictionary_1(self):
              actual = spellChecker.findWordInDictionary('Africa', 'engDictionary.txt')
              expected = True
              self.assertEqual(actual,expected)

       def test_findWordInDictionary_2(self):
              actual = spellChecker.findWordInDictionary('linsanity', 'engDictionary.txt')
              expected = False
              self.assertEqual(actual,expected)
       #3
       def test_getWordsOfSimLength(self):
              actual = spellChecker.getWordsOfSimLength('ging', 'oed.txt', 1)
              expected = ['ban', 'bang', 'gang', 'mange']
              self.assertEqual(actual,expected)
       #4
       def test_getWordsWithSameStart_1(self):
              actual = spellChecker.getWordsWithSameStart('ging',['ban','bang','gang','mange'],1)
              expected = ['gang']
              self.assertEqual(actual,expected)

       def test_getWordsWithSameStart_2(self):
              actual = spellChecker.getWordsWithSameStart('band', ['ban','bang','gang','mange'],2)
              expected = ['ban', 'bang']
              self.assertEqual(actual,expected)
       #5
       def test_getWordsWithCommonLetters_1(self):
              actual = spellChecker.getWordsWithCommonLetters('clang',['ban','bang','gang','aa','mange'],3)
              expected = ['bang', 'gang', 'mange']
              self.assertEqual(actual,expected)

       def test_getWordsWithCommonLetters_2(self):
              actual = spellChecker.getWordsWithCommonLetters('immediate',['ban','bang','gang','aa','mange'],3)
              expected = ['mange']
              self.assertEqual(actual,expected)

       #6
       def test_getSimilarityMetric_1(self):
              actual = spellChecker.getSimilarityMetric('oblige','oblivion')
              expected = 2.5
              self.assertEqual(actual,expected)
              
       def test_getSimilarityMetric(self):
              actual = spellChecker.getSimilarityMetric('aghast','gross')
              expected = 1.5
              self.assertEqual(actual,expected)
       
       #7
       def test_getSimilarityDict(self):
              actual = spellChecker.getSimilarityDict('band', ['ban','bang','gang','aa','mange'])
              expected = {'ban': 1.5, 'aa': 0.5, 'bang': 3.0, 'gang': 2.0, 'mange': 1.0}
              self.assertEqual(actual,expected)

       #8
       def test_getBestWords(self):
              actual = spellChecker.getBestWords({'ban': 1.5, 'aa': 0.5, 'bang': 3.0, 'gang': 2.0, 'mange': 1.0},2)
              expected = ['bang', 'gang']
              self.assertEqual(actual,expected)

       #9
       def test_getWordSuggestionsV1(self):
              actual = spellChecker.getWordSuggestionsV1('ging', 'oed.txt', 1, 50, 2)
              expected = ['gang','bang']
              self.assertEqual(actual,expected)

       #10
       def test_getWordSuggestionsV2(self):
              actual = spellChecker.getWordSuggestionsV2('biger', 'engDictionary.txt', 2, 2)
              expected = ['biker', 'biter']
              self.assertEqual(actual,expected)
       #11
       def test_getCombinedWordSuggestions(self):
              actual = spellChecker.getCombinedWordSuggestions('paul','engDictionary.txt')
              expected = ['pail', 'haul', 'pall', 'plug', 'pats', 'peel', 'pals', 'past', 'palm', 'pass']
              self.assertEqual(actual,expected)

       #12
       def test_sortIn2D(self):
              actual = spellChecker.sortIn2D(('Harry',22),('Linda',25))
              expected = -1
              self.assertEqual(actual,expected)
              actual2 = spellChecker.sortIn2D(('Harry',20),('Linda',15))
              expected2 = 1
              self.assertEqual(actual2,expected2)
              actual3 = spellChecker.sortIn2D(('Harry',22),('Linda',22))
              expected3 = 0
              self.assertEqual(actual3,expected3)
       
      #13
       def test_getListOfFirstComponents(self):
              actual = spellChecker.getListOfFirstComponents([(1,2),(3,4)])
              expected = [1, 3]
              


if __name__ == '__main__':
    unittest.main()

              
