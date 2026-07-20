import requests                                          #to get the pictures from the phone's server
import pygame                                            #to recieve inputs from the controller
import time                                              #to determine which pictures to save


#General variables
UpperThreshold = 25                                      #in seconds
LowerThreshold = 0.8
IPAddress = input('Input your phone\'s IP address:\n')   #IP address needed to access stream via website url
FileName = input('Enter the prefix for your files:\n')   #will be used for each jpg file saved


#Procedure to take and save photo
def takePhoto(IPAddress):
    return requests.get(f'http://{IPAddress}/photo.jpg')

def savePhoto(Response, TimeHeld, FileName, PhotoCount):
    with open(f"{FileName}{PhotoCount}.jpg", "wb") as f:
        f.write(Response.content)
    print(f'{FileName}{PhotoCount}.jpg saved successfully')


#Initialising controller
Connected = False
while not Connected:
    pygame.init()
    if pygame.joystick.get_count() != 1:
        UserConfirm = input(('Please press enter once you have connected one controller.'))
    else:
        Connected = True
        Controller = pygame.joystick.Joystick(0)
        print(f'You have connected a {Controller.get_name()}')


#Main loop during printing
Timelapsing = True
PhotoCount = 0
PrevPress = False #previous get_button() result for the triangle button
print('\nTimelapse started, press triangle to take a photo or the PS button to exit.')
while Timelapsing:
    pygame.event.get() #refreshing information about the joystick actions

    #Checking the state of the PS button for exiting
    if Controller.get_button(5): 
        print('Exiting timelapse')
        Timelapsing = False

    #Checking the state of the triangle button for taking a photo
    elif Controller.get_button(3) and not PrevPress: #Triangle button
        StartTime = time.time()
        print('\nTriangle pressed')
        Response = takePhoto(IPAddress)

    elif not Controller.get_button(3) and PrevPress:
        TimeHeld = time.time() - StartTime
        if TimeHeld < UpperThreshold and TimeHeld > LowerThreshold:
            savePhoto(Response, TimeHeld, FileName, PhotoCount)
            PhotoCount += 1
        else:
            print('Triangle button held for an invalid amount of time, and the photo wasn\'t saved')
        print(TimeHeld)

    PrevPress = Controller.get_button(3)