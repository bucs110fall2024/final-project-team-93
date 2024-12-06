import json

class Highscore:
    def __init__(self):
        self.file = "assets/highscore.json"
        self.current_highscore = self.load_highscore()

    def load_highscore(self):
        with open(self.file, "r") as file:
            highscore = json.load(file)
            return highscore.get("highscore")

    def update_highscore(self, score):
        if score > self.current_highscore:
            self.current_highscore = score
            with open(self.file, "w") as file:
                json.dump({"highscore": self.current_highscore}, file)
