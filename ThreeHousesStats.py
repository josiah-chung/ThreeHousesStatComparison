#This project uses data from characters from one of my favorite strategy video games, Fire Emblem: Three Houses. In this game, you choose around 10 characters from a pool of about 40 characters to fight with you throughout the game. I created this project so that I could compare the statistics of each character to inform my decision of who may be best to choose.
#Every character has a BASE and GROWTH stat for nine different stats: HP, Strength, Magic, Dexterity, Speed, Luck, Defense, Resistance, and Charm. For example, every character has a BASE HP stat and a corresponding GROWTH HP stat.
#Your BASE stat is the number you start with at Level 1. Your GROWTH stat is the probability that you will gain one point in that stat each time you level up. For example, if my BASE HP is 5 and my GROWTH HP is 50, there is a 50 percent chance I will grow from 5 HP to 6 HP upon leveling up.
#Taking the above information into consideration, I wanted to make a program that could compare which of the 40 characters would be the strongest (on average) after leveling up 30 times.


# This Statlist() function allows you to create a list for any character you want to compare. The function accepts a name as a string and 18 stats as ints and returns a list of three dictionaries; one dictionary has the name, one dictionary holds the BASE stats, and one dictionary holds the GROWTH stats. 
def Statlist(Name, BHP, BStr, BMag, BDex, BSpd, BLck, BDef, BRes, BCharm, GHP, GStr, GMag, GDex, GSpd, GLck, GDef, GRes, GCharm):
    ListofDicts = [{"Name":Name}, {"B_HP":BHP, "B_Str":BStr, "B_Mag":BMag, "B_Dex":BDex, "B_Spd":BSpd, "B_Lck":BLck, "B_Def":BDef, "B_Res":BRes, "B_Charm":BCharm}, {"G_HP":GHP, "G_Str":GStr, "G_Mag":GMag, "G_Dex":GDex, "G_Spd":GSpd, "G_Lck":GLck, "G_Def":GDef, "G_Res":GRes, "G_Charm":GCharm}]
    return ListofDicts

# After using the Statlist() function to create a character that you want to compare, this growth() function will list out on average how strong each character's stats will be after leveling up 30 times.
def growth(character = [], name = ""):
    #To calculate each stat after 30 levels, we take the BASE stat, which is their starting value, then add it to the GROWTH stat. Since the Growth stats are listed as a percent and we are calculating the final value after the character levels up 30 times, we multiply the growth stat by 30/100 or 0.3
    FinalHP = character[1]["B_HP"] + ((character[2]["G_HP"])*(.3))
    FinalStr = character[1]["B_Str"] + ((character[2]["G_Str"])*(.3))
    FinalMag = character[1]["B_Mag"] + ((character[2]["G_Mag"])*(.3))
    FinalDex = character[1]["B_Dex"] + ((character[2]["G_Dex"])*(.3))
    FinalSpd = character[1]["B_Spd"] + ((character[2]["G_Spd"])*(.3))
    FinalLck = character[1]["B_Lck"] + ((character[2]["G_Lck"])*(.3))
    FinalDef = character[1]["B_Def"] + ((character[2]["G_Def"])*(.3))
    FinalRes = character[1]["B_Res"] + ((character[2]["G_Res"])*(.3))
    FinalCharm = character[1]["B_Charm"] + ((character[2]["G_Charm"])*(.3))
    TotalStat = FinalHP + FinalStr + FinalMag + FinalDex + FinalSpd + FinalLck + FinalRes + FinalCharm

    output_string = ""
    output_string += name + ":\n"
    output_string += "Final HP: " + str(FinalHP) + "\n"
    output_string += "Final Strength: " + str(FinalStr) + "\n"
    output_string += "Final Magic: " + str(FinalMag) + "\n"
    output_string += "Final Dexterity: " + str(FinalDex) + "\n"
    output_string += "Final Speed: " + str(FinalSpd) + "\n"
    output_string += "Final Luck: " + str(FinalLck) + "\n"
    output_string += "Final Defense: " + str(FinalDef) + "\n"
    output_string += "Final Resistance: " + str(FinalRes) + "\n"
    output_string += "Final Charm: " + str(FinalCharm) + "\n"
    output_string += "Overall Stats: " + str(TotalStat) + "\n"
    return output_string


