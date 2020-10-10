import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))
sentence = "Backgammon is one of the oldest known board games."
words = nltk.word_tokenize(sentence)
word_without_stopwords = []
for word in words:
    if word not in stop_words:
        word_without_stopwords.append(word)

print(word_without_stopwords)
        # print(word)
# word_without_stopwords = [word for word in words if not word in stopwords]
# print(word_without_stopwords)

# text = "Backgammon is one of the oldest known board games. Its history can be traced back nearly 5,000 years to archeological discoveries in the Middle East. It is a two player game where each player has fifteen checkers which move between twenty-four points according to the roll of two dice."
# sentences = nltk.sent_tokenize(text)
# for sentence in sentences:
#     print(sentence)
#     print()