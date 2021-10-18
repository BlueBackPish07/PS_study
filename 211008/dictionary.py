

def sol(word): #
    str_list = ['A','E','I','O','U']
    book = set(str_list)
    temp =[]
    for i in range(4):
        for dict_word in book:
            for alpa in str_list:
                temp.append(dict_word+ alpa)
            
        book.update(temp)
        temp = []
    return sorted(list(book)).index(word) +1

print(sol('I'))
 
 
