def duplicate_encode(word):
    new_word = ""
    word = word.lower()
    for w in word:
    	if word.count(w) > 1:
    		new_word += ')'
    	else:
    		new_word += '('

    return new_word