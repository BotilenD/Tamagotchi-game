
# Making peolot to do with pets


class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
        self.fitness = 50

    def eat(self):
        if self.hunger < 100:
            self.hunger -= 20
            self.happiness += 5
            print(f"{self.name} ate food. Hunger is now {self.hunger}. Happiness increased to {self.happiness}.")
        else:
            print(f"{self.name} is not hungry.")

    def sleep(self):
        if self.energy < 100:
            self.energy += 30
            self.hunger += 10
            print(f"{self.name} slept well. Energy is now {self.energy}. Hunger increased to {self.hunger}.")
        else:
            print(f"{self.name} is not tired.")

    def exercise(self):
        if self.energy > 20:
            self.fitness += 20
            self.energy -= 15
            self.happiness += 10
            print(f"{self.name} exercised. Fitness is now {self.fitness}, Energy decreased to {self.energy}, Happiness increased to {self.happiness}.")
        else:
            print(f"{self.name} is too tired to exercise.")

    def play(self):
        if self.happiness < 100:
            self.happiness += 20
            self.energy -= 10
            print(f"{self.name} played. Happiness is now {self.happiness}, Energy decreased to {self.energy}.")
        else:
            print(f"{self.name} is already very happy.")

# Playing with the pets

def interact_with_tamagotchi():
    tamagotchi = Tamagotchi(name="Tama")

    while True:
        print("\nWhat would you like to do with your Tamagotchi?")
        print("1. Eat")
        print("2. Sleep")
        print("3. Exercise")
        print("4. Play")
        print("5. Exit")

        choice = input("Enter the number of the action you want to take: ")

        if choice == "1":
            tamagotchi.eat()
        elif choice == "2":
            tamagotchi.sleep()
        elif choice == "3":
            tamagotchi.exercise()
        elif choice == "4":
            tamagotchi.play()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")


interact_with_tamagotchi()
