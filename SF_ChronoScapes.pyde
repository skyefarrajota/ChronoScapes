#Hello, welcome to ChronoScapes!
#The commentary will contextualise the code below it :)


#Setting up the canvas size
width, height = 800, 600

#Creating the setup; canvas size, white background colour, smooth edges
def setup():
    size(width, height) 
    background (255)
    smooth()
  
#Creating a loop      
def draw():
    global current_hour

    #Creating a white background for each frame of the animation
    background(255)

    #Drawing the building at a fixed position
    building_x, building_y = width/2, height/2
    building_width, building_height = 100,200
    #Setting the colour of the building
    fill(150)
    noStroke()
    rect(building_x - building_width/2, building_y - building_height, building_width, building_height) 
    
    #Setting the current time data for the hour (24 hour time)
    current_hour = hour()
    
    #Mapping the current hour to an angle range, simulating the morning to evening light passages
    #0 degrees (midnight) does not cast any shadow, 180 degrees (noon) casts the longest shadow
    #The angle is adjusted based on the hour
    shadow_angle = map(current_hour, 0, 24, 0, PI)
    
    #Calculating the properties of the shadows; length varies by time
    shadow_length = map(sin(shadow_angle), 0, 1, 20, 150)
    shadow_offset_x = shadow_length * cos(shadow_angle)
    shadow_offset_y = shadow_length * sin(shadow_angle)
    
    #Drawing the shadow; setting the colour and making semi-transparent
    fill(100,100)
    quad(
        building_x - building_width / 2, building_y, 
        building_x + building_width / 2, building_y, 
        building_x + building_width / 2 + shadow_offset_x, building_y + shadow_offset_y, 
        building_x - building_width / 2 + shadow_offset_x, building_y + shadow_offset_y 
    )
    
    #Displaying time on the screen
    fill(0)
    textSize(16)
    text("Hour: " + str(current_hour), 10, 20)
    
    
    
