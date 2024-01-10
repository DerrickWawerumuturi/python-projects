
print("welcome to my game")
 
playing= input("do you want to play? ")
if playing  != "yes":
    quit()
print("Okay, let's play")

score=0
answer= input("What is the top speed of the Bugatti Chiron, one of the fastest sports cars in the world? ")
if answer.lower()== "261 mph":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT")
answer= input("Which automaker produces the iconic sports car model known as the Porsche 911? ")
if answer.lower()== "porsche":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT")
answer= input("What is the engine displacement (in liters) of the Chevrolet Corvette C8, the first mid-engine Corvette? ")
if answer.lower()== "6.2 liters":
        print("CORRECT!")
        score+=1
else:
    print("INCORRECT")
answer= input("In Formula 1 racing, which team has won the most Constructors' Championships to date? ")
if answer.lower()== "scuderia ferrari":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT")

answer= input("What technology is commonly used in modern sports cars to enhance traction and handling, allowing power to be sent to individual wheels as needed? ")
if answer.lower()== "all-wheel drive or four-wheel drive":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT")

answer= input("Which sports car holds the lap record at the Nürburgring Nordschleife, a legendary racetrack in Germany? ")
if answer.lower()== "lamborghini aventador svj":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT")

answer= input("What is the iconic sports car model produced by Ford that gained popularity through its appearance in the movie Gone in 60 Seconds? ")
if answer.lower()== "ford mustang shelby gt500":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT")

answer= input("Which sports car brand is associated with the legendary racing driver Ayrton Senna? ")
if answer.lower()== "mclaren":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT")

answer= input("What is the term used to describe the roof design of a sports car that can be fully or partially retracted, allowing for open-top driving? ")
if answer.lower()== "convertible or roadster roof":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT")

print("You got" + str(score)+  "questions correct")
print("You got " + str(round(score/9 * 100,2))+ " %")

if score == 9 :
      ("Good job")







