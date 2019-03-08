f = open('gibberish.txt', 'r')
text = f.read()
words = text.split(' ')
freqs = {}
for word in words:
    if word in freqs.keys():
        freqs[word] += 1
    else:
        freqs[word] = 1

popular_word = ''
max_freq = 0
top_words = []
for key in freqs.keys():
    if freqs[key] > max_freq:
        popular_word = key
        max_freq = freqs[key]

print(popular_word)
