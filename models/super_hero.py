

class SuperHero:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def serialize(self):
        return {
            "name": self.name,
            "skill": self.skill
        }
