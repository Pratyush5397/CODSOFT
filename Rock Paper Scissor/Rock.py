import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock-Paper-Scissors Game")
        master.geometry("400x400")
        master.resizable(False, False)

        # Initialize scores.
        self.user_score = 0
        self.computer_score = 0

        # Title Label.
        self.title_label = tk.Label(master, text="Rock-Paper-Scissors Game", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Instruction Label.
        self.instruction_label = tk.Label(master, text="Choose rock, paper, or scissors:", font=("Helvetica", 12))
        self.instruction_label.pack(pady=5)

        # Frame to hold the buttons.
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)

        # Rock button.
        self.rock_button = tk.Button(
            self.button_frame, text="Rock", width=10, font=("Helvetica", 12),
            command=lambda: self.play_round("rock")
        )
        self.rock_button.grid(row=0, column=0, padx=5)

        # Paper button.
        self.paper_button = tk.Button(
            self.button_frame, text="Paper", width=10, font=("Helvetica", 12),
            command=lambda: self.play_round("paper")
        )
        self.paper_button.grid(row=0, column=1, padx=5)

        # Scissors button.
        self.scissors_button = tk.Button(
            self.button_frame, text="Scissors", width=10, font=("Helvetica", 12),
            command=lambda: self.play_round("scissors")
        )
        self.scissors_button.grid(row=0, column=2, padx=5)

        # Label to display the result of each round.
        self.result_label = tk.Label(master, text="Let's play!", font=("Helvetica", 12), justify="center")
        self.result_label.pack(pady=15)

        # Label to display the current scores.
        self.score_label = tk.Label(
            master, 
            text=f"Your Score: {self.user_score}    Computer Score: {self.computer_score}",
            font=("Helvetica", 12)
        )
        self.score_label.pack(pady=5)

        # Reset Game button.
        self.reset_button = tk.Button(master, text="Reset Game", font=("Helvetica", 12), command=self.reset_game)
        self.reset_button.pack(pady=15)

    def play_round(self, user_choice):
        """Handles the logic for one round of the game."""
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Determine the outcome.
        if user_choice == computer_choice:
            outcome = "It's a tie!"
        elif ((user_choice == "rock" and computer_choice == "scissors") or
              (user_choice == "paper" and computer_choice == "rock") or
              (user_choice == "scissors" and computer_choice == "paper")):
            outcome = "You win!"
            self.user_score += 1
        else:
            outcome = "You lose!"
            self.computer_score += 1

        # Update the result display.
        self.result_label.config(
            text=f"You chose: {user_choice.capitalize()}\n"
                 f"Computer chose: {computer_choice.capitalize()}\n"
                 f"Result: {outcome}"
        )

        # Update the score display.
        self.score_label.config(
            text=f"Your Score: {self.user_score}    Computer Score: {self.computer_score}"
        )

    def reset_game(self):
        """Resets the scores and display messages."""
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="Let's play!")
        self.score_label.config(text=f"Your Score: {self.user_score}    Computer Score: {self.computer_score}")

def main():
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
