#count amount of red lights off

#set light state
lights = [[[0, 0, 1], [0]], [[1, 0, 0], [1]], [[1, 1, 0], [0]], [[0, 0, 1], [1]]]

#set empty list to count off red LED lights
off_red_lights = 0

for direction in lights :
    RGB_lights = direction[0] #check only g,y,r light lists
    if RGB_lights[2] == 0 : #check the red light position
        off_red_lights +=1 #update count
        print("+1 off red LED")
    else :
        print("This red LED is on") # Or is not a 0... i.e. could be "blinkysplat" too ... we like error checking and handling!

print(f"Amount of Red LEDs that are off : {off_red_lights}")
