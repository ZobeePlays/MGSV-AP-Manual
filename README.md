Archipelago Manual randomizer for Metal Gear Solid V: The Phantom Pain

This Project is still a pretty heavy WIP, if you would like to contribute, DM me on Discord, submit a PR, or submit a response to my google form for logic/name updates:
https://forms.gle/YGfb3rXkiFW2fPEr9

----------------------------------------------------------------
# SETUP GUIDE:
You will need to use the SnakeBite Mod manager to install some mods used to make playing this manual more stream lined.  
The First are Infinite Heaven and IH Hook, very powerful modding tools that give access to lots of different things. Basically the Base modding framework.  

https://www.nexusmods.com/metalgearsolidvtpp/mods/106  
https://www.nexusmods.com/metalgearsolidvtpp/mods/45  
https://www.nexusmods.com/metalgearsolidvtpp/mods/1226  

Second are the mods that allow you to claim your unlocks given by Archipelago, These remove the requirements of the Dev Tree and Base Development to make them free, allowing you to pick them up at any time upon receiving items. These can be found in the releases of this Github. There are Two Versions of the Dev Tree mod depending on if you want Online exclusive items to show up in game or not. 

Go Through the Snake bite Setup and install all 4 (or more) mods.  

After all that is done, Back up your save file and replace it with the Custom Save provided. This save file is essentially an attempt at a Low% Run of the game, doing the bare minimum to set up a playable file for this manual. up to unlocking the final mission.  
One Specific caveat to know, is that the Fulton + Cargo 2 is researched in this file, as it is required to progress past mission 35.  
Players will have to remember this restriction for their fulton cargo unlocks.

Proceed with standard Archipelago generation setup and play to your hearts content!  

----------------------------------------------------------------
# Infinite Heaven hooks for Traps and Restrictions:  
(Note that most of these hooks only work when in the ACC)  
Important Items:  
Buddy Bond Menu -> Change Bond Points  
Player Restrictions Menu -> Disable fulton action -> Used to completely disable the ability for snake to fulton until the FULTON DEVICE item is found  
  
If developed unintentionally:  
Player Restrictions Menu -> Fulton levels menu -> Used to Set Fulton ammo Levels (and wormhole)  
Player Restrictions Menu -> Hand Abilities levels menu -> Used to Force Hand Upgrades to lower or higher ranks  
Player Restrictions Menu -> Item Level Menu -> To Force iDROID and INT Scope levels  
  
Qol:  
Support heli Menu -> Start Free Roam on Foot = Can be turned on to skip the long heli opening when landing into free roam, nice for Synced sessions  
Support heli Menu -> Start Missions on Foot = Can be turned on to skip the long heli opening when landing into a mission, nice for Synced sessions  
Progression Menu -> Resource Scale Menu -> Can Be used to increase resource gains so you don't have to worry about heavy item loadouts  

----------------------------------------------------------------
Traps:  
Demonism Trap:  
"Player Settings Menu -> Add Demonism Points"  
if you want to possibly get out of demonism I suggest "Hero Points Subtract Demon Points" on  

Stink Trap:  
It seems like the best way to achieve the effect of making snake stinky is to turn up the time scale very very high, there is no hook to set in IH to make him stinky on its own  
Time Scale Menu -> TSM world time scale (20)  

more detail on how enemy preparedness works can be found on the metal gear wiki here:  
https://metalgear.fandom.com/wiki/Revenge_System_(enemy_preparedness)  
all options can be found under Enemy Prep Menu -> Custom prep menu, after setting prep modes to Custom Prep  

----------------------------------------------------------------
Reset Enemy Prep:  
"Enemy Prep Menu -> Reset Enemy Preparedness Levels"  

----------------------------------------------------------------
Enemy Preparedness Trap (Fulton Response)  
LV0:  
Enemy Prep Menu -> Soldier Abilities -> FULTON_MIN (Low)  
LV1:  
Enemy Prep Menu -> Soldier Abilities -> FULTON_MIN (None)  
LV2:  
Enemy Prep Menu -> Soldier Abilities -> FULTON_MIN (High)  
LV3:  
Enemy Prep Menu -> Soldier Abilities -> FULTON_MIN (Special)  

----------------------------------------------------------------
Enemy Preparedness Trap (Headshot Response)  
Enemy Prep Menu -> Headgear Deployment -> HELMET_MIN  

LV0: 0%  
LV1: 10%  
LV2: 20%  
LV3: 30%  
LV5: 50%  
LV7: 70%  

----------------------------------------------------------------
Enemy Preparedness Trap (Covert Actions Response)  

LV0:  
Enemy Prep Menu -> Soldier Abilities -> STEALTH_MIN (Low)  
Enemy Prep Menu -> Soldier Abilities -> HOLDUP_MIN (Low)  
  
LV1:  
Enemy Prep Menu -> CP Deterrent Deployment -> CAMERA_MIN  
  
