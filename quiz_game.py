# this is my first python project a easy one i might say but given tat its the beginning its fine.



print("welcome to my quiz! ")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
     quit()
     
print("Okay lets play :")
score = 0
answer = input("What does the cpu stand for? ")
if answer.lower()== "central processing unit":
     print('correct')
     score += 1

else:
     print("Incorrect")


answer = input("What does the GPU stand for? ")
if answer.lower()== "graphical processing unit":
     print('correct')
     score += 1

else:
     print("Incorrect")

     answer = input("What does the C stand for in my name? ")
if answer.lower()== "charles":
     print('correct')
     score += 1

else:
     print("Incorrect")

answer = input("What does the RAM stand for? ")
if answer.lower()== "random access memory":
     print('correct')
     score += 1

else:
     print("Incorrect")

answer = input("What does the PSU stand for? ")
if answer.lower()== "power supply unit":
     print('correct')
     score += 1

else:
     print("Incorrect")

print("you got" + str(score) +"questions correct!")
print("you got" + str(score /5 *100) + "%.")