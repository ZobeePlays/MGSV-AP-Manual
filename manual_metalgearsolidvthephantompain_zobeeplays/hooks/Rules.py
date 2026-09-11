from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"

def DogFultons():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "(|D-Dog| AND (|TACTICAL (FULTON) (D-Dog)| OR |D-Dog Equipment|))"

def WalkerFultons():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "(|D-Walker| AND (|@DWalkiesFultons:1| OR |D-Walker Equipment|))"

def Mission0():
    return "|Mission 0 - PROLOGUE; AWAKENING| OR ({YamlEnabled(Disable_Mission_Unlocks)})"

def Mission1():
    return "|Mission 1 - PHANTOM LIMBS| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 0 - PROLOGUE; AWAKENING - COMPLETE|)"

def Mission2():
    return "|Mission 2 - DIAMOND DOGS| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 1 - PHANTOM LIMBS - COMPLETE|)"

def Mission3():
    return "|Mission 3 - A HERO'S WAY| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 2 - DIAMOND DOGS - COMPLETE|)"

def Mission4():
    return "|Mission 4 - C2W| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 3 - A HERO'S WAY - COMPLETE|)"

def Mission5():
    return "|Mission 5 - OVER THE FENCE| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 4 - C2W - COMPLETE|)"

def Mission6():
    return "|Mission 6 - WHERE DO THE BEES SLEEP?| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 5 - OVER THE FENCE - COMPLETE|)"

def Mission7():
    return "|Mission 7 - RED BRASS| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 6 - WHERE DO THE BEES SLEEP? - COMPLETE|)"

def Mission8():
    return "|Mission 8 - OCCUPATION FORCES| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 7 - RED BRASS - COMPLETE|)"

def Mission9():
    return "|Mission 9 - BACKUP, BACK DOWN| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 8 - OCCUPATION FORCES - COMPLETE|)"

def Mission10():
    return "|Mission 10 - ANGEL WITH BROKEN WINGS| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 9 - BACKUP, BACK DOWN - COMPLETE|)"

def Mission11():
    return "|Mission 11 - CLOAKED IN SILENCE| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 10 - ANGEL WITH BROKEN WINGS - COMPLETE|)"

def Mission12():
    return "|Mission 12 - HELLBOUND| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 11 - CLOAKED IN SILENCE - COMPLETE|)"

def Mission13():
    return "|Mission 13 - PITCH DARK| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 12 - HELLBOUND - COMPLETE|)"

def Mission14():
    return "|Mission 14 - LINGUA FRANCA| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 13 - PITCH DARK - COMPLETE|)"

def Mission15():
    return "|Mission 15 - FOOTPRINTS OF PHANTOMS| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 14 - LINGUA FRANCA - COMPLETE|)"

def Mission16():
    return "|Mission 16 - TRAITORS' CARAVAN| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 15 - FOOTPRINTS OF PHANTOMS - COMPLETE|)"

def Mission17():
    return "|Mission 17 - RESCUE THE INTEL AGENTS| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 16 - TRAITORS' CARAVAN - COMPLETE|)"

def Mission18():
    return "|Mission 18 - BLOOD RUNS DEEP| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 17 - RESCUE THE INTEL AGENTS - COMPLETE|)"

def Mission19():
    return "|Mission 19 - ON THE TRAIL| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 18 - BLOOD RUNS DEEP - COMPLETE|)"

def Mission20():
    return "|Mission 20 - VOICES| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 19 - ON THE TRAIL - COMPLETE|)"

def Mission21():
    return "|Mission 21 - THE WAR ECONOMY| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 20 - VOICES - COMPLETE|)"

def Mission22():
    return "|Mission 22 - RETAKE THE PLATFORM| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 21 - THE WAR ECONOMY - COMPLETE|)"

def Mission23():
    return "|Mission 23 - THE WHITE MAMBA| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 22 - RETAKE THE PLATFORM - COMPLETE|)"

def Mission24():
    return "|Mission 24 - CLOSE CONTACT| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 23 - THE WHITE MAMBA - COMPLETE|)"

def Mission25():
    return "|Mission 25 - AIM TRUE, YE VENGEFUL| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 24 - CLOSE CONTACT - COMPLETE|)"

def Mission26():
    return "|Mission 26 - HUNTING DOWN| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 25 - AIM TRUE, YE VENGEFUL - COMPLETE|)"

def Mission27():
    return "|Mission 27 - ROOT CAUSE| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 26 - HUNTING DOWN - COMPLETE|)"

def Mission28():
    return "|Mission 28 - CODE TALKER| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 27 - ROOT CAUSE - COMPLETE|)"

def Mission29():
    return "|Mission 29 - METALLIC ARCHAEA| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 28 - CODE TALKER - COMPLETE|)"

