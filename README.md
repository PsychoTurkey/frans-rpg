# frans-rpg
Command line like rpg for Telegram.

Things that really should be changed:
- Make player ids telegram ids instead of their names (and change everything to print both ids and names) (especially for /do command)
- Make the random NPC choice bigger when a location's level >= 95
- Marriage
- Generate and send image of the map
- Different group chats handling (unknown people, still be able to attack players in an empty group)
- hp = maxHp when leveling up
- Player stats privacy?
- Does use() of healingItem class work; reading "name" after deletion?
- locationInfo should work for individual locations (referable to by coordinates)
- listPlayers should give player levels as well
- fillStore() reaally shoudl be changed (how to access it, amount of items per player, more healing items)