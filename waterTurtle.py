import random

class WaterTurtle():
    """
    Class for the new Water Turtle Progmon
    """
    def __init__(self):
        """
        Creates variables associated with WaterTurtle
        Args:
            self (object) - WaterTurtle
        Returns:
            None
        """
        self.name = "Water Turtle"
        self.hp = 200
        self.currentHealth = 200
        self.alive = True
        self.bag = ["healthPotion", "statBoost", "defenseBoost"]
        self.attackList = ["Aqua Jet", "Aqua Tail", "Water Pulse", "Bubble"]
        self.stunned = False
        self.statBoost = False
        self.defenseBoost = False

    def doDamage(self, damageDone):
        """
        Deals damage to the enemy's health; set alive to False if health goes below 1
        Args:
            self (object) - WaterTurtle
            damageDone (int) - amount of damage to do
        Returns:
            None
        """
        if(self.defenseBoost == True):
            self.currentHealth = self.currentHealth - damageDone + 10
            self.defenseBoost = False
        else:
            self.currentHealth = self.currentHealth - damageDone

        if(self.currentHealth <= 0):
            self.alive = False

    def checkAlive(self):
        """
        Checks if WaterTurtle is alive
        Args:
            self (object) - WaterTurtle
        Returns:
            (bool) - True if WaterTurtle is alive, otherwise False
        """
        if(self.alive == True):
            return True
        else:
            return False

    def getAttackList(self):
        """
        Gets the attack list of Progmon
        Args:
            self (object)
        Returns:
            Progmon's attackList
        """
        return self.attackList

    def setBag(self, newBag):
        """
        Sets the bag of Progmon
        Args:
            self (object)
            newBag (array) - what to set bag to
        Returns:
            None
        """
        self.bag = newBag

    def getBag(self):
        """
        Gets the bag list of Progmon
        Args:
            self (object)
        Returns:
            Progmon's bag
        """
        return self.bag

    def getCurrentHealth(self):
        """
        Gets the currentHealth of WaterTurtle
        Args:
            self (object) - WaterTurtle
        Returns:
            WaterTurtle's currentHealth
        """
        return self.currentHealth

    def setCurrentHealth(self, newHealth):
        """
        Sets the current health of Progmon
        Args:
            self (object)
            newHealth (int) - what to set current health to
        Returns:
            None
        """
        self.currentHealth = newHealth

    def getHp(self):
        """
        Gets the max health of WaterTurtle
        Args:
            self (object) - WaterTurtle
        Returns:
            WaterTurtle's max health
        """
        return self.hp

    def setStunStatus(self, setter):
        """
        Sets the stun status of Progmon
        Args:
            self (object)
            setter (boolean) - what to set stunned to
        Returns:
            None
        """
        self.stunned = setter

    def getStunStatus(self):
        """
        Gets the stun status of Progmon
        Args:
            self (object)
        Returns:
            Progmon's stunned
        """
        return self.stunned

    def setDefenseBoost(self, setter):
        """
        Sets the defense boost of Progmon
        Args:
            self (object)
            setter (boolean) - what to set defense boost to
        Returns:
            None
        """
        self.defenseBoost = setter

    def getDefenseBoost(self):
        """
        Gets the defense boost of Progmon
        Args:
            self (object)
        Returns:
            Progmon's defense boost
        """
        return self.defenseBoost

    def setStatBoost(self, setter):
        """
        Sets the stat boost of Progmon
        Args:
            self (object)
            setter (boolean) - what to set stat boost to
        Returns:
            None
        """
        self.statBoost = setter

    def getStatBoost(self):
        """
        Gets the defense boost of Progmon
        Args:
            self (object)
        Returns:
            Progmon's defense boost
        """
        return self.statBoost

    def attack1(self, enemyPlayer):
        chanceToHit = random.randint(1, 101)
        if(self.statBoost == True and chanceToHit <= 70):
            self.statBoost = False
            enemyPlayer.doDamage(55)
            enemyPlayer.setStunStatus(True)
            return True, "Aqua Jet did 55 damage and stunned the enemy!"
        if(chanceToHit <= 70):
            enemyPlayer.doDamage(45)
            return True, "Aqua Jet did 45 damage!"
        else:
            return False, "Aqua Jet missed!"

    def attack2(self, enemyPlayer):
        chanceToHit = random.randint(1, 101)
        if(chanceToHit <= 55):
            enemyPlayer.doDamage(50)
            return True, "Aqua Tail did 50 damage!"
        else:
            return False, "Aqua Tail missed!"

    def attack3(self, enemyPlayer):
        chanceToHit = random.randint(1, 101)
        if(self.statBoost == True and chanceToHit <= 48):
            self.statBoost = False
            enemyPlayer.doDamage(80)
            enemyPlayer.setStunStatus(True)
            return True, "Water Pulse did 80 damage and stunned the enemy!"
        if(chanceToHit <= 48):
            enemyPlayer.doDamage(70)
            return True, "Water Pulse did 70 damage!"
        else:
            return False, "Water Pulse missed!"

    def attack4(self, enemyPlayer):
        enemyPlayer.doDamage(12)
        return True, "Bubble did 12 damage!"

    def AIAttack(self, enemyPlayer):
        """
        Attacks enemy Progmon with a randomly chosen attack
        Args:
            self (object) - WaterTurtle
            enemyPlayer (object) - enemy Progmon
        Returns:
            (string) - the attack that was used by the AI
        """
        attackToUse = random.randint(1, 5)
        tempHealth = enemyPlayer.getCurrentHealth()
        if(attackToUse == 1):
            self.attack1(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Aqua Jet hit for 45 damage!"
            else:
                return "AI Aqua Jet missed!"
        if(attackToUse == 2):
            self.attack2(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Aqua Tail hit!"
            else:
                return "AI Aqua Tail missed!"
        if(attackToUse == 3):
            self.attack3(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Water Pulse hit!"
            else:
                return "AI Water Pulse missed!"
        if(attackToUse == 4):
            self.attack4(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Bubble hit!"
            else:
                return "AI Bubble missed!"

    def useHealthPotion(self):
        """
        Uses a healthPotion to heal 30 points of health
        Args:
            self (object) - WaterTurtle
        Returns:
            None
        """
        if(self.currentHealth+30 > self.hp):
            hpToAdd = self.hp - self.currentHealth
            self.currentHealth + hpToAdd
            print("Health Potion healed you for:", hpToAdd, "\n")
            self.bag.remove("healthPotion")

        else:
            self.currentHealth + 30
            print("Health Potion healed you for: 30\n")
            self.bag.remove("healthPotion")

    def useStatBoost(self):
        """
        Allows this Progmon to use a statBoost Potion
        Args:
            self (object) - WaterTurtle
        Returns:
            None
        """
        self.statBoost = True
        print("Stat Boost for Water Turtle is activated!\n You will do +10 damage and have a chance to stun!\n")
        self.bag.remove("statBoost")

    def useDefenseBoost(self):
        """
        Allows this progmon to use a defense Potion
        Args:
            self (object) - WaterTurtle
        Returns:
            None
        """
        self.defenseBoost = True
        print("Defense boost for Water Turtle is now activated!\n You will take 10 less damage on the next attack.\n")
        self.bag.remove("defenseBoost")

    def bagEmpty(self):
        """
        Checks if the Bag is empty
        Args:
            self (object) - WaterTurtle
        Returns:
            (bool) - True if Bag is empty, otherwise False
        """
        if(self.bag):
            return False
        else:
            return True
