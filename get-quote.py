#edited by iambashar
import random

def primary():
 print("Keep it logically awesome.")

 f = open("quotes.txt")
 quotes = f.readlines()
 f.close()
 
 last = len(quotes) - 2
 rnd = random.randint(0, last)
 print(quotes[rnd].strip())
 print(quotes[rnd+1].strip())

 f = open("quotes.txt", "a")
 i = input("Enter 'E' to add quotes:")
 if i == 'E':
   h = input("Enter quotes to insert in your fav list : ")
   h += "\n"
   f.write(h)
 f.close()

if __name__== "__main__":
 	primary()
