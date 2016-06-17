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
- Find a home for the creation of the storeObject
- !!! ((storeObject in creatures[]? What if something loops trough it and cannot find certain variables? (eg listPlayers())) Righty: removed it from the creatures list. But why was it added there once?) item.destroy() will remove it's id from the inventory it's in, and tries to find that inventory within the creatures list. Either move storeObj back to creatures list, or make an inventories list. What to do?
- Move-between-inventories function for items.
- Buying items!
- Market - players can try to sell their items for a self-chosen price. They cannot use the item when its up fore sale! Limit it so that the market won't be overflown with items nobody wants (eg max number of items one person can try to sell at a time.)
- Send a message from fillStore()
- Loan function: get an amount of money (to your inventory gold), but all money you store in bank will be taken untill the loan has been repaid. ()
- viewStore() names everything a weapon and gives level while it shouldn't for healing items/