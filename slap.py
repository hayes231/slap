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

    def greet(self):
        print(f"{self.name}: Hello, my name is {self.name}. I am a {self.charclass}. I am {self.age} years old")

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

agreement = input(f"So you're a {player.age} year old {player.race} {player.charclass} named {player.name}?")