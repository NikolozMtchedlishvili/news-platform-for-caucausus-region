import tool as tool

def Split():
    with open("data.txt", "r") as file:
        to_clear = open('splited_data.txt', 'w')
        to_clear.close()
        lines = file.readlines()
        for line in lines:
            line = line.split('\n', 1)[0]
            line = line.split()
            splited = line[:6]
            if splited[-1] in ('of','or','and','at','as','in','the','The','In','As','At','And','Or','For','for','Of','To','to','with','With','over','Over'):
                splited_second = line[:7]
                splited_second = ' '.join([str(elem) for elem in splited_second])
                with open("splited_data.txt", 'a+') as to_write:
                    to_write.write(f'{splited_second}\n')
            else:
                splited = ' '.join([str(elem) for elem in splited])
                with open("splited_data.txt", 'a+') as to_write:
                    to_write.write(f'{splited}\n')
          
        
def Generate():
    with open("splited_data.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.split('\n', 1)[0]
            query = line
            tool.main(query)


    

# done: find paid APi, responsive images
# do: connect and automate, find Free API (googles search engine to extract img with search results