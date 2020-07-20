# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:10:09 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create() 
x,y,z=mc.player.getTilePos()
while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("你現在在x"+str(x)+
                  "Y:"+str(y)+"Z:"+str(z))
                         
                              