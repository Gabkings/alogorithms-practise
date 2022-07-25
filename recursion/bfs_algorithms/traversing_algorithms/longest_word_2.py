
# LongestWord(sen) take the sen parameter being passed and return the longest word in the string. 
# If there are two or more words that are the same length, 
# return the first word from the string with that length. 
# Ignore punctuation and assume sen will not be empty. 
# Words may also contain numbers, for example "Hello world123 567"

def LongestWord(sen):
    import re 

    length_greatest = 0

    sen = sen.lower()

    sen = re.sub('[^abcdefghijklmnopqrstuvwxyz1234567890]',' ', sen)

    sen_split = sen.split()

    for word in sen_split:

        length = len(word)

        if length > length_greatest:

            length_greatest, longest_word = length, word
        
    return longest_word

print(LongestWord(raw_input()))