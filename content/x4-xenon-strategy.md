Title: X4 Foundations: Clearing Xenon Sectors Easily
Date: 2023-12-07 22:22
Modified: 2023-12-07 22:22
Category: Games
Tags: x4,strategy
Slug: x4-xenon-strategy
Author: delucks
Summary: My method and some general tips

## Fighting Xenon Shisp

Throughout *ahem* some time in X4 Foundations, I've had a huge variety of success in fighting the Xenon. When I first came to X4 from X3 last year, I mostly avoided
direct confrontation with the Xenon, preferring to try to reinforce NPC fleets in key points. This kind of response only lasts so long in **your** space sandbox where
you want to change anything at will; so I started fighting them. At first I suffered heavy losses, especially in sector, against any Xenon capital fleet or sufficiently
big cloud of P. It took a while before I learned the trick to fighting the Xenon's ships: overwhelming them with numbers. If the Xenon bring three capitals to the fight,
you should have at least ten to counter them. If they bring a few dozen M and N, you should have at least 50 high-survivability fighters. The effect is especially 
important in-sector, where combat with Xenon capitals results in higher losses than out-of-sector combat. My typical fleet size is overprovisioned to account for this;
the more ships you have, the better their collective chances of survival and the less micromanaging you need to do in equipping replacement fleets.

If you're just starting out and don't have the resources to field a fleet, you can still handle Xenon capitals one-on-one in a M-sized ship (usually a corvette) if you have
the right equipment. Prioritize high average damage output guns on a maneuverable ship like a Katana, Dragon, or Kuraokami- bonus points if your chosen gun ignores shields.
If you have access to Split weapons, the Thermal Disintegrators are great for this purpose. You want to be able to swoop in behind the capital ship where both K and I have
a (relatively) blind spot. Both ships have a battery of M-sized turrets protecting their aft but no L-sized turrets pointing directly backward. If you can get in close
and take out those guns, you have bought yourself a safe place to recharge your shields while steadily taking the rest of the machine apart. Start with the engines so
the ship doesn't move far, then move on to taking out the graviton turrets and shield generators. If you're in a patrolled sector, it's likely the NPCs will join in to
help.

While you can handle a single capital, a group of capitals is a harder challenge in an M-class ship. For that purpose I'd recommend a Rattlesnake or Syn destroyer; both
have enough damage output to take out a Xenon capital before you get too crispy.

### Fleet Composition

Here's an example of a single anti-Xenon fleet:

```
Fleet Name: 45 Ulexite
Fleet Leader: Tokyo
Support Ship: Honshu (with four Katana escorts set to "Defend Commander")
Battleships (10): Syn with L Bolt and M Bolt turrets set to "Bombard for Commander"
Fighters (50): Kalis with maximum shielding and Mk2 Proton Barrage set to "Attack with Commander"
```

This is sufficient to handle any group of Xenon warships that doesn't exceed 3 capital ships OOS. For gate defense, I'll usually put two of these on "Defend Position"
around the gate; I have very occasional destroyer losses using this deployment.

In my current >10d playtime save, I have somewhere around 50 of similar fleets spread out throughout the galaxy. To keep them accounted for, I number each fleet
(in this example, 45) and give it a unique mineral name (Ulexite). This way any given task can get mapped back to a set of mineral nicknames for which ships are
involved.

## Fighting Xenon Stations

This is the really difficult part. Typically taking on Xenon stations is a miserable time; in-sector you really only have the option of fighting a station by yourself with a destroyer or battleship but this can get really tedious and time-consuming. Out of sector you can use your fleets more effectively, but losses are usually so high that it's not worth doing. I've got a pretty decent strategy for *in-sector* fighting *with your fleets*, but it's very much a mid-to-late game strategy. You'll need the ability to build at least:

- Two well specced anti-Xenon fleets (like the above example) with their destroyers set to "Bombard for Commander"
- An Asgard for your personal use
- Fifty specialized commonwealth fighters

For the specialized fighters, you need to design a ship for taking on surface elements only. I like to use the Shih for its high shielding and four hardpoints. On those four hardpoints, I have two Mk2 Burst Ray and two Mk2 Blast Mortar; the first two for the higher damage to surface components and the second two for their AOE effect. Make sure this ship is well shielded and has a good engine; many will die otherwise. Make somewhere around 50 of these ships (again, much easier with a player-owned wharf).

Bring your Asgard, your fleets, and anti-component fighters to the target Xenon sector. Use travel mode on the Asgard to get within 12km to your target station while ordering the two fleets to "fly and wait" just over 40km away from the station. With your Asgard, take out the station's dock module (the bulbous dark-grey symmetrical one) and any convenient defense modules.

Now for the fun part! Select all 50 of your anti-component fighters and order them to Attack only the turrets of the station (it's in the drop-down of the last option). They'll fly around the station taking out the graviton turrets until there are none left, then they'll start attacking the station itself. You can see that this is the case by using the "Next Surface Component" key to check what components still exist on the target station. When all the turrets are gone, select all 50 again and "remove all orders and assignments", then order them a safe distance away from the station.

Now you have a Xenon station with no practical capital defense! Order one of your fleet leaders to "Coordinate Attack" on the station and let them do their job. I
usually teleport away from the sector just before the station explodes to prevent fighter losses but you can be in sector for that part too.

## Example of Clearing a Xenon Sector

Let's go through an example of using this method. I'm trying to clear Family Tkr of its current robotic occupants; I need a route to ship all the products I'm making in Tharka's Ravine south! I've got the following armada:

```
Flagship Fleet: Raptor + 20 Syn (bolt, bombard) + 120 Takoba (intercept)
Anti-Fighter Specialist Fleet: Tokyo + 10 Syn (beam, intercept) + 50 Takoba (intercept)
Anti-Xenon Fleets (18): Mix of Osaka and Syn, fighters are all Kalis
```

All told this is absolute overkill. You could take the sector with a tenth of the ships but hey, smoke 'em if you've got 'em.

We're up against two stations, one defense platform and one solar power plant. Anyone who's tried to take on a Xenon SPP knows how difficult it is to kill compared to most other stations in the game.
