Miscellaneous items will be placed here

The key detail of the servo motors are its provided APIs. It is trivial yet important to know what the functin of the APIs are. With this in mind there are two main API's the driver libraries provide for us in this project. That is, pwm.set_pwm_freq, and pwm.set_pwm.

The pwm.set_pwm_freq takes one integer argument that will specifiy the frequence the PWM signal is pusle at. For this prject, this API is as an itialization set and is set once in the code and never set again.

pwm.set_pwm take three integer arguments. The first ranges from 0-15 and specifies which channel the driver will modulate. So if you desire a motor to move and it is connect to channel 0 on the driver then th first argument of the pwm.set_pwm API will be 0. The last two arguments of the driver sets the time a PWM pulse is set low and high respectively. The second to last argument specify how long the signal will be low and the last argument specifies how long the PWM wave will be high. Both these arguments takes and intger argument from 100 to 600.
