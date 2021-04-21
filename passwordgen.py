import secrets

#a "simple" program to generate random passwords a la that one xkcd.
#takes a text file of the 10 thousand most used words and grabs 4 random ones.
#it might be too much for python, might need to use a compiled language.
#there is also the easy way out, as on pip there are a few modules that just grab random words
#also using vim to code this just to get more used to it again.

#create list of words from word document

#words = open("wiki-100k.txt", 'r')
#switch commenting between these two to change whether its the most common 100 thousand words or the
#most common 1000
words = open("1-1000.txt", 'r')
wordlist = words.readlines()
words.close()

repetitions = 4 #change this to change the amount of words glued together
password = ''
for i in range(0,repetitions):
   password += secrets.choice(wordlist).replace('\n', '')
print (password)
