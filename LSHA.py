import math
from math import exp
from math import sin,cos
#Halbach array parameters

pi = 3.1415
M = 5                       #No. of magnets per lambda(1/m)
B = 1.35                   #Magnetic field of one magnet(T)
t = 5*10**-3                 #thickness of magnet(m)
w = 5*10**-3                 #width of magnet(m)
A = 250 *10**-6              #Area under halbach array
L = 7.5*10**-8              #Inductance of inductrack
Lambda = 25*10**-3           #Wavelength
dc = 3*10**-3                #Spacing of inductor(mm)
K = (2*pi/(25*10**-3))        #Wave number (2*pi/lambda)
R = 2*10**-4                 #Resistance of inductrack

Bo = (B*(1-exp(-(4*pi*t)/Lambda))*sin(pi/M))/(pi/M)  #Max Magnetic field
print(Bo)
#Mechanical system parameters
theta1 = pi/6
theta0 = pi/2
theta2 = 5*pi/6
u = 0.3                    #coefficient of friction
K1 =10                     #Large spring constant
Ko =5                      #Small spring constant
h = 2*10^-3                #permissible spring deflection

y = 0.002
v = 5

fbx = (((((Bo)**2)*w*A)/(2*K*L*dc))*((R/(K*v*L))/(1+(R/(K*v*L))**2))*exp(-2*K*y))
fby = (Bo**2*w*A)/(2*K*L)*(1/(1+(R/(K*v*L))**2))*exp(-2*K*y)
f = (14.88*exp(-160*pi*y))/(1+(113/(v**2)))

print(fby)
print(f)
