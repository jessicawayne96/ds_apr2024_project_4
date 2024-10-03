import pandas as pd
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(self,character,strength,speed,intelligence,specialAbilities,weaknesses):
    
        character_batman = 0
        character_captain_america = 0
        character_flash = 0
        character_iron_man = 0
        character_spider_man = 0
        character_superman = 0
        character_thor = 0
        character_wonder_woman = 0
        weaknesses_kryptonite = 0
        weaknesses_magic = 0
        weaknesses_silver = 0
        weaknesses_wooden_stake = 0
        specialAbilities_flight = 0
        specialAbilities_invisibility = 0
        specialAbilities_super_strength = 0
        specialAbilities_telekinesis = 0

        # parse character
        if (character == "Batman"):
            character_batman = 1
        elif (character == "Captain America"):
            character_captain_america = 1
        elif (character == "Flash"):
            character_flash = 1
        elif (character == "Iron Man"):
            character_iron_man = 1
        elif (character == "Spider Man"):
            character_spider_man = 1
        elif (character == "Superman"):
            character_superman = 1
        elif (character == "Thor"):
            character_thor = 1
        elif (character == "Wonder Woman"):
            character_wonder_woman = 1
        else:
            pass

        # parse weakness
        if (weaknesses == "Kryptonite"):
            weaknesses_kryptonite = 1
        elif (weaknesses == "Magic"):
            weaknesses_magic = 1
        elif (weaknesses == "Silver"):
            weaknesses_silver = 1
        elif (weaknesses == "Wooden Stake"):
            weaknesses_wooden_stake = 1
        else:
            pass

        # parse abillity 
        if (specialAbilities == "Flight"):
            specialAbilities_flight = 1
        elif (specialAbilities == "Invisibility"):
            specialAbilities_invisibility = 1
        elif (specialAbilities == "Super Strength"):
            specialAbilities_super_strength = 1
        elif (specialAbilities == "Telekinesis"):
            specialAbilities_telekinesis = 1
        else:
            pass

        # create dataframe of one row for inference
        df = pd.DataFrame()
        df["Strength"] = [strength]
        df["Speed"] = [speed]
        df["Intelligence"] = [intelligence]
        df["Character_Batman"] = [character_batman]
        df["Character_Captain America"] = [character_captain_america]
        df["Character_Flash"] = [character_flash]
        df["Character_Iron Man"] = [character_iron_man] 
        df["Character_Spider-Man"] = [character_spider_man]
        df["Character_Superman"] = [character_superman]
        df["Character_Thor"] = [character_thor]
        df["Character_Wonder Woman"] = [character_wonder_woman]
        df["SpecialAbilities_Flight"] = [specialAbilities_flight]
        df["SpecialAbilities_Invisibility"] = [specialAbilities_invisibility]
        df["SpecialAbilities_Super Strength"] = [specialAbilities_super_strength]
        df["SpecialAbilities_Telekinesis"] = [specialAbilities_telekinesis]
        df["Weaknesses_Kryptonite"] = [weaknesses_kryptonite]
        df["Weaknesses_Magic"] = [weaknesses_magic]
        df["Weaknesses_Silver"] = [weaknesses_silver]
        df["Weaknesses_Wooden Stake"] = [weaknesses_wooden_stake]
        

        # model
        model = pickle.load(open("battle_model.pkl", 'rb'))

        # columns in order
        df = df.loc[:, ['Strength', 'Speed', 'Intelligence',
       'Character_Batman', 'Character_Captain America', 'Character_Flash',
       'Character_Iron Man', 'Character_Spider-Man', 'Character_Superman',
       'Character_Thor', 'Character_Wonder Woman', 'SpecialAbilities_Flight',
       'SpecialAbilities_Invisibility', 'SpecialAbilities_Super Strength',
       'SpecialAbilities_Telekinesis', 'Weaknesses_Kryptonite',
       'Weaknesses_Magic', 'Weaknesses_Silver', 'Weaknesses_Wooden Stake']]

        preds = model.predict_proba(df)
        return(preds[0][1])