def Mission30():
    return "|Mission 30 - SKULL FACE| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 29 - METALLIC ARCHAEA - COMPLETE|)"

def Mission31():
    return "|Mission 31 - SAHELANTHROPUS| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 30 - SKULL FACE - COMPLETE|)"

def Mission32():
    return "|Mission 32 - TO KNOW TOO MUCH| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |SAHELANTHROPUS DEFEATED|)"

def Mission33():
    return "|Mission 33 - [SUBSISTENCE] C2W| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 32 - TO KNOW TOO MUCH - COMPLETE|)"

def Mission34():
    return "|Mission 34 - [EXTREME] BACKUP, BACK DOWN| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 33 - [SUBSISTENCE] C2W - COMPLETE|)"

def Mission35():
    return "|Mission 35 - CURSED LEGACY| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 34 - [EXTREME] BACKUP, BACK DOWN - COMPLETE|) OR ({YamlEnabled(Disable_Mission_Unlocks)} AND {YamlDisabled(Repeat_Missions)} AND |[EVENT] Mission 32 - TO KNOW TOO MUCH - COMPLETE|)"

def Mission36():
    return "|Mission 36 - [TOTAL STEALTH] FOOTPRINTS OF PHANTOMS| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 35 - CURSED LEGACY - COMPLETE|)"

def Mission37():
    return "|Mission 37 - [EXTREME] TRAITORS' CARAVAN| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 36 - [TOTAL STEALTH] FOOTPRINTS OF PHANTOMS - COMPLETE|)"

def Mission38():
    return "|Mission 38 - EXTRAORDINARY| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 37 - [EXTREME] TRAITORS' CARAVAN - COMPLETE|) OR ({YamlEnabled(Disable_Mission_Unlocks)} AND {YamlDisabled(Repeat_Missions)} AND |[EVENT] Mission 35 - CURSED LEGACY - COMPLETE|)"

def Mission39():
    return "|Mission 39 - [TOTAL STEALTH] OVER THE FENCE| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 38 - EXTRAORDINARY - COMPLETE|)"

def Mission40():
    return "|Mission 40 - [EXTREME] CLOAKED IN SILENCE| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 39 - [TOTAL STEALTH] OVER THE FENCE - COMPLETE|)"

def Mission41():
    return "|Mission 41 - PROXY WAR WITHOUT END| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 40 - [EXTREME] CLOAKED IN SILENCE - COMPLETE|) OR ({YamlEnabled(Disable_Mission_Unlocks)} AND {YamlDisabled(Repeat_Missions)} AND |[EVENT] Mission 38 - EXTRAORDINARY - COMPLETE|)"

def Mission42():
    return "|Mission 42 - [EXTREME] METALLIC ARCHAEA| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 41 - PROXY WAR WITHOUT END - COMPLETE|)"

def Mission43():
    return "|Mission 43 - SHINING LIGHTS, EVEN IN DEATH| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 42 - [EXTREME] METALLIC ARCHAEA - COMPLETE|) OR ({YamlEnabled(Disable_Mission_Unlocks)} AND {YamlDisabled(Repeat_Missions)} AND |[EVENT] Mission 41 - PROXY WAR WITHOUT END - COMPLETE|)"

def Mission44():
    return "|Mission 44 - [TOTAL STEALTH] PITCH DARK| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 43 - SHINING LIGHTS, EVEN IN DEATH - COMPLETE|)"

def Mission45():
    return "|Quiet| AND |Mission 45 - A QUIET EXIT| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 44 - [TOTAL STEALTH] PITCH DARK - COMPLETE|) OR ({YamlEnabled(Disable_Mission_Unlocks)} AND {YamlDisabled(Repeat_Missions)} AND |[EVENT] Mission 43 - SHINING LIGHTS, EVEN IN DEATH - COMPLETE|)"

def Mission46():
    return "|Mission 46 - TRUTH; THE MAN WHO SOLD THE WORLD| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 45 - A QUIET EXIT - COMPLETE|)"

def Mission47():
    return "|Mission 47 - [TOTAL STEALTH] THE WAR ECONOMY| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |THE TRUTH|)"

def Mission48():
    return "|Mission 48 - [EXTREME] CODE TALKER| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 47 - [TOTAL STEALTH] THE WAR ECONOMY - COMPLETE|)"

def Mission49():
    return "|Mission 49 - [SUBSISTENCE] OCCUPATION FORCES| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 48 - [EXTREME] CODE TALKER - COMPLETE|)"

def Mission50():
    return "|Mission 50 - [EXTREME] SAHELANTHROPUS| OR ({YamlEnabled(Disable_Mission_Unlocks)} AND |[EVENT] Mission 49 - [SUBSISTENCE] OCCUPATION FORCES - COMPLETE|)"















































































