# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 20:35:13 2017

@author: Hasee
"""
import matplotlib.pyplot as plt
import math
g=9.8
l=1
Ω_D=2.0
F_D=0.2
θ_0=0.5
q=0.1
def Projectile(θ_0,F_D,t_0):
    list_θ=[0,]
    list_ω=[0,]
    list_t=[0,]
    t=0
    delt_t=0.005
    θ=θ_0
    ω=0
    while t<t_0 :  
        θ=θ+ω*delt_t
        ω=ω-g*(math.sin(θ))/l-q*ω+F_D*math.sin(Ω_D*t)
        t=t+delt_t
        list_θ.append(θ)
        list_ω.append(ω)
        list_t.append(t)
    return (list_θ,list_ω,list_t)
plt.figure(figsize=(10,5))
j=1
while j<2:
    x_j,ω,y_j=Projectile(0.2,0.2,5)
    plt.plot(x_j,ω,label="$knunckle ball  trajectory$",marker='.')
    j=j+1
    
plt.figure(figsize=(10,5))
plt.xlabel("X/m")
plt.ylabel("Y/m")
plt.title("knunckle ball trajectory")
plt.ylim(-6,6)
plt.xlim(0,20)
plt.legend()
plt.show()    
