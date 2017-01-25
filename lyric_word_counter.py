# -*- coding: utf-8 -*-
def lyrics_to_frequency(lyrics):
    """
    Assumes that lyrics is a string.
    Creates a dictionary of each word in the lyrics and its frequency
    """
    lyrics = lyrics.lower()
    copy = lyrics
    for l in copy:
        if l == '\'':
            lyrics = lyrics.replace(l,' ')
    for l in copy:
        if l.isalpha() == False and l != ' ':
            lyrics = lyrics.replace(l,'')
    wordlist = lyrics.split()
    ###
    dictionary = {}
    for w in wordlist:
        dictionary[w] = wordlist.count(w)
    return dictionary  
    
################################   
    
def most_used_words(lyrics):
    """
    takes lyrics and prints out the most used word(s),
    and how many times they are used
    """
    dictionary = lyrics_to_frequency(lyrics)
    maxNum = max(dictionary.values())
    result = []
    for a in dictionary:
        if dictionary[a] == maxNum:
            result.append(a)
    print (result, maxNum)
################################     

def occurAtLeastxTimes(lyrics, x):
    """
    takes lyrics and returns all words that occur at least x times
    """    
    dictionary = lyrics_to_frequency(lyrics)
    result = []
    for b in dictionary:
        if dictionary[b] >= x:
            result.append(b)
    print (result)   
################################ 
  
song = open("C:/Users/malbrecht/Documents/MITPythonCourse/WeAreTheChampions.txt", "r")
#song = open("WeAreTheChampions.txt", "r")
lyrics =  song.read()
#lyrics = "I've paid my dues Time after time I've done my sentence But committed no crime And bad mistakes I've made a few I've had my share of sand kicked in my face But I've come through We are the champions, my friends And we'll keep on fighting 'til the end We are the champions We are the champions No time for losers 'Cause we are the champions of the world I've taken my bows And my curtain calls You brought me fame and fortune and everything that goes with it I thank you all But it's been no bed of roses No pleasure cruise I consider it a challenge before the whole human race And I ain't gonna lose We are the champions, my friends And we'll keep on fighting 'til the end We are the champions We are the champions No time for losers 'Cause we are the champions of the world We are the champions, my friends And we'll keep on fighting 'til the end We are the champions We are the champions No time for losers 'Cause we are the champions"
song.close()
occurAtLeastxTimes(lyrics, 7)
#print(lyrics_to_frequency(lyrics))