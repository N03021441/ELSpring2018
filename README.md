![New Paltz banner](https://www.newpaltz.edu/media/identity/logos/newpaltzlogo.jpg)
## Spring 2018 Embedded Linux class.
***
This repository documents my class work and projects done for ***CPS342***.

1. **Personal Information:**

    Name: *Anthony DiNardi*

    Major: *Computer Science*

    ID: *[N03021441](https://github.com/N03021441)*
  
    Year: *Senior*

2. **Class Start Date:** Jan 22, 2018

3. **Class End Date:** May 8, 2018

![TartufoCam](https://photos.google.com/photo/AF1QipNrBLl1DeBQrm3LHRbjPvfMBmokY7Rqn1BQOvPM)

Project Participation

Anthony DiNardi: 50%

Minh Nguyen: 50%

Dean: 0%

This repository focuses on the servo side of the the IOT security camera using a raspberry pi. This includes setting up the hardware as well as the software side of the project reguarding the servos. All the code for the final project are in the folder titled "FINAL_Project"

Materials gathered to motorize the IOT security camera are 2 SG5010, PCA9685, and sevaeral jumper cables. First, connect the two servos to channel 0 and channel 1 of the servo driver. Next, solder a DC barrel connector to the power line of the servo driver. Once this is done, a standard DC power cable will be sufficient to power the servos. Next the driver was interfaced with the Pi. Connect the VCC to a 3.3v power supply on the raspberry pi and connect GND on the driver to GND on the raspberry pi. Then connect the SCLK of the driver to the SCL1 pin on the rapsberry pi, and also, hook up the SDA pin from the driver to the SDA1 pin on the rapberry pi. At this point the hardward side of the IOT security camera pertain to motorized movements are complete. For the software side of the servos, refer to the folder "code."

The camera livestream is from a respository that somebody else has published. The README and License for that respository are in the "code" folder in the "FINAL_Project" folder. That component of code works by taking a couple of pictures every second and streaming them to the template page. The mechanism for the servos movement works like this: the user clicks the up/down/left/right buttons on the web page to move the camera. When a button is clicked, a value for that direction is sent to the python file through a post request. Depending on the direction, the current position value of the servo is added to a set value "turnValue" and will be compared to the maximum or minimum value for that servo in order to make sure the servo does not exceed the max or min values.
