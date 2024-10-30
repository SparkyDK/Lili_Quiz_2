# check that N/S and W/E are not green at the same time

#set light state where there WON'T be accidents
no_accident = [[[0, 0, 1], [0]], [[1, 0, 0], [1]], [[0, 0, 1], [0]], [[1, 0, 0], [1]]]
#set light state where there WILL be accidents
accident = [[[0, 0, 1], [0]], [[1, 0, 0], [1]], [[1, 1, 0], [0]], [[0, 0, 1], [1]]]

def check_green_lights(light_setting) :
#DAK    if ((light_setting[0][0][0] or light_setting[2][0][0]) == 1) and ((light_setting[1][0][0] or light_setting[3][0][0]) == 1) :
#DAK You want to be doing boolean comparisons with objects that have True or False values, rather than mixing them up with 1's and 0's!
#DAK We know that boolean and integers are not the same type... so we should be careful ... wand careful with the brackets too!

#DAK It is OK to break up compound logic tests like this, I think, to improve readability!
    one_or_more_NS_green = light_setting[0][0][0]==1 or light_setting[2][0][0]==1    # either one or both of the green LEDs are on
    one_or_more_EW_green = light_setting[1][0][0]==1 or light_setting[3][0][0]==1    # either one or both of the green LEDs are on
    
    if (one_or_more_NS_green and one_or_more_EW_green):  # note that these variables are both booleans, which are True or False
        print ("Same thing as below, right?")
        
    # Your compound statement is the same, but seems harder to read  
    if ( (light_setting[0][0][0]==1 or light_setting[2][0][0]==1) and (light_setting[1][0][0]==1 or light_setting[3][0][0]==1) ) :
        print("Oh no!! A North/South green light and a East/West green light is on at the same time. This could cause and accident!")
    else :
        print("No problemo, a North/South and East/West green light aren't on at the same time. Circulation should be safe.")

check_green_lights(accident)
check_green_lights(no_accident)
