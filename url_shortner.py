# Project: URL Shortner
# Azubi Africa Cohort 1- Getinnotized

import random
import csv
import json

# accept the url


# so the challenge is to make sure that the script doesn't accept the same url
# shorten it
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


ch_list = [chr(i) for i in range(48,127)]  #generate the ascii characters

# to make sure shortened links don't repeat.. 
def rand_gen():
    r_ch = random.choices(ch_list, k=6) 
    random.shuffle(r_ch) 
    return ''.join(r_ch)  

# appending to a csv file

def to_file(link_dict):
    with open('links.csv','a', newline= '') as f:
        write = csv.writer(f)
        write.writerow(link_dict)
    f.close()


# this is the entry point for the program
if __name__ == "__main__":  
    pass

