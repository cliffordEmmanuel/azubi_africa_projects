# Project: URL Shortner
# Azubi Africa Cohort 1- Getinnotized

import random
import csv

# accept the url and url validation 
#checking for https:// , and special keys
def url_validator():
    pass


def shorten(url):
    short_url = 'https://' + 'short.lnk/'+ rand_gen() 
    return (url ,short_url )
    

def url_exists(url):
    # open the file and check if the long url has already been processed
    with open('links.csv', mode='r') as l_file:
        reader = csv.reader(l_file)
        for row in reader:
            if row[0] == url:
                return True

l = [58,59,60,61,62,63,64,91,92,93,94,95,96]  # removing the special characters
ch_list = [chr(i) for i in range(48,122) if i not in l]  #generate the ascii characters

# to make sure shortened links don't repeat.. 
def rand_gen():
    r_ch = random.choices(ch_list, k=6) 
    random.shuffle(r_ch) 
    return ''.join(r_ch)  

# appending to a csv file

def to_file(link):
    with open('links.csv','a', newline= '') as f:
        write = csv.writer(f)
        write.writerow(link)
    f.close()


def search_by_long_url():
    pass

def search_by_short_url():
    pass
        
# this is the entry point for the program
if __name__ == "__main__":
    url = input("Enter the url: ")
    if not url_exists(url):
        link_dict = shorten(url)
        to_file(link_dict)
        print('URL saved')
    else:
        print('URL already saved. Enter a new one')


# search by long url
# search by short url
# allows should see a shortened url.