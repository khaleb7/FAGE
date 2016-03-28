#!/usr/bin/python
import random 
import sys
#Added Elves


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
        race = ["Orc","Human","Elf","Halfling","Dwarf","Gnome"]
        racenum = [0,2,4,5]
        racechoicenum = random.choice(racenum)
        racechoice = race[racechoicenum]
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
                         elif c_race == "Elf":
                                 c_stats[1] = c_stats[1] +1
                         elif c_race == "Human":
                                 print "1 and Human"
                         elif c_race == "Halfling":
                                 print "1 and Halfling"
                                 #WTF do people play Halflings?
                         elif c_race == "Gnome":
                                 c_stats[2] = c_stats[2] +1
                         elif c_race == "Dwarf":
                                 c_stats[8] = c_stats[8] +1
                         else:
                                 print "DEBUG: No Race match"
                elif benefits2[iteration - 1] == 2:
                         if c_race == "Orc":
                                 #print "1 and Orc"
                                 c_focus.append("Perception(Smelling)")
                         elif c_race == "Elf":
                                 c_focus.append("Intelligence(Cultural Lore)")
                         elif c_race == "Human":
                                 print "1 and Human"
                         elif c_race == "Halfling":
                                 print "1 and Halfling"
                                 #WTF do people play Halflings?
                         elif c_race == "Gnome":
                                 c_focus.append("Dexterity(Traps)")
                                 
                         elif c_race == "Dwarf":
                                 c_focus.append("Intelligence(Historical Lore)")
                         else:
                                 print "DEBUG: No Race match"

                elif benefits2[iteration - 1] == 3:
                         if c_race == "Orc":
                                 #print "1 and Orc"
                                 c_focus.append("Dexterity(Stealth)")
                         elif c_race == "Elf":
                                 c_focus.append("Perception(Hearing)")
                         elif c_race == "Human":
                                 print "1 and Human"
                         elif c_race == "Halfling":
                                 print "1 and Halfling"
                                 #WTF do people play Halflings?
                         elif c_race == "Gnome":
                                 c_focus.append("Intelligence(Evaluation)")
                         elif c_race == "Dwarf":
                                 c_focus.append("Constitution(Stamina)")
                         else:
                                 print "DEBUG: No Race match"

                elif benefits2[iteration - 1] == 4:
                         if c_race == "Orc":
                                 #print "1 and Orc"
                                 c_focus.append("Strength(Intimidation)")
                         elif c_race == "Elf":
                                 c_focus.append("Weapon Group or Focus(Bows)")
                         elif c_race == "Human":
                                 print "1 and Human"
                         elif c_race == "Halfling":
                                 print "1 and Halfling"
                                 #WTF do people play Halflings?
                         elif c_race == "Gnome":
                                 c_focus.append("Perception(Hearing)")
                         elif c_race == "Dwarf":
                                 c_focus.append("Weapon Group or Focus(Axes)")
                         else:
                                 print "DEBUG: No Race match"

                elif benefits2[iteration - 1] == 5:
                         if c_race == "Orc":
                                 #print "1 and Orc"
                                 c_stats[4] = c_stats[4] +1
                         elif c_race == "Elf":
                                 c_stats[0] = c_stats[0] +1
                         elif c_race == "Human":
                                 print "1 and Human"
                         elif c_race == "Halfling":
                                 print "1 and Halfling"
                                 #WTF do people play Halflings?
                         elif c_race == "Gnome":
                                 c_stats[8] = c_stats[8] +1
                         elif c_race == "Dwarf":
                                 c_stats[4] = c_stats[4] +1
                         else:
                                 print "DEBUG: No Race match"

                elif benefits2[iteration - 1] == 6:
                         if c_race == "Orc":
                                 #print "1 and Orc"
                                 c_focus.append("Weapon Group or Focus(Bludgeons)")
                         elif c_race == "Elf":
                                 c_focus.append("Dexterity(Initiative)")
                         elif c_race == "Human":
                                 print "1 and Human"
                         elif c_race == "Halfling":
                                 print "1 and Halfling"
                                 #WTF do people play Halflings?
                         elif c_race == "Gnome":
                                 c_focus.append("Intelligence(Arcane Lore)")
                         elif c_race == "Dwarf":
                                 c_focus.append("Strength(Smithing)")
                         else:
                                 print "DEBUG: No Race match"

                elif benefits2[iteration - 1] == 7:
                         if c_race == "Orc":
                                 #print "1 and Orc"
                                 c_focus.append("Accuracy(Brawling)")
                         elif c_race == "Elf":
                                 c_focus.append("Communication(Persuasion)")
                         elif c_race == "Human":
                                 print "1 and Human"
                         elif c_race == "Halfling":
                                 print "1 and Halfling"
                                 #WTF do people play Halflings?
                         elif c_race == "Gnome":
                                 c_focus.append("Communication(Bargaining)")
                         elif c_race == "Dwarf":
                                 c_focus.append("Intelligence(Engineering)")
                         else:
                                 print "DEBUG: No Race match"

                elif benefits2[iteration - 1] == 8:
                         if c_race == "Orc":
                                 #print "1 and Orc"
                                 c_stats[8] = c_stats[8] +1
                         elif c_race == "Elf":
                                 c_stats[6] = c_stats[6] +1
                         elif c_race == "Human":
                                 print "1 and Human"
                         elif c_race == "Halfling":
                                 print "1 and Halfling"
                                 #WTF do people play Halflings?
                         elif c_race == "Gnome":
                                 c_stats[5] = c_stats[5] +1
                         elif c_race == "Dwarf":
                                 c_stats[7] = c_stats[7] +1
                         else:
                                 print "DEBUG: No Race match"
                         #       
                else:
                       print "No match"


                        
