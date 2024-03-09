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

def main():
    game = QuizGame()
    user_name = game.take_name_input()
    print("Hello,", user_name)
    game.playing(user_name)


if __name__ == "__main__":
    main()