#As an example, I have pulled the data for eight characters from the website listed below and have imported them into my program using my Statlist() function.
#https://fireemblem.fandom.com/wiki/List_of_characters_in_Fire_Emblem:_Three_Houses
Claude = Statlist("Claude", 26, 11, 5, 8, 8, 7, 6, 4, 8, 35, 40, 25, 60, 55, 45, 30, 25, 55)
Lorenz = Statlist("Lorenz", 28, 8, 7, 6, 7, 5, 6, 6, 3, 55, 40, 40, 45, 40, 25, 30 ,40, 35)
Raphael = Statlist("Raphael", 30, 11, 3, 5, 6, 6, 7, 1, 4, 65, 50, 15, 35, 15, 35, 45, 10, 25)
Ignatz = Statlist("Ignatz", 25, 8, 5, 7, 8, 8, 4, 6, 4, 35, 35, 30, 50, 50, 55, 25, 35, 25)
Lysithea = Statlist("Lysithea", 22, 4, 11, 7, 7, 4, 3, 4, 5, 20, 15, 60, 60, 50, 15, 10, 25, 25)
Marianne = Statlist("Marianne", 23, 5, 11, 6, 7, 6, 4, 8, 7, 35, 20, 50, 40, 40, 35, 15, 45, 40)
Hilda = Statlist("Hilda", 29, 10, 5, 5, 8, 6, 6, 3, 7, 50, 45, 25, 30, 50, 35, 35, 20, 50)
Leonie = Statlist("Leonie", 26, 9, 5, 8, 9, 6, 7, 2, 7, 40, 40, 20, 55, 60, 40, 40, 15, 40)

#Here I use the growth() function to print and compare the stats each character.
print(growth(Claude, "Claude"))
print(growth(Lorenz, "Lorenz"))
print(growth(Raphael, "Raphael"))
print(growth(Ignatz, "Ignatz"))
print(growth(Lysithea, "Lysithea"))
print(growth(Marianne, "Marianne"))
print(growth(Hilda, "Hilda"))
print(growth(Leonie, "Leonie"))