#define races        
                        

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
        r_focus = random.choice(["Constitution(Stamina)","Strength(Might)"])
        c_focus.append(r_focus)
        #Add Darksight
        c_talent.append("Darksight")
        c_language.append("You can speak and read Orcish and the Common Tongue")
        #Benefits table to follow
        race_benefits()
        c_stats[9] = 10 + c_stats[3]


def Dwarf():
        global c_name
        global c_focus
        global c_talent
        global c_stats
        global c_language
        global c_race
        #Names first and last
        f_name = random.choice(["Ailine","Dara","Kalin","Klara","Ulma","Bodag","Crag","Doffin","Hador","Gurt","Throrik","Warrik"])
        l_name = random.choice(["Bronzeblade","Highcliff","Ironshield","Rockhammer","Steelhelm","Stonebones","Throshbeard","Bloodyaxe"])
        c_name = f_name + " " + l_name
        #static additions for the race follow
        #add 1 Constitution
        c_stats[2] = c_stats[2] + 1
        #Choose between two foci
        r_focus = random.choice(["Constitution(Drinking)","Intelligence(Evaluation)"])
        c_focus.append(r_focus)
        #Add Darksight
        c_talent.append("Darksight")
        c_language.append("You can speak and read Dwarven and the Common Tongue")
        #Benefits table to follow
        race_benefits()
        c_stats[9] = 8 + c_stats[3]

def Human():
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

def Halfling():
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

def Elf():
        global c_name
        global c_focus
        global c_talent
        global c_stats
        global c_language
        global c_race
        #Names first and last
        f_name = random.choice(["Alowar","Celemor","Elowen","Faerenel","Hereal","Lanathiel","Alagolin","Effoland","Kyriel","Larrendir","Melloran","Serren"])
        l_name = random.choice(["Andurari","Arvanor","Derendil","Ellendi","Kellowan","Talloran"])
        c_name = f_name + " " + l_name
        #static additions for the race follow
        #add 1 Dexterity
        c_stats[3] = c_stats[3] + 1
        #Choose between two foci
        r_focus = random.choice(["Intelligence(Natural Lore)","Perception(Seeing)"])
        c_focus.append(r_focus)
        #Add Darksight
        c_talent.append("Darksight")
        c_language.append("You can speak and read Elven and the Common Tongue")
        #Benefits table to follow
        race_benefits()
        c_stats[9] = 12 + c_stats[3]

