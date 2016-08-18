
from non_alcoholic_data import parseData

def listOfReviewText(data):
    ''' if data is a list of dict for beer reviews, return list of review text'''
    return [d['review/text'] for d in data ]

def listOfLists(listOfStrings):
    result = []
    for s in listOfStrings:
        result.append(s.split())
    return result

def countWords(words):
    result = {}
    for w in words:
        try:
          result[w] = result[w] + 1
        except KeyError:
          result[w] = 1

    return result

def listOfWords(listOfLists):

    result = []
    for l in listOfLists:
        for w in l:
            result.append(w)
    return result


if __name__ == "__main__":
    data = list(parseData("http://jmcauley.ucsd.edu/cse255/data/beer/non-alcoholic-beer.json"))
    smallData = data[:10]

    allTheWords = listOfLists(listOfReviewText(smallData))
    words = listOfWords(allTheWords)
    wordCount = countWords(words)

        
