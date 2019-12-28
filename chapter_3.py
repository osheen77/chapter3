# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 11:22:56 2019

@author: Osheen 
# new change
"""

#**************CHA[TER 3*************
# Exercise 3.1-3.3

friends = ['neha', 'mega', 'monica', 'mona', 'lola']
print(friends[0].title())
print(friends[1].title())
print(friends[2].title())
print(friends[3].title())
print(friends[4].title())

message_1= friends[0].title() + " is very helpful" + "."
print(message_1)

message_2= friends[1].title() + " is very beautiful" + "."
print(message_2)

message_3= friends[2].title() + " is very intelligent" + "."
print(message_3)

message_4= friends[3].title() + " is athletic" + "."
print(message_4)

message_5= friends[4].title() + " is very joyous" + "."
print(message_5)


#exercise 3.4-3.7
guests =['mom', 'dad', 'bro','cousin']
message_6 = guests[0].title() + " is going  to cook for the dinner" + "."
print(message_6)

message_7 = guests[1].title() + " will be sitting on the head's seat" + "."
print(message_7)

message_8 = guests[2].title() + " will be giving the speach for th enight" + "."
print(message_8)

message_9 = guests[3].title() + " is coming from New York" + "."
print(message_9)

guests =['mom', 'dad', 'bro','cousin']
not_coming= guests.pop(3)
print( not_coming)
print(guests)
print("My " + not_coming + " is not coming for the dinner anymore")
                    
guests.insert(3,'friend')
print(guests)
print("instead of my cousin, my  " + guests[3]+ " is coming")

message_10 = guests[0].title() + " is going  to cook for the dinner" + "."
print(message_10)

message_11 = guests[1].title() + " will be sitting on the head's seat" + "."
print(message_11)

message_12 = guests[2].title() + " will be giving the speach for th enight" + "."
print(message_12)

message_13 = guests[3].title() + " is my life savour" + "."
print(message_13)


print("I found a bigger table at a better restraunt")
guests.insert(0, 'Billy')
guests.insert(3,'Brandy')
guests.append('Brian')
print(guests)


message_14 = guests[0].title() + " is my best friend since childhood " + "."
print(message_14)

message_15 = guests[1].title() + " Thanks fo r making last minute changes" + "."
print(message_15)

message_16 = guests[2].title() + " I can't wait to see you" + "."
print(message_16)

message_17 = guests[3].title() + " is my childhood sweatheart" + "."
print(message_17)

message_18 = guests[4].title() + " Thanks for making th enew reservatons" + "."
print(message_18)

message_19 = guests[5].title() + " Always helpp me" + "."
print(message_19)

message_20 = guests[6].title() + " Don't be late like always" + "."
print(message_20)


guests=['Billy', 'mom', 'dad', 'Brandy', 'bro', 'friend', 'Brian']
print(guests)
print("Only two peopele for the dinner invited")
not_invited=guests.pop(0)
print("sorry to inform " + not_invited+ " ,you are not invited.")
not_invited=guests.pop(3)
print("sorry to inform " + not_invited+ " ,you are not invited.")
not_invited=guests.pop(4)
print("sorry to inform " + not_invited+ " ,you are not invited.")
removal='Brandy'
guests.remove(removal)
print("sorry to inform " + removal+ " ,you are not invited.")
removal_1='friend'
guests.remove(removal_1)
print("sorry to inform " + removal_1+ " ,you are not invited.")

len(guests)