def Gnome():
        global c_name
        global c_focus
        global c_talent
        global c_stats
        global c_language
        global c_race
        #Names first and last
        f_name = random.choice(["Alyce","Emma","Flora","Gale","Muriel","Ruby","Cog","Flinder","Garret","Hoster","Weldon","Yost"])
        l_name = random.choice(["Gemspinner","Goldwarren","Minder","Rocktapper","Trundle","Underhill"])
        c_name = f_name + " " + l_name
        #static additions for the race follow
        #add 1 Dex
        c_stats[3] = c_stats[3] + 1
        #Choose between two foci
        r_focus = random.choice(["Constitution(Stamina)","Dexterity(Legerdemain)"])
        c_focus.append(r_focus)
        #Add Darksight
        c_talent.append("Darksight")
        c_language.append("You can speak and read Gnomish and the Common Tongue")
        #Benefits table to follow
        race_benefits()
        c_stats[9] = 8 + c_stats[3]

      

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

def Mage():
        global c_name
        global c_stats
        global c_focus
        global c_talent
        global c_language
        global c_class
        roller = random.randint(1,6)
        c_stats[11] = 20 + c_stats[2] + roller
        s_talent = random.choice(["N: Chirurgy","N:Linguistics","N:Lore"])
        c_talent.append(s_talent)
        
def Rogue():
        global c_name
        global c_stats
        global c_focus
        global c_talent
        global c_language
        global c_class
        roller = random.randint(1,6)
        c_stats[11] = 25 + c_stats[2] + roller

def Warrior():
        global c_name
        global c_stats
        global c_focus
        global c_talent
        global c_language
        global c_class
        roller = random.randint(1,6)
        c_stats[11] = 30 + c_stats[2] + roller

