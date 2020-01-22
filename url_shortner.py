# Project: URL Shortner
# Azubi Africa Cohort 1- Getinnotized
# Date: Friday 17th January, 2020.
# Written by: Vanessa Quartey and Clifford E. Akai-Nettey

import random
import csv

# accept the url and url validation 
#checking for https:// , and special keys
url = input("Enter your url: ")
if("https://" in url and".com" in url and "www." in url ):
  print(url)
else:
  print("kindly enter a secured url") 

# shorten it
def shorten(url):
    short_url = 'https://' + 'short.lnk/'+ rand_gen() 
    return [ url, short_url]

ch_list = [ chr(i) for i in range(33,127)]  #generate the ascii characters

# to make sure shortened links don't repeat.. 
def rand_gen():
    r_ch = random.choices(ch_list, k=6) 
    random.shuffle(r_ch) 
    return ''.join(r_ch)  

# appending to a csv file

link_pair = shorten(url)

with open('links.csv', mode='a') as data:
    write = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    write.writerow(link_pair)
data.close()