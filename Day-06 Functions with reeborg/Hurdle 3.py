def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def wall_in_both_side():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

while not at_goal():
    if wall_in_front():
        wall_in_both_side()
    else:
        move()



################################################################
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
################################################################
