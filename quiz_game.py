class QuizGame:    
    def take_name_input(self):
        while True:
            user_name = input("Please enter your name: ").strip()
            if user_name.isalpha() and user_name:
                return user_name
            print("Invalid input. Your first name must contain only letters and be at least 1 character long.")
    
    def playing(self, user_name):
        while True:
            play = input(f"{user_name}, do you want to play the quiz game? (yes/no) ").strip().lower()
            if play == "yes":
                print("Great, let's go!")
                break
            elif play == "no":
                print("Okay! Until next time.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def questions(self):
        score = 0
        while True:
            answer = input("What does CPU stand for? ").strip().lower()
            if answer == "central processing unit":
                print("Correct!")
                score += 1
                break
            elif answer == "":
                print("Please enter an answer.")
            else:
                print("Incorrect!")
                break

        print("You got " + str(score) + " quesrtions correct!")
        print("You got " + str((score/1) * 100) + "%.")

def main():
    game = QuizGame()
    user_name = game.take_name_input()
    print("Hello,", user_name)
    game.playing(user_name)
    game.questions()

if __name__ == "__main__":
    main()