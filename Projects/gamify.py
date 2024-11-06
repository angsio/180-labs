def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''
    
    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration
    
    global last_finished
    global bored_with_stars
    global cur_star
    global star_times
    global health_chain
    global tired
    
    cur_hedons = 0
    cur_health = 0
    health_chain = 0
    
    cur_star = None
    star_times = []
    
    bored_with_stars = False
    
    last_activity = None
    last_activity_duration = 0
    
    cur_time = 0
    
    last_finished = -1000

    tired = False
    

def star_can_be_taken(activity):
    pass
    
def perform_activity(activity, duration):
    global cur_hedons
    global cur_health
    global tired
    global cur_star
    global cur_time
    global health_chain

    # FIX TIREDNESS
    
    # stars always apply
    if activity == cur_star and not bored_with_stars:
        if duration <= 10:
            cur_hedons += 3*duration
        else:
            cur_hedons += 30

    # tired check
    if tired and activity != "resting":
        cur_hedons += -2*duration

    if activity == "running":
        # for hedons
        if not tired:
            if duration <= 10:
                cur_hedons += 2*duration
            else:
                cur_hedons += 20 - 2*(duration - 10)
        
        # for health
        # health_chain = 20, duration = 170
        # 160*3 + 10*1
        if duration + health_chain <= 180:
            cur_health += duration*3
        else:
            cur_health += (180 - health_chain)*3 + (health_chain + duration - 180)

        tired = True
        health_chain += duration

    elif activity == "textbooks":
        cur_health += 2*duration

        # for hedons
        if not tired:
            if duration <= 20:
                cur_hedons += duration
            else:
                cur_hedons += 10 - (duration - 20)
        health_chain = 0

    elif activity == "resting":
        if duration >= 120:
            tired = False
        health_chain = 0
        
    cur_star = None
    cur_time += duration
    

def get_cur_hedons():
    global cur_hedons
    return cur_hedons
    
def get_cur_health():
    global cur_health
    return cur_health
    
def offer_star(activity):
    global cur_star
    global cur_time
    global star_times
    global bored_with_stars
    cur_star = activity
    star_times.append(cur_time)
    if len(star_times) >= 3:
        bored_with_stars = (star_times[-1] - star_times[-3] < 120)
        print(star_times)
        print(bored_with_stars)
    
def most_fun_activity_minute():
    global tired
    global cur_star
    global bored_with_stars
        
    if bored_with_stars:
        return "resting" if tired else "running"
    else:
        if cur_star in ("running", "textbooks"):
            return cur_star
        else:
            return "resting" if tired else "running"


        
    
################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass
    
def get_effective_minutes_left_health(activity):
    pass    

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    pass
            

def estimate_health_delta(activity, duration):
    pass
        
################################################################################
        
if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)    
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2           		
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)    
    offer_star("running")              
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)  
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10
