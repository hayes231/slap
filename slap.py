from datetime import date

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

class Char:
    def __init__(self, name, age, race, charclass):
        self.name = name
        self.age = age
        self.race = race
        self.charclass = charclass
        
    def slap(self):
        print("you've been hacked")

    def greet(self):
        print("{}: Hello, my name is {}. I am a {}. I am {} years old".format(self.name, self.name, self.charclass, self.age))

hayes = Char('Hayes', age(date(1998, 6, 8)), 'human', 'warrior')
baron = Char('Baron', 43, 'human', 'blacksmith')

hayes.greet()

newcharname = input('what is your name?: ')
newcharage = input('what is your birthday? (M/D/YYYY): ')
bmonth, bday, byear = newcharage.split("/")
newcharage = age(date(int(byear), int(bmonth), int(bday)))

if int(newcharage) < 18:
    exit("you are not old enough to play this game")
else:
    print(f"you are {newcharage}!")
    
newcharrace = input('what is your race? (human, elf, dwarf): ')
newcharclass = input('what is your class? (mage, warrior, thief): ')

player = Char(newcharname, newcharage, newcharrace, newcharclass)

player.slap()