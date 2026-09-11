# Object classes from AP core, to represent an entire MultiWorld and this individual World that's part of it
from collections.abc import Callable, Sequence, Set
from typing import Any, Tuple
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState, Item
from options import PerGameCommonOptions
from collections import defaultdict

# Object classes from Manual -- extending AP core -- representing items and locations that are used in generation
from ..Items import ManualItem
from ..Locations import ManualLocation

# Raw JSON data from the Manual apworld, respectively:
#          data/game.json, data/items.json, data/locations.json, data/regions.json
#
from ..Data import game_table, item_table, location_table, region_table

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value, format_state_prog_items_key, ProgItemsCat, remove_specific_item

# calling logging.info("message") anywhere below in this file will output the message to both console and log file
import logging

########################################################################################
## Order of method calls when the world generates:
##    1. create_regions - Creates regions and locations
##    2. create_items - Creates the item pool
##    3. set_rules - Creates rules for accessing regions and locations
##    4. generate_basic - Runs any post item pool options, like place item/category
##    5. pre_fill - Creates the victory location
##
## The create_item method is used by plando and start_inventory settings to create an item from an item name.
## The fill_slot_data method will be used to send data to the Manual client for later use, like deathlink.
########################################################################################



# Use this function to change the valid filler items to be created to replace item links or starting items.
# Default value is the `filler_item_name` from game.json
def hook_get_filler_item_name(world: World, multiworld: MultiWorld, player: int) -> str | bool:
    return False

def before_generate_early(world, multiworld, player):
    print("MGSV DEBUG: Goal =",world.options.goal.value)
    match world.options.goal.value:
        case 1:
            world.options.Repeat_Missions.value = True
            world.options.Include_Chapter_2.value = True
            print("MGSV DEBUG: Chapter 2 and Repeat Missions Enabled")
        case 4:
            world.options.Include_Chapter_2.value = True
            print("MGSV DEBUG: Chapter 2 Enabled")
        case 5:
            world.options.Require_Paz.value = True
            print("MGSV DEBUG: Paz Enabled")

    print("MGSV DEBUG: Team Level Split =",world.options.Mother_Base_Team_Levels_Split.value)
    match world.options.Mother_Base_Team_Levels_Split.value:
        case 0:
            world.options.Development_Teams1.value = True
            world.options.Development_Teams2.value = False
            world.options.Development_Teams3.value = False
            world.options.Development_Teams5.value = False
            world.options.Development_Teams10.value = False
            world.options.Development_Teams162.value = False
            print("MGSV DEBUG: Team Levels set to 1")
        case 1:
            world.options.Development_Teams1.value = False
            world.options.Development_Teams2.value = True
            world.options.Development_Teams3.value = False
            world.options.Development_Teams5.value = False
            world.options.Development_Teams10.value = False
            world.options.Development_Teams162.value = False
            print("MGSV DEBUG: Team Levels set to 2")
        case 2:
            world.options.Development_Teams1.value = False
            world.options.Development_Teams2.value = False
            world.options.Development_Teams3.value = True
            world.options.Development_Teams5.value = False
            world.options.Development_Teams10.value = False
            world.options.Development_Teams162.value = False
            print("MGSV DEBUG: Team Levels set to 3")
        case 3:
            world.options.Development_Teams1.value = False
            world.options.Development_Teams2.value = False
            world.options.Development_Teams3.value = False
            world.options.Development_Teams5.value = True
            world.options.Development_Teams10.value = False
            world.options.Development_Teams162.value = False
            print("MGSV DEBUG: Team Levels set to 5")
        case 4:
            world.options.Development_Teams1.value = False
            world.options.Development_Teams2.value = False
            world.options.Development_Teams3.value = False
            world.options.Development_Teams5.value = False
            world.options.Development_Teams10.value = True
            world.options.Development_Teams162.value = False
            print("MGSV DEBUG: Team Levels set to 10")
        case 5:
            world.options.Development_Teams1.value = False
            world.options.Development_Teams2.value = False
            world.options.Development_Teams3.value = False
            world.options.Development_Teams5.value = False
            world.options.Development_Teams10.value = False
            world.options.Development_Teams162.value = True
            print("MGSV DEBUG: Team Levels set to 162")


    print("MGSV DEBUG: Development Item Unlocks handeling =",world.options.Item_Unlock_Handling.value)
    match world.options.Item_Unlock_Handling.value:
        case 0:
            world.options.ProgressiveWeapons.value = True
            world.options.SplitWeapons.value = False
            world.options.CombinedWeapons.value = False
            world.options.StaticProgressiveWeapons.value = True
            world.options.StaticProgCombo.value = True
            world.options.WeaponCategories.value = False
            print("MGSV DEBUG: Setting Dev Tree Unlocks to Progressive")
        case 1:
            world.options.ProgressiveWeapons.value = False
            world.options.SplitWeapons.value = True
            world.options.CombinedWeapons.value = False
            world.options.StaticProgressiveWeapons.value = True
            world.options.StaticProgCombo.value = True
            world.options.WeaponCategories.value = False
            print("MGSV DEBUG: Splitting Dev Tree Unlocks")
        case 2:
            world.options.ProgressiveWeapons.value = False
            world.options.SplitWeapons.value = False
            world.options.CombinedWeapons.value = True
            world.options.StaticProgressiveWeapons.value = True
            world.options.StaticProgCombo.value = False
            world.options.WeaponCategories.value = False
            print("MGSV DEBUG: Combining Dev Tree Unlocks")
        case 3:
            world.options.ProgressiveWeapons.value = False
            world.options.SplitWeapons.value = False
            world.options.CombinedWeapons.value = False
            world.options.StaticProgressiveWeapons.value = False
            world.options.StaticProgCombo.value = False
            world.options.WeaponCategories.value = True
            print("MGSV DEBUG: Setting Dev Tree Unlocks to Weapon Categories")


