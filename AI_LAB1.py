def get_next_states(state):
    x,y = state
    can_pour_x = min(x, 3-y)
    can_pour_y = min(y, 4-x)
    
    next_states = [
        (4,y),
        (x,3),
        (0,y),
        (x,0),
        (x- can_pour_x, y+ can_pour_x),
        (x + can_pour_y, y- can_pour_y)]
    return next_states

start = (0,0)
seen = {start}
frontier = [start]
level = 0
max_levels = 8

while frontier and level < max_levels:
    new_states_this_level = []
    
    for state in frontier:
        for next_state in get_next_states(state):
            if next_state in seen:
                continue
            
            seen.add(next_state)
            new_states_this_level.append(next_state)
            
            if next_state[0] ==  2 or next_state[1] == 2:
                print("   *** GOAL REACHED:", next_state, "at level", level + 1, "***")
            
    level+=1
    frontier = new_states_this_level
print("Total states found:", len(seen))