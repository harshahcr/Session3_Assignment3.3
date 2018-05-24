def longest_word_insent(wordtext):
    compare_word = ''
    for word in wordtext:
        if len(word) > len(compare_word):
            compare_word=word
    print(compare_word)

sent = input('Please update the sentence : ')
wordtext=sent.split()
longest_word_insent(wordtext)
