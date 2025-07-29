# Base Character class
import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        # Random damage within ±20% of base attack power
        min_damage = int(self.attack_power * 0.8)
        max_damage = int(self.attack_power * 1.2)
        damage = random.randint(min_damage, max_damage)
        
        # Check for special defenses
        if hasattr(opponent, 'evade_next') and opponent.evade_next:
            print(f"{opponent.name} evades {self.name}'s attack!")
            opponent.evade_next = False
            return
        
        if hasattr(opponent, 'shield_next') and opponent.shield_next:
            print(f"{opponent.name}'s Divine Shield blocks {self.name}'s attack!")
            opponent.shield_next = False
            return
        
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = 30
        old_health = self.health
        self.health = min(self.health + heal_amount, self.max_health)
        actual_heal = self.health - old_health
        print(f"{self.name} heals for {actual_heal} health! Current health: {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def berserker_rage(self, opponent):
        damage = self.attack_power + 20  # Bonus damage
        opponent.health -= damage
        print(f"{self.name} goes into Berserker Rage and attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def shield_bash(self, opponent):
        damage = self.attack_power // 2
        opponent.health -= damage
        print(f"{self.name} uses Shield Bash on {opponent.name} for {damage} damage and stuns them!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def fireball(self, opponent):
        damage = self.attack_power + 25  # High damage spell
        opponent.health -= damage
        print(f"{self.name} casts Fireball on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def mana_shield(self):
        heal_amount = 20
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} uses Mana Shield and recovers {heal_amount} health! Current health: {self.health}")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        heal_amount = 5
        old_health = self.health
        self.health = min(self.health + heal_amount, self.max_health)
        actual_heal = self.health - old_health
        if actual_heal > 0:
            print(f"{self.name} regenerates {actual_heal} health! Current health: {self.health}")
        else:
            print(f"{self.name} is already at full health!")

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
        self.evade_next = False  # Track if next attack should be evaded

    def quick_shot(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Quick Shot on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def evade(self):
        self.evade_next = True
        print(f"{self.name} prepares to evade the next attack!")

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)
        self.shield_next = False  # Track if next attack should be blocked

    def holy_strike(self, opponent):
        damage = self.attack_power + 15  # Bonus damage
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def divine_shield(self):
        self.shield_next = True
        print(f"{self.name} casts Divine Shield! Next attack will be blocked!")


def create_character():
    print("Choose your character class:")
    print("1. Warrior - High health, balanced attack (Berserker Rage, Shield Bash)")
    print("2. Mage - Low health, high magic damage (Fireball, Mana Shield)")
    print("3. Archer - Balanced stats, ranged attacks (Quick Shot, Evade)") 
    print("4. Paladin - Highest health, defensive abilities (Holy Strike, Divine Shield)")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    print(f"\n🗡️  BATTLE BEGINS! 🗡️")
    print(f"{player.name} vs {wizard.name}")
    print("=" * 40)
    
    while wizard.health > 0 and player.health > 0:
        print(f"\n--- {player.name}'s Turn ---")
        print(f"Your Health: {player.health}/{player.max_health}")
        print(f"Wizard Health: {wizard.health}")
        print("\nChoose your action:")
        print("1. Attack")
        print("2. Use Special Ability 1")
        print("3. Use Special Ability 2")
        print("4. Heal")
        print("5. View Stats")

        choice = input("Choose an action (1-5): ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            # First special ability for each class
            if isinstance(player, Warrior):
                player.berserker_rage(wizard)
            elif isinstance(player, Mage):
                player.fireball(wizard)
            elif isinstance(player, Archer):
                player.quick_shot(wizard)
            elif isinstance(player, Paladin):
                player.holy_strike(wizard)
        elif choice == '3':
            # Second special ability for each class
            if isinstance(player, Warrior):
                player.shield_bash(wizard)
            elif isinstance(player, Mage):
                player.mana_shield()
            elif isinstance(player, Archer):
                player.evade()
            elif isinstance(player, Paladin):
                player.divine_shield()
        elif choice == '4':
            player.heal()
        elif choice == '5':
            player.display_stats()
            wizard.display_stats()
            continue  # Don't end turn, let player choose again
        else:
            print("Invalid choice. Try again.")
            continue  # Don't end turn, let player choose again

        # Check if wizard is defeated
        if wizard.health <= 0:
            break

        # Wizard's turn
        print(f"\n--- {wizard.name}'s Turn ---")
        wizard.regenerate()
        wizard.attack(player)

        # Check if player is defeated
        if player.health <= 0:
            print(f"\n💀 DEFEAT! {player.name} has been defeated by {wizard.name}! 💀")
            print("The darkness spreads across the land...")
            return

    # If we get here, the wizard was defeated
    print(f"\n🎉 VICTORY! {player.name} has defeated {wizard.name}! 🎉")
    print("The realm is safe once again!")
    print(f"Final Stats - {player.name}: {player.health}/{player.max_health} HP remaining")

def main():
    print("=" * 50)
    print("🏰 WELCOME TO THE REALM OF HEROES! 🏰")
    print("=" * 50)
    print("A dark wizard threatens the land...")
    print("Choose your hero and save the realm!")
    print()
    
    player = create_character()
    print(f"\n✨ {player.name} the {player.__class__.__name__} has been created! ✨")
    player.display_stats()
    
    wizard = EvilWizard("Malachar the Dark")
    print(f"\n⚡ Your enemy: {wizard.name} appears! ⚡")
    wizard.display_stats()
    
    battle(player, wizard)

if __name__ == "__main__":
    main()
