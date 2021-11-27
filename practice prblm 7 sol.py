"""

                                            SEARCH ENGINE

You are given few sentences as a list [PYTHON LIST OF SENTENCE]. Take a query as an input from the user.
You have to pull out the sentences matching this query inputted from the user in decreasing order of relevance.
Most relevant sentence is the one with the maximum number of matching words with the query.

sentence = ["This is good", "python is good", "python is not python snake"]

Input:
Please input your query string
"python"

Output:
3 results found
1. python is not python snake
2. python is good
3. This is python
"""


def Matching_words(sentence1, sentence2):
    found1 = sentence1.split()
    found2 = sentence2.split()
    match = 0
    for word1 in found1:
        for word2 in found2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                match += 1
    return match


if __name__ == '__main__':
    # print(Matching_words("This is good", "python is good"))
#     sentences = ["Siddhesh will make this count", "Siddhesh will be a Data scientist",
#                  "Always present your sure answer siddhesh",
#                  "Don't relay on anyone siddhesh", "Make things better siddhesh",
#                  "work with consistency to achieve your goal siddhesh"]
#
#     query = input("Please enter the query string\n")
#     match = [Matching_words(query, sentence) for sentence in sentences]
#     # print(match)
#     sortedsentscore = [sentscore for sentscore in sorted(zip(match, sentences), reverse=True)]
#     # print(sortedsentscore)
#
#     print(f"{len(sortedsentscore)} results found")
#     for match, item in sortedsentscore:
#         print(f"\"{item}\": with match of {match}")

# def matchingwords(sentence1, sentence2):
#     found1 = sentence1.split()
#     found2 = sentence2.split()
#     match = 0
#     for word1 in found1:
#         for word2 in found2:
#             print(f"matching {word1} with {word2}")
#             if word1.lower() == word2.lower():
#                 match += 1
#     return match
#
#
# if __name__ == '__main__':
#     print(matchingwords(f"Today is siddhesh gavare birthday as he turn 21 and also a very special day too s he is joinning ",
#           f"a company as as data scientist as his dream job. Today he is very happy"))
