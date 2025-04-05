def wordcount(text):
    count = 0
    words = text.split()
    for i in words:
        count += 1
    return count

def charactercount(text):
    characters = {}
    for i in text:
        charecter = i.lower()
        if charecter in characters:
            x = characters[charecter]
            x +=1
            characters[charecter] = x
        else:
            characters[charecter] = 1
    return characters

def sorteddic(dic):
    result =[]
    for char,count in dic.items():
        new_dic = {"char": char, "count": count}
        result.append(new_dic)
    result.sort(key=lambda x:x["count"],reverse=True)
    return result

def printstats(path,count,dic):
    newdic=sorteddic(dic)
    #sort the dic
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}.")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for i in newdic:
        char = i["char"]
        count = i["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")