def get_num_words(text):
    words = text.split()
    return len(words)
def count_character(text):
   
    data = text.lower()
    
    position = ''
    database = {}
    
    for char in data:
        if not char in database:
            database[char]= 1
        else:
            database[char] +=1
        
    return database

def book_bot(text):
    database = count_character(text)
    sorted_database = dict(sorted(database.items(),reverse =True,key =lambda item:item[1] ))
    count= get_num_words(text)

    return sorted_database,count
    
