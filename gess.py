import random



guess = []
scrambled = []
words = open('words.txt', mode='rt', encoding='utf-8')
for word in words:
    scrambled.append(word.replace('\n', ''))
    l = list(word)
    y = random.shuffle(l)
    y = ''.join(l)
    guess.append(y.replace('\n', ''))
words.close()
name = input('Hello Sir/Madame, could you kindly tell us your precious name? :)  ')
gender = input("Are you a male or a female? for male type 'Mr' and female 'Mme' :)")
print("Hey! "+gender + " " + name+",\n")
print("Welcome to WordGuessGame!  You wana give it a try? Okay! ")


def main():
    last = int(len(scrambled)) -1
    print(last)
    count = 0
    i = random.randint(0, last)
    mark = 0
    while True:
        user_input = input(" Please guess this word to earn a mark : " + guess[i]+"\n ")
        if user_input == scrambled[i]:
            print("Congratulations "+gender+" "+name+", You guessed well!")
            mark += 1
            print("You have " + str(mark) + " mark(s)."+"You can earn more! Continue!")
        else:
            print("Ohh naps! You are near to the answer!")
            count += 1
            if count == 3:
                print("Hey folks! You have exhausted your 3 trials! Try back later.")
                print(gender+" "+name+" your Total mark(s) is  : " + str(mark)+"/"+str(i))
                stop_quiz()
                return False
        i = i + 1


def stop_quiz():
    print("GuessGame restarting..... \n")
    main()

if __name__ == "__main__":
    main()
