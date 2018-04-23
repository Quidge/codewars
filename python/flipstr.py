def spin_words(sentence):
    flipped_list = []
    str_list = sentence.split(" ")
    for word in str_list:
        if len(word) < 5:
            flipped_list.append(word)
        else:
            flipped_word = ""
            for i in range(len(word), 0, -1):
                flipped_word = flipped_word + word[i-1]
            flipped_list.append(flipped_word)
    return " ".join(flipped_list)


def spin_words2(sentence):
    str_list = sentence.split(" ")

    def flip_word(word):
        flipped = "".join([word[i - 1] for i in range(len(word), 0, -1)])
        return flipped

    flip_list = " ".join([flip_word(wrd) if len(wrd) > 4 else wrd for wrd in str_list])
    return flip_list


string = "Hello mary poppins"

print(string)
print(spin_words2(string))





