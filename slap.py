class Char:
    def __init__(self, name, age, race, charclass):
        self.name = name
        self.age = age
        self.race = race
        self.charclass = charclass
        
    def slap(self):
        print("youve been slapped")

    def greet(self):
        print("{}: Hello, my name is {}. I am a {}".format(self.name, self.name, self.charclass))

Hayes = Char('Hayes', 18, 'human', 'warrior')
Baron = Char('Baron', 43, 'human', 'blacksmith')

Hayes.greet()

newcharname = input('what is your name?: ')
newcharage = input('how old are you?: ')
if int(newcharage) < 18:
    exit("you are not old enough to play this game")
newcharrace = input('what is your race? (human, elf, dwarf): ')
newcharclass = input('what is your class? (mage, warrior, thief): ')

player = Char(newcharname, newcharage, newcharrace, newcharclass)

player.slap()
