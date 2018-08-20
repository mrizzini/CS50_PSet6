import nltk


def lines(a, b):
    """Return lines in both a and b"""
    aList = a.split('\n')
    bList = b.split('\n')
    similarList = []

    for i in range(len(bList)):
        if bList[i] in aList:
            if bList[i] not in similarList:
                similarList.append(bList[i])

    # TODO
    return similarList


def sentences(a, b):
    """Return sentences in both a and b"""

    aSentences = nltk.sent_tokenize(a)
    bSentences = nltk.sent_tokenize(b)
    similarSentences = []

    for i in range(len(bSentences)):
        if bSentences[i] in aSentences:
            if bSentences[i] not in similarSentences:
                similarSentences.append(bSentences[i])

    # TODO
    return similarSentences


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    length = n
    aList = []

    for i in range(len(a) - (length - 1)):
        aList.append(a[i:(i + length)])

    bList = []

    for i in range(len(b) - (length - 1)):
        bList.append(b[i:(i + length)])

    similarSubstrings = []

    for i in range(len(bList)):
        if bList[i] in aList:
            if bList[i] not in similarSubstrings:
                similarSubstrings.append(bList[i])

    # TODO
    return similarSubstrings
