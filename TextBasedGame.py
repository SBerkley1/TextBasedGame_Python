# Stephen Berkley

def game_instructions():
    '''Prints out game instructions'''
    print('#' * 60)
    print('#                                                          #')
    print('#   The Walking Dead Themed text-game                      #')
    print('#   Movement: go South, go North, go East, go West         #')
    print('#   Movement(stairs): go Upstairs, go Downstairs           #')
    print('#   Commands: use [item_name], get [item_name]             #')
    print('#   Health system: use Bandages to increase health         #')
    print('#   Hot keys: exit (quit game), --help (see this menu)     #')
    print('#   To win, collect all 7 items and face the zombie        #')
    print('#                                                          #')
    print('#' * 60, '\n')

def intro_story():
    '''A little introduction story to be able to start with the key in our inventory'''
    print('It\'s been 7 months since the first zombie has appeared.')
    print('Unfortunately, this zombie virus has spread rapidly. You')
    print('are on your own with no supplies left. You have been walking')
    print('through the woods for days and you found an old wooden house.')
    print('As you approach the house you see something glistening in the')
    print('sunrays. It\'s a small Key. You put the Key in your pocket and')
    print('walk up the front porch stairs...')

def isAlive():
    '''Returns true if survivor's health is greater than 0'''
    return character['Survivor'] > 0

def isZombieAlive():
    '''Returns true if zombie's health equal to 0'''
    return character['Zombie'] == 0

def isValidDirection(key, direction):
    '''returns True if direction is valid from the room user is in'''
    return direction in rooms.get(key)

def isValidUse(key, item):
    '''Returns true if the item you're using is supposed to be used in currentRoom'''
    return rooms[key]['item']['use'] == item

def isValidItem(key, item):
    '''returns True if 'get' item is in the room'''
    return rooms[key]['item']['name'] == item

def move_to_new_room(key, direction):
    '''move to new room'''
    return rooms[key][direction]

inventory = ['Key']  # list of items in inventory
items_collected = []   # list of items that have been collected

def use_item(key, item):
    '''Checks if item is in inventory. Use item and remove from inventory.
    Set item in currentRoom to hidden = False'''
    for i in range(len(inventory)):
        if inventory[i] == item:
            inventory.pop(i)
            rooms[key]['item']['hidden'] = False
            print('The {} was used!'.format(item))
            break
    else:
        print('You do not seem to have a {}'.format(item)) # why can't I reach this else???


def get_item(key, item):
    '''get item and store in inventory and items_collected'''
    if item in items_collected:
        print('You\'ve already picked up the {}'.format(item))
        return
    if not rooms[key]['item']['hidden']:    #if hidden == False, get item and put in inventory
        inventory.append(item)
        items_collected.append(item)
        rooms[key]['item']['have'] = True
    else:
        print('It seems you need to use something first!')

