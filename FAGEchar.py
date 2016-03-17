#!/usr/bin/python
import random 
import sys



def charattr():
        range = [-2,-1,-1,0,0,0,1,1,1,2,2,2,3,3,3,4] 
        roller = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
        element = roller - 3
        rollreturn = range[element]
        return rollreturn

def twodsix():
        roller = random.randint(1,6) + random.randint(1,6)
        return twodsix

def character_race():
        race = ["Orc","human","elf","halfling","dwarf","gnome"]
        racenum = [0,1,2,3,4,5]
        racechoicenum = random.choice(racenum)
        racechoice = race[racechoicenum]
        racechoice = "Orc"
        c_race = racechoice
        return racechoice

def character_focus():
        return focus

def race_benefits():
        global c_name
        global c_focus
        global c_talent
        global c_stats
        global c_language
        global c_race
        benefits = []
        benefits2 = []
        for iteration in range(1,10):
                benny = random.choice([1,2,2,3,4,5,5,6,7,7,8])
                benefits.append(benny)
        # Shitty dedupper is shitty - JR
        benefits = list(set(benefits))
        roller = random.randint(1,len(benefits))
        benefits2.append(benefits[roller - 1])
        benefits.remove(benefits[roller - 1])
        roller = random.randint(1,len(benefits))
        benefits2.append(benefits[roller - 1])
        print (benefits2)
        for iteration in range(1,3):
                if benefits2[iteration - 1] == 1:
                         if c_race == "Orc":
                                 #print "1 and Orc"
                                 c_stats[2] = c_stats[2] +1
                         elif c_race == "elf":
                                 print "1 and elf"
                         elif c_race == "human":
                                 print "1 and human"
                         elif c_race == "halfling":
                                 print "1 and halfling"
                                 #WTF do people play halflings?
                         elif c_race == "gnome":
                                 print "1 and gnome"
                                 #Gnomes are fugly halflings
                         elif c_race == "dwarf":
                                 print "1 and dwarf"
                         else:
                                 print "DEBUG: No Race match"
                elif benefits2[iteration - 1] == 2:
                         if c_race == "Orc":
                                 #print "1 and Orc"
                                 c_focus.append("Perception(Smelling)")
                         elif c_race == "elf":
                                 print "1 and elf"
                         elif c_race == "human":
                                 print "1 and human"
                         elif c_race == "halfling":
                                 print "1 and halfling"
                                 #WTF do people play halflings?
                         elif c_race == "gnome":
                                 print "1 and gnome"
                                 #Gnomes are fugly halflings
                         elif c_race == "dwarf":
                                 print "1 and dwarf"
                         else:
                                 print "DEBUG: No Race match"

                elif benefits2[iteration - 1] == 3:
                         if c_race == "Orc":
                                 #print "1 and Orc"
                                 c_focus.append("Dexterity(Stealth)")
                         elif c_race == "elf":
                                 print "1 and elf"
                         elif c_race == "human":
                                 print "1 and human"
                         elif c_race == "halfling":
                                 print "1 and halfling"
                                 #WTF do people play halflings?
                         elif c_race == "gnome":
                                 print "1 and gnome"
                                 #Gnomes are fugly halflings
                         elif c_race == "dwarf":
                                 print "1 and dwarf"
                         else:
                                 print "DEBUG: No Race match"

                elif benefits2[iteration - 1] == 4:
                         if c_race == "Orc":
                                 #print "1 and Orc"
                                 c_focus.append("Strength(Intimidation)")
                         elif c_race == "elf":
                                 print "1 and elf"
                         elif c_race == "human":
                                 print "1 and human"
                         elif c_race == "halfling":
                                 print "1 and halfling"
                                 #WTF do people play halflings?
                         elif c_race == "gnome":
                                 print "1 and gnome"
                                 #Gnomes are fugly halflings
                         elif c_race == "dwarf":
                                 print "1 and dwarf"
                         else:
                                 print "DEBUG: No Race match"

                elif benefits2[iteration - 1] == 5:
                         if c_race == "Orc":
                                 #print "1 and Orc"
                                 c_stats[4] = c_stats[4] +1
                         elif c_race == "elf":
                                 print "1 and elf"
                         elif c_race == "human":
                                 print "1 and human"
                         elif c_race == "halfling":
                                 print "1 and halfling"
                                 #WTF do people play halflings?
                         elif c_race == "gnome":
                                 print "1 and gnome"
                                 #Gnomes are fugly halflings
                         elif c_race == "dwarf":
                                 print "1 and dwarf"
                         else:
                                 print "DEBUG: No Race match"

                elif benefits2[iteration - 1] == 6:
                         if c_race == "Orc":
                                 #print "1 and Orc"
                                 c_focus.append("Weapon Group or Focus(Bludgeons)")
                         elif c_race == "elf":
                                 print "1 and elf"
                         elif c_race == "human":
                                 print "1 and human"
                         elif c_race == "halfling":
                                 print "1 and halfling"
                                 #WTF do people play halflings?
                         elif c_race == "gnome":
                                 print "1 and gnome"
                                 #Gnomes are fugly halflings
                         elif c_race == "dwarf":
                                 print "1 and dwarf"
                         else:
                                 print "DEBUG: No Race match"

                elif benefits2[iteration - 1] == 7:
                         if c_race == "Orc":
                                 #print "1 and Orc"
                                 c_focus.append("Accuracy(Brawling)")
                         elif c_race == "elf":
                                 print "1 and elf"
                         elif c_race == "human":
                                 print "1 and human"
                         elif c_race == "halfling":
                                 print "1 and halfling"
                                 #WTF do people play halflings?
                         elif c_race == "gnome":
                                 print "1 and gnome"
                                 #Gnomes are fugly halflings
                         elif c_race == "dwarf":
                                 print "1 and dwarf"
                         else:
                                 print "DEBUG: No Race match"

                elif benefits2[iteration - 1] == 8:
                         if c_race == "Orc":
                                 #print "1 and Orc"
                                 c_stats[8] = c_stats[8] +1
                         elif c_race == "elf":
                                 print "1 and elf"
                         elif c_race == "human":
                                 print "1 and human"
                         elif c_race == "halfling":
                                 print "1 and halfling"
                                 #WTF do people play halflings?
                         elif c_race == "gnome":
                                 print "1 and gnome"
                                 #Gnomes are fugly halflings
                         elif c_race == "dwarf":
                                 print "1 and dwarf"
                         else:
                                 print "DEBUG: No Race match"
                         #       
                else:
                       print "No match"


                        
        
                        

