""" Inputs:
        (string) document = "many google employees can program"
        (string list) searchTerms = ["google", "program"]
    Output:
        (string) "google employees can program"

    Inputs:
        (string) document = "a b c d a"
        (string list) searchTerms = ["a", "c", "d"]
    Output:
        (string) "c d a"
    """

def answer(document, searchTerms):
    word_list = document.split()
    substring = ""
    terms = {}
    mn = 0
    mx = 0
    #step through list one at a time, noting position
    for idx, word in enumerate(word_list):
        # if the focused word is what we're looking for,
        # either add it to the dict, or check the length of the new spread
        if word in searchTerms:
            # if the string doesn't have all of our words yet,
            # add the word to our dict
            if not all(x in substring for x in searchTerms):
                terms.update({word: idx})
            # create new string from potential new distance
            # if the new string is shorter than the old, save it
            if all(x in substring for x in searchTerms):
                # first item not being looked at
                terms.update({word: idx})
                mn, mx = min_max(searchTerms, terms)
                temp = " ".join(word_list[terms[mn]:idx + 1])
                if len(temp.split()) < len(substring.split()):
                    substring = temp
            else:
                # build towards comparison items when not finished
                # mn and mx are the strings of the first and last items
                # in the string
                mn, mx = min_max(searchTerms, terms)
                substring = " ".join(word_list[terms[mn]:terms[mx] + 1])
    return substring

def min_max(l, d):
    mn = min(l, key=lambda i: d.get(i, float('inf')))
    mx = max(l, key=lambda i: d.get(i, float('-inf')))
    return (mn, mx)

# steps:
# walk through list.
# If present word in sT

#document = "many google employees can program"
#searchTerms = ["google", "program"]
#answer_phrase = "google employees can program"
document = "a b c d a"
searchTerms = ["a", "c", "d"]
answer_phrase = "c d a"
ans = answer(document, searchTerms)
print(ans)
print(ans == answer_phrase)