#Viewing the output of the growth() function is nice, but what if I want to make more direct comparisons between two characters? The function below accomplishes this.
#This function accepts two lists for two characters that you want to compare. This function also accepts a third list in which you can add any stat(s) that you want to compare for the characters.
def compare(character1 = [], character2 = [], statlist = []):
    AcceptedStrings = ["hp", "strength", "magic", "dexterity", "speed", "luck", "defense", "resistance", "charm", "total"]
    returnstring = ""

    #calculating the stats of the two characters we want to compare
    FinalHP1 = character1[1]["B_HP"] + ((character1[2]["G_HP"])*(.3))
    FinalStr1 = character1[1]["B_Str"] + ((character1[2]["G_Str"])*(.3))
    FinalMag1 = character1[1]["B_Mag"] + ((character1[2]["G_Mag"])*(.3))
    FinalDex1 = character1[1]["B_Dex"] + ((character1[2]["G_Dex"])*(.3))
    FinalSpd1 = character1[1]["B_Spd"] + ((character1[2]["G_Spd"])*(.3))
    FinalLck1 = character1[1]["B_Lck"] + ((character1[2]["G_Lck"])*(.3))
    FinalDef1 = character1[1]["B_Def"] + ((character1[2]["G_Def"])*(.3))
    FinalRes1 = character1[1]["B_Res"] + ((character1[2]["G_Res"])*(.3))
    FinalCharm1 = character1[1]["B_Charm"] + ((character1[2]["G_Charm"])*(.3))
    TotalStat1 = FinalHP1 + FinalStr1 + FinalMag1 + FinalDex1 + FinalSpd1 + FinalLck1 + FinalRes1 + FinalCharm1

    FinalHP2 = character2[1]["B_HP"] + ((character2[2]["G_HP"])*(.3))
    FinalStr2 = character2[1]["B_Str"] + ((character2[2]["G_Str"])*(.3))
    FinalMag2 = character2[1]["B_Mag"] + ((character2[2]["G_Mag"])*(.3))
    FinalDex2 = character2[1]["B_Dex"] + ((character2[2]["G_Dex"])*(.3))
    FinalSpd2 = character2[1]["B_Spd"] + ((character2[2]["G_Spd"])*(.3))
    FinalLck2 = character2[1]["B_Lck"] + ((character2[2]["G_Lck"])*(.3))
    FinalDef2 = character2[1]["B_Def"] + ((character2[2]["G_Def"])*(.3))
    FinalRes2 = character2[1]["B_Res"] + ((character2[2]["G_Res"])*(.3))
    FinalCharm2 = character2[1]["B_Charm"] + ((character2[2]["G_Charm"])*(.3))
    TotalStat2 = FinalHP2 + FinalStr2 + FinalMag2 + FinalDex2 + FinalSpd2 + FinalLck2 + FinalRes2 + FinalCharm2

    #this loop will take the calculated stats and report the comparison(s) that you want to make
    for stat in statlist:
        if stat.lower() in AcceptedStrings:
            if stat.lower() == "hp":
                if FinalHP1 > FinalHP2:
                    returnstring += character1[0]["Name"] + " has higher HP than " + character2[0]["Name"] + ".\n"
                elif FinalHP1 < FinalHP2:
                    returnstring += character2[0]["Name"] + " has higher HP than " + character1[0]["Name"] + ".\n"
                elif FinalHP1 == FinalHP2:
                    returnstring += character1[0]["Name"] + " and " + character2[0]["Name"] + " have equal HP.\n"
            if stat.lower() == "strength":
                if FinalStr1 > FinalStr2:
                    returnstring += character1[0]["Name"] + " has higher strength than " + character2[0]["Name"] + ".\n"
                elif FinalStr1 < FinalStr2:
                    returnstring += character2[0]["Name"] + " has higher strength than " + character1[0]["Name"] + ".\n"
                elif FinalStr1 == FinalStr2:
                    returnstring += character1[0]["Name"] + " and " + character2[0]["Name"] + " have equal strength.\n"
            if stat.lower() == "magic":
                if FinalMag1 > FinalMag2:
                    returnstring += character1[0]["Name"] + " has higher magic than " + character2[0]["Name"] + ".\n"
                elif FinalMag1 < FinalMag2:
                    returnstring += character2[0]["Name"] + " has higher magic than " + character1[0]["Name"] + ".\n"
                elif FinalMag1 == FinalMag2:
                    returnstring += character1[0]["Name"] + " and " + character2[0]["Name"] + " have equal magic.\n"
            if stat.lower() == "dexterity":
                if FinalDex1 > FinalDex2:
                    returnstring += character1[0]["Name"] + " has higher dexterity than " + character2[0]["Name"] + ".\n"
                elif FinalDex1 < FinalDex2:
                    returnstring += character2[0]["Name"] + " has higher dexterity than " + character1[0]["Name"] + ".\n"
                elif FinalDex1 == FinalDex2:
                    returnstring += character1[0]["Name"] + " and " + character2[0]["Name"] + " have equal dexterity.\n"
            if stat.lower() == "speed":
                if FinalSpd1 > FinalSpd2:
                    returnstring += character1[0]["Name"] + " has higher speed than " + character2[0]["Name"] + ".\n"
                elif FinalSpd1 < FinalSpd2:
                    returnstring += character2[0]["Name"] + " has higher speed than " + character1[0]["Name"] + ".\n"
                elif FinalSpd1 == FinalSpd2:
                    returnstring += character1[0]["Name"] + " and " + character2[0]["Name"] + " have equal speed.\n"
            if stat.lower() == "luck":
                if FinalLck1 > FinalLck2:
                    returnstring += character1[0]["Name"] + " has higher luck than " + character2[0]["Name"] + ".\n"
                elif FinalLck1 < FinalLck2:
                    returnstring += character2[0]["Name"] + " has higher luck than " + character1[0]["Name"] + ".\n"
                elif FinalLck1 == FinalLck2:
                    returnstring += character1[0]["Name"] + " and " + character2[0]["Name"] + " have equal luck.\n"
            if stat.lower() == "defense":
                if FinalDef1 > FinalDef2:
                    returnstring += character1[0]["Name"] + " has higher defense than " + character2[0]["Name"] + ".\n"
                elif FinalDef1 < FinalDef2:
                    returnstring += character2[0]["Name"] + " has higher defense than " + character1[0]["Name"] + ".\n"
                elif FinalDef1 == FinalDef2:
                    returnstring += character1[0]["Name"] + " and " + character2[0]["Name"] + " have equal defense.\n"
            if stat.lower() == "resistance":
                if FinalRes1 > FinalRes2:
                    returnstring += character1[0]["Name"] + " has higher resistance than " + character2[0]["Name"] + ".\n"
                elif FinalRes1 < FinalRes2:
                    returnstring += character2[0]["Name"] + " has higher resistance than " + character1[0]["Name"] + ".\n"
                elif FinalRes1 == FinalRes2:
                    returnstring += character1[0]["Name"] + " and " + character2[0]["Name"] + " have equal resistance.\n"
            if stat.lower() == "charm":
                if FinalCharm1 > FinalCharm2:
                    returnstring += character1[0]["Name"] + " has higher charm than " + character2[0]["Name"] + ".\n"
                elif FinalCharm1 < FinalCharm2:
                    returnstring += character2[0]["Name"] + " has higher charm than " + character1[0]["Name"] + ".\n"
                elif FinalCharm1 == FinalCharm2:
                    returnstring += character1[0]["Name"] + " and " + character2[0]["Name"] + " have equal charm.\n"
            if stat.lower() == "total":
                if TotalStat1 > TotalStat2:
                    returnstring += character1[0]["Name"] + " has higher total stats than " + character2[0]["Name"] + ".\n"
                elif TotalStat1 < TotalStat2:
                    returnstring += character2[0]["Name"] + " has higher total stats than " + character1[0]["Name"] + ".\n"
                elif TotalStat1 == TotalStat2:
                    returnstring += character1[0]["Name"] + " and " + character2[0]["Name"] + " have equal total stats.\n"
    return returnstring

#Let's say for example that I want to compare who has a higher magic stat between Claude and Lysithea:
print(compare(Claude, Lysithea, ["magic"]))

#Or maybe I want to see who has higher HP and strength between Hilda and Lorenz:
print(compare(Hilda, Lorenz, ["HP", "strength"]))

#Maybe I want to compare every single stat, including the total, between Raphael and Leonie:
print(compare(Raphael, Leonie, ["hp", "strength", "magic", "dexterity", "speed", "luck", "defense", "resistance", "charm", "total"]))
    






























    
