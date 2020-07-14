# Pseudocode: 

#open file 
poem = open('test.txt')

# Write a function:
#     Count how many space separated words occur in file 
#         create word count of each word
#     print the word count 

#Remember: In a for loop, text is broken up by line.

def word_count(poem):

    '''Remove the punctuation/return.'''

    punc = ['.', ',', '?', '\n']

    count_words_dict = {}

    for line in poem:
        phrase = line.split(' ')

        for word in phrase:
            word_list = []
            word_list.append(word)

            word_strs = str(word_list)

            '''Create a dictionary that would count how frequently each word shows up.'''

            for word in word_list:
                count_words_dict[word] = count_words_dict.get(word, 0) + 1

    print(count_words_dict)
    
    #use .item: 
    #list for keys

    # print(new_dict = count_words_dict.items())

    something = sorted(count_words_dict.items(), key=lambda x: x[1], reverse = True)
    print(something)
    
    return count_words_dict





word_count(poem)