def character_background():
        global c_name
        global c_stats
        global c_focus
        global c_talent
        global c_language
        global c_class
        global c_social
        rollera = random.randint(1,6)
        rollerb = random.randint(1,6)

        if rollera == 1:
                c_social = "Outsider"
                if rollerb == 1:
                      c_social = c_social + ": Criminal"
                      s_focus = random.choice(["Communication(Deception)","Dexterity(Lockpicking)"])
                      c_focus.append(s_focus)
                elif rollerb == 2:
                      c_social = c_social + ": Exile"
                      s_focus = random.choice(["Communication(Bargaining)","Intelligence(Cultural Lore)"])
                      c_focus.append(s_focus)
                elif rollerb == 3:
                      c_social = c_social + ": Hermit"
                      s_focus = random.choice(["Constitution(Stamina)","Willpower(SElf-Discipline)"])
                      c_focus.append(s_focus)
                elif rollerb == 4:
                      c_social = c_social + ": Pirate"
                      s_focus = random.choice(["Dexterity(Sailing)","Strength(Intimidation)"])
                      c_focus.append(s_focus)
                elif rollerb == 5:
                      c_social = c_social + ": Radical"
                      s_focus = random.choice(["Communication(Persuasion)","Communication(Leadership)"])
                      c_focus.append(s_focus)
                elif rollerb == 6:
                      c_social = c_social + ": Wanderer"
                      s_focus = random.choice(["Constitution(Stamina)","Intelligence(Navigation)"])
                      c_focus.append(s_focus)
                else:
                        print "Error Handling Here"

        elif rollera == 2 or rollera == 3:
                c_social = "Lower Class"
                if rollerb == 1:
                      c_social = c_social + ": Artist"
                      s_focus = random.choice(["Intelligence(Cultural Lore)","Intelligence(Evaluation)"])
                      c_focus.append(s_focus)
                elif rollerb == 2:
                      c_social = c_social + ": Laborer"
                      s_focus = random.choice(["Constitution(Stamina)","Strength(Might)"])
                      c_focus.append(s_focus)
                elif rollerb == 3:
                      c_social = c_social + ": Performer"
                      s_focus = random.choice(["Communication(Performance)","Intelligence(Musical Lore)"])
                      c_focus.append(s_focus)
                elif rollerb == 4:
                      c_social = c_social + ": Sailor"
                      s_focus = random.choice(["Constitution(Drinking)","Dexterity(Sailing)"])
                      c_focus.append(s_focus)
                elif rollerb == 5:
                      c_social = c_social + ": Soldier"
                      s_focus = random.choice(["Accuracy(Brawling)","Communication(Gambling)"])
                      c_focus.append(s_focus)
                elif rollerb == 6:
                      c_social = c_social + ": Tradesperson"
                      s_focus = random.choice(["Communication(Bargaining)","Intelligence(Evaluation)"])
                      c_focus.append(s_focus)
                else:
                        print "Error Handling Here"

        elif rollera == 4 or rollera == 5:
                c_social = "Middle Class"
                if rollerb == 1:
                      c_social = c_social + ": Guilder"
                      s_focus = random.choice(["Communication(Etiquette)","Dexterity(Crafting)"])
                      c_focus.append(s_focus)
                elif rollerb == 2:
                      c_social = c_social + ": Initiate"
                      s_focus = random.choice(["Intelligence(Religious Lore)","Willpower(Faith)"])
                      c_focus.append(s_focus)
                elif rollerb == 3:
                      c_social = c_social + ": Innkeeper"
                      s_focus = random.choice(["Communication(Bargaining)","Perception(Empathy)"])
                      c_focus.append(s_focus)
                elif rollerb == 4:
                      c_social = c_social + ": Merchant"
                      s_focus = random.choice(["Communication(Bargaining)","Communication(Deception)"])
                      c_focus.append(s_focus)
                elif rollerb == 5:
                      c_social = c_social + ": Scribe"
                      s_focus = random.choice(["Dexterity(Calligraphy)","Intelligence(Writing)"])
                      c_focus.append(s_focus)
                elif rollerb == 6:
                      c_social = c_social + ": Student"
                      s_focus = random.choice(["Intelligence(Historical Lore)","Intelligence(Research)"])
                      c_focus.append(s_focus)
                else:
                        print "Error Handling Here"

        elif rollera == 6:
                c_social = "Upper Class"
                if rollerb == 1:
                      c_social = c_social + ": Apprentice"
                      s_focus = random.choice(["Intelligence(Arcane Lore)","Intelligence(Research)"])
                      c_focus.append(s_focus)
                elif rollerb == 2:
                      c_social = c_social + ": Dilettante"
                      s_focus = random.choice(["Communication(Gambling)","Constitution(Drinking)"])
                      c_focus.append(s_focus)
                elif rollerb == 3:
                      c_social = c_social + ": Noble"
                      s_focus = random.choice(["Communication(Etiquette)","Intelligence(Heraldry)"])
                      c_focus.append(s_focus)
                elif rollerb == 4:
                      c_social = c_social + ": Official"
                      s_focus = random.choice(["Communication(Leadership)","Communication(Persuasion)"])
                      c_focus.append(s_focus)
                elif rollerb == 5:
                      c_social = c_social + ": Scholar"
                      s_focus = random.choice(["Intelligence(Religious Lore)","Intelligence(Historical Lore)"])
                      c_focus.append(s_focus)
                elif rollerb == 6:
                      c_social = c_social + ": Squire"
                      s_focus = random.choice(["Intelligence(Heraldry)","Intelligence(Military Lore)"])
                      c_focus.append(s_focus)
                else:
                        print "Error Handling Here"

                        
        else:
                print "Nothing"

        return c_social
      

                                       
def character_assemble():
        global c_name
        global c_stats
        global c_focus
        global c_talent
        global c_language
        global c_class
        global c_race
        global c_social
        c_focus = []
        c_talent = []
        c_language = []
        c_stats = [charattr(),charattr(),charattr(),charattr(),charattr(),charattr(),charattr(),charattr(),charattr(),0,0,0,0,0]
        c_class = character_class()
        c_race = character_race()
        ra_func=getattr(sys.modules[__name__], c_race)
        cl_func=getattr(sys.modules[__name__], c_class)
        ra_func()
        cl_func()
        c_social = character_background()
        print c_name
        print c_race
        print c_class
        print c_social
        print (c_stats)
        print (c_focus)
        print (c_talent) 
        print "Speed"
        print c_stats[9]
        print (c_language) 
# Array is as follows:
# 0 accuracy, 1 communication, 2 constitution,3 dexterity,4 fighting, 5 inteliignece, 6 perception, 7 strength, 8 willpower 9 Speed 10 Defence 11 Health 12 MP
character_assemble()