def describe_room(key):
    '''Describe room. Description changes if used correct item in room'''
    if key == 'FrontPorch':
        return 'A wooden porch that is falling apart. I better hurry inside!'
    # ---FLOOR 1 ROOMS---
    elif key == 'Foyer':
        if rooms[key]['item']['hidden'] == True and rooms[key]['item']['have'] == False:       # when item is hidden,
            return 'It looks like a small lock is keeping that trunk in the corner closed.'    # and you don't have it
        elif rooms[key]['item']['have'] == True:                                               # when you have the item
            return 'The room is empty'
        else:
            return 'The trunk was unlocked! Inside the trunk you see a Flashlight.'            # when you use the item

    elif key == 'DiningRoom':
        if rooms[key]['item']['hidden'] == True and rooms[key]['item']['have'] == False:
            return 'This is unusual, someone has placed a glass piggy bank on the table.'
        elif rooms[key]['item']['have'] == True:
            return 'The room is empty'
        else:
            return 'The piggy bank smashed to bits. Among the pieces is a Screwdriver.'

    elif key == 'StairWell':  # Stairwell does not have a hidden item
        if rooms[key]['item']['have'] == True:
            return 'There\'s a staircase going up, other then that, the room is empty'
        else:
            return 'You see a Hammer on a small table by a staircase going up.'

    elif key == 'Kitchen':
        if rooms[key]['item']['hidden'] == True and rooms[key]['item']['have'] == False:    # when item is hidden,
            return 'That\'s odd, one of the drawers is screwed shut.'                       # and you don't have it
        elif rooms[key]['item']['have'] == True:                                            # when you have the item
            return 'The room is empty'
        else:
            return 'The only thing inside the drawer is a pair of Scissors.'                # when you use the item

    elif key == 'Bathroom':
        if rooms[key]['item']['hidden'] == True and rooms[key]['item']['have'] == False:
            return 'It\'s very dark in here. I can\'t see anything.'
        elif rooms[key]['item']['have'] == True:
            return 'The room is empty'
        else:
            return 'As you shine the Flashlight under the sink you see some Bandages.'
    # ---FLOOR 2 ROOMS---
    elif key == 'Loft':
        if rooms[key]['item']['hidden'] == True and rooms[key]['item']['have'] == False:
            return 'There\'s stairs and a wooden box nailed shut. I wonder if I can pry it open?'
        elif rooms[key]['item']['have'] == True:
            return 'Besides the stairs, the room is empty'
        else:
            return 'The wooden box easily opened, and there\'s an Axe inside.'

    elif key == 'Attic':
        if rooms[key]['item']['hidden'] == True and rooms[key]['item']['have'] == False:
            return 'There\'s a duffle bag with a broken zipper. Can I cut this open?'
        elif rooms[key]['item']['have'] == True:
            return 'The room is empty'
        else:
            return 'Out falls a Crowbar from the bag.'

    else:  # SupplyCloset, where the Zombie is located
        return 'The Zombie is chasing after you!'

def fight_zombie():
    '''If you don't have all the items you lose one health.
    If you didn't use the bandage, you die. If have all items the zombies dies'''
    if len(items_collected) < 7:    # if player doesn't have all the items
        if character['Survivor'] > 1:
            print('There\'s a zombie in this room! It scratches you! GET OUT OF THE ROOM FAST!')
            character['Survivor'] -= 1
        else:
            print('There\'s a zombie in this room! It bites you!')
            character['Survivor'] -= 1
    else:
        character['Zombie'] -= 1
        print('Groaning and with an open mouth, the zombie lunges at you. You bring the Axe down and...')
        print('You just won the game!!!')

def check_health(health):
    '''Used to display our health status'''
    if health == 0:
        return 'Undead'
    elif health == 1:
        return 'Critical'
    elif health ==2:
        return 'Stable'
    else:
        return 'Unknown'

def add_health():
    '''When player use Bandages'''
    for i in range(len(inventory)):     # if you have Bandages, you use it and get +1 health and remove Bandages
        if inventory[i] == 'Bandages':
            inventory.pop(i)
            character['Survivor'] += 1
            print('You\'ve used the Bandages. You\'re feeling better already.')
            break
    else:
        print('You don\'t have a Bandage')

# character dictionary to help control health aspect of game
character = {
    'Zombie': 0,
    'Survivor': 1
}

