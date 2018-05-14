##Programs and code will be placed in this folder

To run the camera stream, execute the command:  *python app.py*
from the directory titled "code"

You will be able to view the interface and control the camera by using the link: your-pi-IP:5000
where "your-pi-IP" is....well....your Pi's IP address.

The first step to is to interface the pi with the driver. To do this we must configure the I2C protocol on the raspberry pi. From the pi irst run the following commands,

sudo apt-get install python-smbus
sudo apt-get install i2c-tools

Becasue this project runs on the lastest revision of the raspberry pi, we were able to run the command,

sudo i2cdetect -y 1

As a result, a table will appear and you should be able to see the numbers 40 and 70 in the first column of the table. This verifies that the driver is successfully registered with the pi and we are now ready to begin transmitting data through the I2C bus.

Now the motor driver libraries must be imported to the directory that you wish to write your motor driver source code. For this run the following commends,

sudo apt-get install git build-essential python-dev
cd ~
git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git
cd Adafruit_Python_PCA9685
sudo python setup.py install 
\# if you have python3 installed:
sudo python3 setup.py install 

To see if the everything was installed and configure correctly we can run the command,

cd examples
sudo python simpletest.py

If all is good, the example source code will oscillate a servo back and forth when connected to channel 0 in the servo driver.
From here, we build on the this source code driver in the github repository https://github.com/N03021441/ELSpring2018
