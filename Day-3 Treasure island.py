#!/usr/bin/env python
# coding: utf-8

# # Treasure island

# In[1]:


game_over = 'Game over.'


# In[3]:


Right = 'You head confidently in the choosen direction, but suddenly, the ground gives way beneath you. You fall into a deep, dark hole, tumbling down into the abyss. Your adventure comes to a swift and unexpected end.' #game over


# In[4]:


Swim = 'You choose to swim, but a massive crocodile attacks!' #game over


# In[5]:


Red = "You opened the red door and were greeted by a burst of flames. You've been burned!" #game over


# In[6]:


Blue = "You opened the blue door and a group of fierce beasts lunged at you. You've been eaten by beasts." #game over


# In[7]:


Yellow = 'Hooraay! You found the treasure box filled with precious gems. Congratulations, you win!' #win


# In[18]:


print('Welcome to Tresure Island.\nYour mission is to find the tresure.')
start = input('Type "start" to start your mission. ➡️').strip().capitalize()

if start == 'Start':
    path = input('\nYou are at a cross road. Where do you want to go? Type "Left" or "Right" ➡️ ').strip().capitalize()
    if path == 'Left':
        at_lake = input('\nyou came to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat. Type "swim" to swim across the lake ➡️ ').strip().capitalize()
        if at_lake == 'Wait':
            choose_door = input('\nYou arrived at the island unharmed. \nThere is a house with 3 doors. One "red", one "blue", one "yellow". \nWhich door you want to enter? ➡️ ').strip().capitalize()
            if choose_door == 'Yellow':
                print(f"\n{Yellow}")
                unbox = input('\nInterested to unbox the treasure box or do you want to open it later? \nType "open" or "Later" ➡️ ').strip().capitalize()
                if unbox == 'Open':
                    print('💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎')
                elif unbox == 'Later':
                    print('\nAlright! but carefull. It can be robbed.')
                else:
                    print('\nYou lost the treasure box. 📦')
            elif choose_door == 'Red':
                print(f"\n{Red} {game_over} 🔥")
            elif choose_door == 'Blue':
                print(f"\n{Blue} {game_over} 🐻")
            else:
                print(game_over + '🔥🔥🔥')
        elif at_lake == 'Swim':
            print(f"\n{Swim} {game_over} 🐊")
        else:
            print(game_over + '🔥🔥🔥')
    elif path == 'Right':
        print(f'\n{Right} {game_over} 🤕')
    else:
        print(f'\n😵‍💫 Wrong direction. {game_over}')
else:
    print('\nSorry to see you leave. 💎')


# ### Day 3 complete