# room dictionary... handles directions and items in and between rooms
rooms = {
    # 'hidden' is True if you need to 'use' an item in the room.  once you 'get' an item, 'have' becomes True
    # Starting Room
   'FrontPorch' : { 'North': 'Foyer'
                  , 'item': {'use': 'None', 'name': 'None', 'hidden': False} },

   # FLOOR 1 ROOMS
   'Foyer' : { 'North': 'Kitchen', 'East': 'StairWell', 'West': 'DiningRoom', 'South': 'FrontPorch'
             , 'item': {'use': 'Key', 'name': 'Flashlight', 'hidden' : True, 'have': False} },

   'DiningRoom' : { 'East': 'Foyer'
                  , 'item': {'use': 'Hammer', 'name': 'Screwdriver', 'hidden': True, 'have': False } },

   'StairWell' : { 'West': 'Foyer', 'Upstairs': 'Loft'      # no hidden item, has stairs
                 , 'item': {'use': 'None', 'name': 'Hammer', 'hidden': False, 'have': False} },

   'Kitchen' : { 'South': 'Foyer', 'East': 'Bathroom'
               , 'item': {'use': 'Screwdriver', 'name': 'Scissors', 'hidden': True, 'have': False} },

   'Bathroom' : { 'West': 'Kitchen'
                , 'item': {'use': 'Flashlight', 'name': 'Bandages', 'hidden': True, 'have': False} },

   # FLOOR 2 ROOMS
   'Loft' : { 'North': 'Attic', 'West': 'SupplyCloset', 'Downstairs': 'StairWell'   # has stairs
            , 'item': {'use': 'Crowbar', 'name': 'Axe', 'hidden': True, 'have': False} },

   'Attic' : { 'South': 'Loft'
             ,  'item': {'use': 'Scissors', 'name': 'Crowbar', 'hidden': True, 'have': False} },

   'SupplyCloset' : { 'East': 'Loft' # Zombie!
                    ,  'item': {'use': 'Axe', 'name': 'Zombie', 'hidden': False, 'have': False} }
}




def main():
    #start the player on the FrontPorch
    currentRoom = 'FrontPorch'
    mainCharacter = 'Survivor'

    game_instructions()         #shows game instructions, also will be hotkey --help
    intro_story()               # small introduction story

    while isAlive() and isZombieAlive():
        # 'exit' will end the loop

        # dictionary used to describe the rooms as the game progresses.
        describe_rooms = {
            key: describe_room(key) for (key, value) in rooms.items()
        }
        # dictionary used to describe health status
        character_health = {
            key: check_health(value) for (key, value) in character.items()
        }

        print('_' * 60)
        print('Current Room: {}\n'
              '{}\n'.format(currentRoom, describe_rooms[currentRoom]))

        print('Inventory:', inventory)

        num_items = len(items_collected)
        print('{} / 7 collected  [Health: {}]'.format(num_items, character_health[mainCharacter]))

        user_input = input('Enter your move: ').split()

        #if one word, check if it's '--help' or 'exit', otherwise error
        if len(user_input) == 1:
            if user_input[0] == '--help':
                game_instructions()
            elif user_input[0] == 'exit':
                break
            else:
                print('***{} is an invalid command!***'.format(user_input[0]))

        #if two words, check that keywords are correct and performs the command
        elif len(user_input) == 2:
            # go [direction]
            if user_input[0] == 'go':
                if isValidDirection(currentRoom, user_input[1]):
                    currentRoom = move_to_new_room(currentRoom, user_input[1])
                    if currentRoom == 'SupplyCloset':
                        fight_zombie()
                else:
                    print('***{} is an invalid direction from the {}! '
                          'Please try again.***'.format(user_input[1], currentRoom))

            # use [item_name]
            elif user_input[0] == 'use':
                if user_input[1] == 'Bandages':
                    add_health()
                elif isValidUse(currentRoom, user_input[1]):
                    use_item(currentRoom, user_input[1])
                else:
                    print('***You cannot use the {} in the {}***'.format(user_input[1], currentRoom))

            # get [item_name]
            elif user_input[0] == 'get':
                if isValidItem(currentRoom, user_input[1]):
                    get_item(currentRoom, user_input[1])
            else:
                print('***{} is an invalid command!***'.format(user_input[0]))

        #error user inputs more than 2 words
        else:
            print('***Error! Too many words. Max of two words allowed***')

    print('Game Over!!!!!')

if __name__ == "__main__":
    main()

