def count_words (text):
    counter=0
    words = str.split(text)
    for word in words:
        counter +=1
    return (counter)

def count_characters (text):
    count={}
    character_text = list(text.lower())
    for character in character_text:
        #print (count[character])
        if character in count:
            count[character] += 1
        else: 
            count[character] =1
    return count

def sort_on(d):
    return d["num"]

def sort_characters (list1):
    sorted_list = []
    for character in list1:
        sorted_list.append({"char": character, "num": list1[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    