# Called before regions and locations are created. Not clear why you'd want this, but it's here. Victory location is included, but Victory event is not placed yet.
def before_create_regions(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after regions and locations are created, in case you want to see or modify that information. Victory location is included.
def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to remove locations from the world
    locationNamesToRemove: list[str] = [] # List of location names

    # Add your code here to calculate which locations to remove

    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if location.name in locationNamesToRemove:
                    region.locations.remove(location)

# This hook allows you to access the item names & counts before the items are created. Use this to increase/decrease the amount of a specific item in the pool
# Valid item_config key/values:
# {"Item Name": 5} <- This will create qty 5 items using all the default settings
# {"Item Name": {"useful": 7}} <- This will create qty 7 items and force them to be classified as useful
# {"Item Name": {"progression": 2, "useful": 1}} <- This will create 3 items, with 2 classified as progression and 1 as useful
# {"Item Name": {0b0110: 5}} <- If you know the special flag for the item classes, you can also define non-standard options. This setup
#       will create 5 items that are the "useful trap" class
# {"Item Name": {ItemClassification.useful: 5}} <- You can also use the classification directly
def before_create_items_all(item_config: dict[str, int | dict], world: World, multiworld: MultiWorld, player: int) -> dict[str, int | dict]:
    from ..Helpers import get_option_value, is_option_enabled

    # Option evaluations moved INSIDE the function
    SDiamonds = is_option_enabled(multiworld, player, "Include_Small_Diamonds")
    Blueprints = is_option_enabled(multiworld, player, "Include_Blueprints")
    Animals = is_option_enabled(multiworld, player, "Include_Animals")
    Development = is_option_enabled(multiworld, player, "Include_Development_Tree")
    
    unlock_val = get_option_value(multiworld, player, "Item_Unlock_Handling")
    ProgUnlocks = unlock_val == 0
    SplitUnlocks = unlock_val == 1
    ComboUnlocks = unlock_val == 2
    CatUnlocks = unlock_val == 3


    if Development:
        item_config["Progressive D-Dog Bond"] = {"progression_skip_balancing": 10}
        item_config["Progressive Quiet Bond"] = {"progression_skip_balancing": 10}
    # Platform modifications
    if SDiamonds:
        item_config["Progressive Combat Unit Platform"] = {"progression_skip_balancing": 4}
        item_config["Progressive Command Platform"] = {"progression_skip_balancing": 3}
        item_config["Progressive R&D Platform"] = {"progression_skip_balancing": 2}
        item_config["Progressive Base Development Platform"] = {"progression_skip_balancing": 4}
        item_config["Progressive Support Platform"] = {"progression_skip_balancing": 4}
        item_config["Progressive Intel Platform"] = {"progression_skip_balancing": 4}
        item_config["Progressive Medical Platform"] = {"progression_skip_balancing": 3}
    elif Blueprints:
        item_config["Progressive Command Platform"] = {"progression_skip_balancing": 3}

    # Animal modifications
    if Animals:
        if ProgUnlocks:
            item_config["Progressive BAIT BOTTLE (Throwing Weapon)"] = {"progression_skip_balancing": 3}
            item_config["Progressive CAPTURE CAGE (Placed Weapon)"] = {"progression_skip_balancing": 3}
        elif SplitUnlocks:
            item_config["BAIT BOTTLE (Grade 3) (Throwing Weapon)"] = {"progression_skip_balancing": 1}
            item_config["BAIT BOTTLE (Grade 4) (Throwing Weapon)"] = {"progression_skip_balancing": 1}
            item_config["BAIT BOTTLE (Grade 5) (Throwing Weapon)"] = {"progression_skip_balancing": 1}
            item_config["CAPTURE CAGE (Grade 2) (Placed Weapon)"] = {"progression_skip_balancing": 1}
            item_config["CAPTURE CAGE (Grade 3) (Placed Weapon)"] = {"progression_skip_balancing": 1}
            item_config["CAPTURE CAGE (Grade 4) (Placed Weapon)"] = {"progression_skip_balancing": 1}
        elif ComboUnlocks:
            item_config["BAIT BOTTLE (Throwing Weapon)"] = {"progression_skip_balancing": 1}
            item_config["CAPTURE CAGE (Placed Weapon)"] = {"progression_skip_balancing": 1}
    print("MGSV DEBUG: Setting Dynamic Item Classes")
    return item_config

# The item pool before starting items are processed, in case you want to see the raw item pool at that stage
def before_create_items_starting(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# The item pool after starting items are processed but before filler is added, in case you want to see the raw item pool at that stage
print("MGSV DEBUG: Locking Starting Items")
FORCED_UNIQUE_FILLS: Tuple[str, Sequence[str]] = [
    # category, list of locations
    (
        lambda opts: {"Music"} if opts.Include_Cassettes.value == True else None,
        [
            "Starting Cassettes: Scouting Barren Lands",
            "Starting Cassettes: Journey to Point C-5",
            "Starting Cassettes: Sands",
            "Starting Cassettes: Dreamt of an Eclipse",
            "Starting Cassettes: Afghanistan's a Big Place",
            "Starting Cassettes: MGO Trailer Music",
            "Starting Cassettes: Richard Wagner: 'Ride of the Valkyries' from The Valkyrie -ACT III- (excerpt)",
        ],
    ),
    (
      lambda opts : {"D-Horse Equipment", "Funny1"} if opts.Item_Unlock_Handling.value == 0 else  {"D-Horse Equipment", "Funny2"} if opts.Item_Unlock_Handling.value == 1 else {"D-Horse Equipment", "Funny3"} if opts.Item_Unlock_Handling.value == 2 else {"D-Horse Equipment"},
        [
            "Development - D-Horse Equipment - NORMAL (Grade 1)",
        ],
    ),
    (
        {"D-Dog Equipment"},
        [
            "Development - D-Dog Equipment - NAKED (Grade 1)",
        ],
    ),
    (
        {"Quiet's Uniforms"},
        [
            "Development - Quiet's equipment - NAKED (Grade 1)",
        ],
    ),
    (
        lambda opts : {"Quiet Guns", "Progressive Weapons"} if opts.Item_Unlock_Handling.value == 0 else {"Quiet Guns", "Split Weapons"} if opts.Item_Unlock_Handling.value == 1 else {"Quiet Guns", "Combined Weapons"} if opts.Item_Unlock_Handling.value == 2 else {"Quiet Guns"},
        [
            "Development - Quiet's equipment - WICKED BUTTERFLY (Grade 2)",
        ],
    ),
    (
        lambda opts : {"StartingDWalkies", "Progressive Weapons"} if opts.Item_Unlock_Handling.value == 0 else {"StartingDWalkies", "Split Weapons"} if opts.Item_Unlock_Handling.value == 1 else {"StartingDWalkies", "Combined Weapons"} if opts.Item_Unlock_Handling.value == 2 else {"StartingDWalkies"},
        [
            "Development - D-Walker Armament - D-WALKER (Grade 2)",
        ],
    ),
    (
        lambda opts : {"StartingDWalkieAmmo", "Funny1"} if opts.Item_Unlock_Handling.value == 0 else {"StartingDWalkieAmmo", "Funny1"} if opts.Item_Unlock_Handling.value == 1 else {"StartingDWalkieAmmo", "Combined Weapons"} if opts.Item_Unlock_Handling.value == 2 else {"StartingDWalkieAmmo"},
        [
            "Development - D-Walker Armament - AMMO RACK (Grade 2)",
        ],
    ),
    (
        lambda opts : {"StartingDWalkieLoader", "Funny1"} if opts.Item_Unlock_Handling.value == 0 else {"StartingDWalkieLoader", "Funny1"} if opts.Item_Unlock_Handling.value == 1 else {"StartingDWalkieLoader", "Combined Weapons"} if opts.Item_Unlock_Handling.value == 2 else {"StartingDWalkieLoader"},
        [
            "Development - D-Walker Armament - AUTOLOADER (Grade 2)",
        ],
    ),
    (
        lambda opts : {"D-Walker Heads", "Progressive Weapons"} if opts.Item_Unlock_Handling.value == 0 else {"D-Walker Heads", "Split Weapons"} if opts.Item_Unlock_Handling.value == 1 else {"D-Walker Heads", "Combined Weapons"} if opts.Item_Unlock_Handling.value == 2 else {"D-Walker Heads"},
        [
            "Development - D-Walker Armament - SUPPORT HEAD (Grade 2)",
        ],
    ),
    (
        {"D-Walker Arms"},
        [
            "Development - D-Walker Armament - TASK ARM (Grade 2)",
        ],
    ),
    (
        lambda opts : {"D-Walker Sub Weapon", "Progressive Weapons"} if opts.Item_Unlock_Handling.value == 0 else {"D-Walker Sub Weapon", "Split Weapons"} if opts.Item_Unlock_Handling.value == 1 else {"D-Walker Sub Weapon", "Combined Weapons"} if opts.Item_Unlock_Handling.value == 2 else {"D-Walker Sub Weapon"},
        [
            "Development - D-Walker Armament - DW S.PISTOL-CS (Grade 1)",
        ],
    ),
    (
        lambda opts : {"StartingHeli", "Progressive Weapons"} if opts.Item_Unlock_Handling.value == 0 else {"StartingHeli", "Split Weapons"} if opts.Item_Unlock_Handling.value == 1 else {"StartingHeli", "Combined Weapons"} if opts.Item_Unlock_Handling.value == 2 else {"StartingHeli"},
        [
            "Development - Support Helicopter Armament - UTH-66 BLACKFOOT (Grade 1)",
        ],
    ),
    (
        lambda opts : {"StartyINT", "StaticProgCombo"} if opts.Item_Unlock_Handling.value == 0 else {"StartyINT", "StaticProgCombo"} if opts.Item_Unlock_Handling.value == 1 else {"StartyINT", "Combined Weapons"} if opts.Item_Unlock_Handling.value == 2 else {"StartyINT"},
        [
            "Development - Tools - INT SCOPE (Grade 1)",
        ],
    ),
    (
        lambda opts : {"StartyDROID", "StaticProgCombo"} if opts.Item_Unlock_Handling.value == 0 else {"StartyDROID", "StaticProgCombo"} if opts.Item_Unlock_Handling.value == 1 else {"StartyDROID", "Combined Weapons"} if opts.Item_Unlock_Handling.value == 2 else {"StartyDROID"},
        [
            "Development - Tools - iDROID (Grade 1)",
        ],
    ),
    (
        lambda opts : {"Starting Arms", "Funny1"} if opts.Item_Unlock_Handling.value == 0 else  {"Starting Arms", "Funny2"} if opts.Item_Unlock_Handling.value == 1 else {"Starting Arms", "Funny3"} if opts.Item_Unlock_Handling.value == 2 else {"Starting Arms"},
        [
            "Development - Prosthetic Arm - BIONIC ARM (Grade 1)",
        ],
    ),
    (
      lambda opts : {"Uniforms - Uniforms", "Funny1"} if opts.Item_Unlock_Handling.value == 0 else  {"Uniforms - Uniforms", "Funny2"} if opts.Item_Unlock_Handling.value == 1 else {"Uniforms - Uniforms", "Funny3"} if opts.Item_Unlock_Handling.value == 2 else {"Uniforms - Uniforms"},
        [
            "Development - Uniform - OLIVE DRAB (Grade 1)",
        ],
    ),
]

def before_create_items_filler(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    items_to_remove = defaultdict(int)
    world.selected_forced_unique_fills = [None] * len(FORCED_UNIQUE_FILLS)

    item_categories = {name:set(item.get("category", [])) for name, item in world.item_name_to_item.items()}
    for i, (cats, locs) in enumerate(FORCED_UNIQUE_FILLS):
        if isinstance(cats, Callable):
            cats = cats(world.options)
        if cats is None or not cats:
            continue
        if isinstance(cats, str):
            cats = frozenset({cats})
        else:
            cats = frozenset(cats)
        if isinstance(locs, str):
            locs = [locs]
        possible_items = [name for name, categories in item_categories.items() if cats <= categories]
        assert len(possible_items) >= len(locs), f"there are enough unique items in the category \"{cats}\" to fill the locations {locs}"
        selected = world.selected_forced_unique_fills[i] = world.random.sample(possible_items, k=len(locs))
        world.selected_forced_unique_fills.append((selected, locs))
        for name in selected:
            items_to_remove[name] += 1

    def should_add(item) -> bool:
        nonlocal items_to_remove
        if items_to_remove[item.name] == 0:
            return True
        else:
            items_to_remove[item.name] -= 1
            return False

    return [item for item in item_pool if should_add(item)]

# The complete item pool prior to being set for generation is provided here, in case you want to make changes to it
def after_create_items(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# Called before rules for accessing regions and locations are created. Not clear why you'd want this, but it's here.
def before_set_rules(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after rules for accessing regions and locations are created, in case you want to see or modify that information.
def after_set_rules(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to modify the access rules for a given location

    def Example_Rule(state: CollectionState) -> bool:
        # Calculated rules take a CollectionState object and return a boolean
        # True if the player can access the location
        # CollectionState is defined in BaseClasses
        return True

    ## Common functions:
    # location = world.get_location(location_name, player)
    # location.access_rule = Example_Rule

    ## Combine rules:
    # old_rule = location.access_rule
    # location.access_rule = lambda state: old_rule(state) and Example_Rule(state)
    # OR
    # location.access_rule = lambda state: old_rule(state) or Example_Rule(state)

# The item name to create is provided before the item is created, in case you want to make changes to it
def before_create_item(item_name: str, world: World, multiworld: MultiWorld, player: int) -> str:
    return item_name

# The item that was created is provided after creation, in case you want to modify the item
def after_create_item(item: ManualItem, world: World, multiworld: MultiWorld, player: int) -> ManualItem:
    return item

# This method is run towards the end of pre-generation, before the place_item options have been handled and before AP generation occurs
def before_generate_basic(world: World, multiworld: MultiWorld, player: int) -> None:
    for items, (_, locs) in zip(world.selected_forced_unique_fills, FORCED_UNIQUE_FILLS):
        if items is None:
            continue
        if isinstance(locs, str):
            locs = [locs]
        for item, loc in zip(items, locs):
            multiworld.get_location(loc, player).place_locked_item(world.create_item(item))

# This method is run at the very end of pre-generation, once the place_item options have been handled and before AP generation occurs
def after_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

# This method is run every time an item is added to the state, can be used to modify the value of an item.
# IMPORTANT! Any changes made in this hook must be cancelled/undone in after_remove_item
def after_collect_item(world: World, state: CollectionState, Changed: bool, item: Item):
    # the following let you add to the Potato Item Value count
    # if item.name == "Cooked Potato":
    #     state.prog_items[item.player][format_state_prog_items_key(ProgItemsCat.VALUE, "Potato")] += 1
    pass

# This method is run every time an item is removed from the state, can be used to modify the value of an item.
# IMPORTANT! Any changes made in this hook must be first done in after_collect_item
def after_remove_item(world: World, state: CollectionState, Changed: bool, item: Item):
    # the following let you undo the addition to the Potato Item Value count
    # if item.name == "Cooked Potato":
    #     state.prog_items[item.player][format_state_prog_items_key(ProgItemsCat.VALUE, "Potato")] -= 1
    pass


# This is called before slot data is set and provides an empty dict ({}), in case you want to modify it before Manual does
def before_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called after slot data is set and provides the slot data at the time, in case you want to check and modify it after Manual is done with it
def after_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called right at the end, in case you want to write stuff to the spoiler log
def before_write_spoiler(world: World, multiworld: MultiWorld, spoiler_handle) -> None:
    pass

# This is called when you want to add information to the hint text
def before_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:

    ### Example way to use this hook:
    # if player not in hint_data:
    #     hint_data.update({player: {}})
    # for location in multiworld.get_locations(player):
    #     if not location.address:
    #         continue
    #
    #     use this section to calculate the hint string
    #
    #     hint_data[player][location.address] = hint_string

    pass

def after_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:
    pass

def hook_interpret_slot_data(world: World, player: int, slot_data: dict[str, Any]) -> dict[str, Any]:
    """
        Called when Universal Tracker wants to perform a fake generation
        Use this if you want to use or modify the slot_data for passed into re_gen_passthrough
    """
    return slot_data