LV2:  
Enemy Prep Menu -> CP Deterrent Deployment -> DECOY_MIN  
  
LV3:  
Enemy Prep Menu -> CP Deterrent Deployment -> MINE_MIN  
Enemy Prep Menu -> Soldier Abilities -> STEALTH_MIN (High)  
  
LV4:  
Enemy Prep Menu -> CP Equip Strength Menu -> ACTIVE_DECOY_MIN  
Enemy Prep Menu -> CP Equip Strength Menu -> GUN_CAMERA_MIN  
Enemy Prep Menu -> Soldier Abilities -> HOLDUP_MIN (High)  
  
LV5:  
Enemy Prep Menu -> Soldier Abilities -> STEALTH_MIN (Special)  

----------------------------------------------------------------
Enemy Preparedness Trap (Combat Response)  

LV0:  
Enemy Prep Menu -> Soldier Abilities -> COMBAT_MIN (Low)  
  
LV1:  
Enemy Prep Menu -> Soldier Abilities -> COMBAT_MIN (None)  
Enemy Prep Menu -> Armor Deployment -> SOFT_ARMOR_MIN (25%)  
  
LV2:  
Enemy Prep Menu ->  
Enemy Prep Menu -> Armor Deployment -> SOFT_ARMOR_MIN (50%)  
Enemy Prep Menu -> Armor Deployment -> SHIELD_MIN (20%)  

LV3:
Enemy Prep Menu -> Soldier Abilities -> COMBAT_MIN (High)  
Enemy Prep Menu -> Armor Deployment -> SOFT_ARMOR_MIN (75%)  
Enemy Prep Menu -> Weapon Strength Menu -> STRONG_WEAPON_MIN (on)  
Enemy Prep Menu -> Vehicle reinforcement level min (SUPER_REINFORCE)  

LV4:
Enemy Prep Menu -> Armor Deployment -> SOFT_ARMOR_MIN (100%)  
Enemy Prep Menu -> Weapon Strength Menu -> STRONG_WEAPON_MIN (on)  
Enemy Prep Menu -> Soldier Abilities -> COMBAT_MIN (High)  

LV5:
Enemy Prep Menu -> Soldier Abilities -> COMBAT_MIN (SPECIAL)  
Enemy Prep Menu -> Vehicle reinforcement level min (BLACK_SUPER_REINFORCE)  

----------------------------------------------------------------
Enemy Preparedness Trap (Nighttime Response)

LV0:  
Enemy Prep Menu -> Weapon Deployment -> GUNLIGHT_MIN (0%)  
Enemy Prep Menu -> Headgear Deployment -> NVG_MIN (0%)  

LV1:  
Enemy Prep Menu -> Headgear Deployment -> NVG_MIN (25%)  
Enemy Prep Menu -> Weapon Deployment -> GUNLIGHT_MIN (75%)  

LV2:  
Enemy Prep Menu -> Headgear Deployment -> NVG_MIN (50%)  
Enemy Prep Menu -> Weapon Deployment -> GUNLIGHT_MIN (75%)  

LV3:  
Enemy Prep Menu -> Headgear Deployment -> NVG_MIN (74%)  
Enemy Prep Menu -> Weapon Deployment -> GUNLIGHT_MIN (75%)  

----------------------------------------------------------------
Enemy Preparedness Trap (Sniper Response)  

LV0:  
Enemy Prep Menu -> Weapon Deployment -> SNIPER_MIN (0%)  
  
LV1:  
Enemy Prep Menu -> Weapon Deployment -> SNIPER_MIN (20%)  

LV2:  
Enemy Prep Menu -> Weapon Deployment -> SNIPER_MIN (30%)  
Enemy Prep Menu -> Weapon Strength Menu -> STRONG_SNIPER_MIN (on)  

----------------------------------------------------------------
Enemy Preparedness Trap (Vehicle Response)  

LV0:  
Enemy Prep Menu -> Weapon Deployment -> MISSILE_MIN (0%)  

LV1:  
Enemy Prep Menu -> Weapon Deployment -> MISSILE_MIN (20%)  

LV2:  
Enemy Prep Menu -> Weapon Deployment -> MISSILE_MIN (20%)  
Enemy Prep Menu -> Weapon Strength Menu -> STRONG_MISSILE_MIN (on)  

LV3:  
Enemy Prep Menu -> Weapon Deployment -> MISSILE_MIN (20%)  
Enemy Prep Menu -> Weapon Strength Menu -> STRONG_MISSILE_MIN (on)  

----------------------------------------------------------------
Enemy Preparedness Trap (Tranquilizer Response)  
No Effect can be changed in IH, but there is a level to it check wiki for details  

----------------------------------------------------------------
Enemy Preparedness Trap (Smoke/Gas Response Response)  
Enemy Prep Menu -> Headgear Deployment -> GAS_MASK_MIN  

LV0: 0%  
LV1: 25%  
LV2: 50%  
LV3: 75%  
