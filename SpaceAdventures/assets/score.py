import json

import pygame


class ScoreDisplay:
    """The class for the score display on the left top corner in the game"""
    def __init__(self, window):
        self.window = window
        self.score_sum = 0
        self.font_style = pygame.font.Font("freesansbold.ttf", 40)
        self.text_y = 10
        self.text_x = 10

    def display_score(self):
        """This method draws the score on the screen"""
        self.score = self.font_style.render(f"Score : {self.score_sum}", True, (255, 255, 255))
        self.window.blit(self.score, (self.text_x, self.text_y))

    def read_high_score(self):
        with open("spacepoop_adventures_highscore.json", "r") as f:
            data = json.load(f)
            high_score = int(data["high score"])

        return high_score

    def write_new_high_score(self):
        try:  # Opens the highscore file and checks if it is greater than the new score
            high_score = self.read_high_score()

            # If the new score is greater than the old high score it will change and be rewritten
            if self.score_sum > high_score:
                high_score = {"high score": str(self.score_sum)}

                with open("spacepoop_adventures_highscore.json", "w") as file:
                    json.dump(high_score, file, ensure_ascii=False)

        # If FileNotFoundError will this make a new highs core JSON file, where the top score it placed
        except FileNotFoundError:
            high_score = {"high score": str(self.score_sum)}

            with open("spacepoop_adventures_highscore.json", "w") as file:
                json.dump(high_score, file, ensure_ascii=False)




