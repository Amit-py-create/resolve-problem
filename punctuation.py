import string

def remove_punctuation(input_string):
    
    translator = str.maketrans('', '', string.punctuation)

    return input_string.translate(translator)


input_str = "Hello, world! How's it going?"
cleaned_str = remove_punctuation(input_str)
print(cleaned_str)  
