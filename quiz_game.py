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
            if play in {"yes", "no"}:
                print("Great, let's go!" if play == "yes" else "Okay! Until next time.")
                return play == "yes"
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def questions(self, user_name):
        score = 0
        questions_and_answers = [
            ("What does CPU stand for?", "central processing unit"),
            ("What does GPU stand for?", "graphics processing unit"),
            ("What does HTML stand for?", "hypertext markup language"),
            ("What does CSS stand for?", "cascading style sheet")
        ]

        for question, answer in questions_and_answers:
            while True:
                user_answer = input(question + " ").strip().lower()
                if user_answer == answer:
                    print("Correct!")
                    score += 1
                    break
                elif user_answer == "":
                    print("Please enter an answer.")
                else:
                    print("Incorrect!")
                    break

        print(f"Well done {user_name}. You got {score} questions correct!")
        print(f"This means you got {int(score/len(questions_and_answers) * 100)}% overall.")

def main():
    game = QuizGame()
    user_name = game.take_name_input()
    print("Hello,", user_name)
    game.playing(user_name)
    game.questions(user_name)

if __name__ == "__main__":
    main()