def Orc():
        global c_name
        global c_focus
        global c_talent
        global c_stats
        global c_language
        global c_race
        #Names first and last
        f_name = random.choice(["Beska","Eldra","Grisha","Mag","Oota","Vol","Feld","Gar","Harsk","Kurg","Scag","Tor"])
        l_name = random.choice(["Blackfire","Heartblood","Irontusk","Redaxe","Sunder"])
        c_name = f_name + " " + l_name
        #static additions for the race follow
        #add 1 Strength
        c_stats[7] = c_stats[7] + 1
        #Choose between two foci
        r_focus = random.choice(["Constitution(Stamina)","Strength(Might"])
        c_focus.append(r_focus)
        #Add Darksight
        c_talent.append("Darksight")
        c_language.append("You can speak and read Orcish and the Common Tongue")
        #Benefits table to follow
        race_benefits()
        c_stats[9] = 10 + c_stats[3]

      

def character_class():
        global c_name
        global c_stats
        global c_focus
        global c_talent
        global c_language
        global c_class

        #Constitution, Dexterity, Fighting, and Strength
        W_affinity = c_stats[2] + c_stats[3] + c_stats[4] + c_stats[7]
        #acc int per will
        M_affinity = c_stats[0] + c_stats[5] + c_stats[6] + c_stats[8]
        #Accuracy, Communication, Dexterity, and Perception
        R_affinity = c_stats[0] + c_stats[1] + c_stats[3] + c_stats[6]
        # 0 accuracy, 1 communication, 2 constitution,3 dexterity,4 fighting, 5 inteliignece, 6 perception, 7 strength, 8 willpower 9 Speed 10 Defence 11 Health 12 MP
        if W_affinity > M_affinity and W_affinity > R_affinity:
                c_class="Warrior"
        elif M_affinity > W_affinity and M_affinity > R_affinity:
                c_class="Mage"
        else:
                c_class="Rogue"
        return c_class


def character_assemble():
        global c_name
        global c_stats
        global c_focus
        global c_talent
        global c_language
        global c_class
        global c_race
        c_focus = []
        c_talent = []
        c_language = []
        c_stats = [charattr(),charattr(),charattr(),charattr(),charattr(),charattr(),charattr(),charattr(),charattr(),0,0,0,0,0]
        c_class = character_class()
        c_race = character_race()
        func=getattr(sys.modules[__name__], c_race)
        func()
        #Only Orcs work currently. Ideally we break out race definitions into seperate modules.
        print c_name
        print c_race
        print c_class
        print (c_stats)
        print (c_focus)
        print (c_talent) 
        print "Speed"
        print c_stats[9]
        print (c_language) 
# Array is as follows:
# 0 accuracy, 1 communication, 2 constitution,3 dexterity,4 fighting, 5 inteliignece, 6 perception, 7 strength, 8 willpower 9 Speed 10 Defence 11 Health 12 MP
character_assemble()

