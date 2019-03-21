# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 13:25:37 2018

@author: Kenneth
"""

"""
Kenneth Zia
Phase Speed Plotter and Total Power Integration
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob as glob
from natsort import natsorted
from decimal import Decimal

plt.rcParams.update({'font.size': 15})



path='C:\Users\Kenneth\Desktop\MCM_AMTM_2017\Jun17-18\changedzpt\BandOH*_TOTAL'
files=glob.glob(path+'.csv')
files=natsorted(files)

path2='C:\Users\Kenneth\Desktop\MCM_AMTM_2017\Jun18-19\BandOH1hr\BandOH*_TOTAL'
files2=glob.glob(path2+'.csv')
files2=natsorted(files2)

t2=np.zeros(np.size(files))
x2=np.zeros(np.size(files))
data1=np.zeros((300,301,np.size(files)))
piece=np.zeros((12,np.size(files)))
quad=np.zeros((4,np.size(files)))


#t2=np.zeros(np.size(files))
#x2=np.zeros(np.size(files))
#data1=np.zeros((300,301,np.size(files)))

data=np.zeros((300,301))
data3=np.zeros((300,301))
data=np.zeros((300,301))
piece=np.zeros((12,np.size(files)))
quad=np.zeros((4,np.size(files)))



for i in range(0,np.size(files)):

    data2 = pd.read_csv(files[i])
    data1[:,:,i]=data2.values
#for i in range(0,np.size(files2)):
#    j=i+np.size(files)
#    data2 = pd.read_csv(files2[i])
#    data1[:,:,j]=data2.values

x=np.arange(-len(data)/2,len(data)/2+1,1)
y=np.arange(-len(data)/2,len(data)/2+1,1)
x0=np.zeros(len(data)+1)
y0=np.zeros(len(data)+1)    

for k in range(0,np.size(files)): 
    for i in range(0,300):
        for ii in range(0,301):
        
            data[i,ii]= data1[i,ii,k]
    
    plt.figure(figsize=(8,8))
    t=np.sum(10**data[:,:])
    t2[k]=t
    x2[k]=k
    ind = np.unravel_index(np.argmax(data, axis=None), data.shape)
    xmax=float(int(ind[1])-150)
    ymax=float(int(ind[0])-150)
    psmax=np.sqrt(xmax**2+ymax**2)
    theta=np.arctan2(ymax,xmax)*180.0/(np.pi)
    
    circle1 = plt.Circle((0, 0), 50, color='k', fill=False)
    circle2 = plt.Circle((0, 0), 100, color='k', fill=False)
    circle3 = plt.Circle((0, 0), 150, color='k', fill=False)
    
    circle1 = plt.Circle((0, 0), 50, color='k', fill=False)
    circle2 = plt.Circle((0, 0), 100, color='k', fill=False)
    circle3 = plt.Circle((0, 0), 150, color='k', fill=False)
    
    circle11 = plt.Circle((0, 0), 10,linestyle=':', color='k', fill=False)
    circle21 = plt.Circle((0, 0), 20,linestyle=':', color='k', fill=False)
    circle31 = plt.Circle((0, 0), 30,linestyle=':', color='k', fill=False)
    circle41 = plt.Circle((0, 0), 40,linestyle=':', color='k', fill=False)
    
    circle12 = plt.Circle((0, 0), 110,linestyle=':', color='k', fill=False)
    circle22 = plt.Circle((0, 0), 120,linestyle=':', color='k', fill=False)
    circle32 = plt.Circle((0, 0), 130,linestyle=':', color='k', fill=False)
    circle42 = plt.Circle((0, 0), 140,linestyle=':', color='k', fill=False)
    
    circle13 = plt.Circle((0, 0), 60,linestyle=':', color='k', fill=False)
    circle23 = plt.Circle((0, 0), 70,linestyle=':', color='k', fill=False)
    circle33 = plt.Circle((0, 0), 80,linestyle=':', color='k', fill=False)
    circle43 = plt.Circle((0, 0), 90,linestyle=':', color='k', fill=False)
    
    
    plt.pcolormesh(x,y,data,cmap='jet',vmin=-11.5,vmax=-6.5)
    plt.plot()
    
    plt.title('AMTM TempOH Jun17-18 (1hr) Interval #'+np.str(k+1))
    
#    plt.xlabel('Phase Speed (W-E) [m/s]')
#    plt.ylabel('Phase Speed (S-N) [m/s]')
#    plt.colorbar(label='log$_{10}$(PSD) [m$^{2}$/s$^{2}$]')
    
#    plt.plot((0.0,xmax),(0.0,ymax))

    plt.plot(x0,y,color='k',lw='0.5')
    plt.plot(x,y0,color='k',lw='0.5')
    plt.gcf().gca().add_artist(circle1)
    plt.gcf().gca().add_artist(circle2)
    plt.gcf().gca().add_artist(circle3)
    plt.gcf().gca().add_artist(circle11)
    plt.gcf().gca().add_artist(circle21)
    plt.gcf().gca().add_artist(circle31)
    plt.gcf().gca().add_artist(circle41)
    plt.gcf().gca().add_artist(circle12)
    plt.gcf().gca().add_artist(circle22)
    plt.gcf().gca().add_artist(circle32)
    plt.gcf().gca().add_artist(circle42)
    plt.gcf().gca().add_artist(circle13)
    plt.gcf().gca().add_artist(circle23)
    plt.gcf().gca().add_artist(circle33)
    plt.gcf().gca().add_artist(circle43)
#    TP='Total Power'+"{:.2E}".format(Decimal(np.str(t)))
#    plt.text(-150,140,TP,color='white',fontsize=12)
#    plt.text(78,130,'Theta='+np.str(int(theta))+'[deg]',color='white',fontsize=12)
#    plt.text(78,140,'Max_Val='+np.str(int(psmax))+'[m/s]',color='white',fontsize=12)

    plt.show()
    plt.savefig('C:\Users\Kenneth\Desktop\FixedPlots\BandOH_#'+np.str(k)+'.jpeg')
  
  
  
    for i in range(0,300):
      for j in range (0,301):
        theta=np.arctan2(i-150,j-150)
        if theta>=0.0:
            if theta>5.0*np.pi/6.0 and theta<=np.pi:
                piece[5,k]=piece[5,k]+10**data[i,j]
            if theta<=5.0*np.pi/6.0 and theta>4.0*np.pi/6.0:
                piece[4,k]=piece[4,k]+10**data[i,j]
            if theta<=4.0*np.pi/6.0 and theta>np.pi/2.0:
                piece[3,k]=piece[3,k]+10**data[i,j]
            if theta>np.pi/3.0 and theta<=np.pi/2.0:
                piece[2,k]=piece[2,k]+10**data[i,j]
            if theta<=np.pi/3.0 and theta>np.pi/6.0:
                piece[1,k]=piece[1,k]+10**data[i,j]
            if theta<=np.pi/6.0 and theta>0.0:
                piece[0,k]=piece[0,k]+10**data[i,j]
        if theta<0.0:
            if abs(theta)>5.0*np.pi/6.0 and abs(theta)<=np.pi:
                piece[6,k]=piece[6,k]+10**data[i,j]
            if abs(theta)<=5.0*np.pi/6.0 and abs(theta)>4.0*np.pi/6.0:
                piece[7,k]=piece[7,k]+10**data[i,j]
            if abs(theta)<=4.0*np.pi/6.0 and abs(theta)>np.pi/2.0:
                piece[8,k]=piece[8,k]+10**data[i,j]
            if abs(theta)>np.pi/3.0 and abs(theta)<=np.pi/2.0:
                piece[9,k]=piece[9,k]+10**data[i,j]
            if abs(theta)<=np.pi/3.0 and abs(theta)>np.pi/6.0:
                piece[10,k]=piece[10,k]+10**data[i,j]
            if abs(theta)<=np.pi/6.0 and abs(theta)>0.0:
                piece[11,k]=piece[11,k]+10**data[i,j]
        if theta>=0.0:
            if theta>np.pi/2:
                quad[1,k]=quad[1,k]+10**data[i,j]
            else:
                quad[0,k]=quad[0,k]+10**data[i,j]
        if theta<0.0:
            if abs(theta)>=np.pi/2:
                quad[2,k]=quad[2,k]+10**data[i,j]
            else:
                quad[3,k]=quad[3,k]+10**data[i,j]
      

#for k in range(0,np.size(files)):     
#    plt.figure(figsize=(8,8))
#    ax=plt.subplot(111,polar=True)
#    thetaax=np.pi/12.0+np.linspace(0.0,2*np.pi,12,endpoint=False)
#    radii=np.array(piece*10**5)
#    width=np.array(np.zeros(12))
#    bars=ax.bar(thetaax[:],radii[:,k],
#        edgecolor='k',
#        #label='x10^-5',
#        width=0.5)
#    ax.set_yticks(np.linspace(0,np.max(radii[:,:]),4))
#    ax.set_xticks(thetaax-np.pi/12.0)
##    plt.legend()
#    plt.grid(True)
#    #plt.title('AMTM TempOH (1hr) Interval #'+np.str(k+1))
#    
#    plt.show()
#    plt.savefig('C:\Users\Kenneth\Desktop\FixedPlots\BandOH_#'+np.str(k)+'.jpeg')

    

plt.figure(figsize=(10,10))
plt.title(' ')
plt.xlabel('Time (hrs)')
plt.ylabel('Total Power')
plt.semilogy(x2,t2, marker='x')
plt.savefig('C:\Users\Kenneth\Desktop\FixedPlots\BandOH_#'+np.str(k)+'.jpeg')
#ax1=plt.gca()
#ax2=ax1.twinx()
#ax2.semilogy(time,T/100.0,label='Intensity',color='r',linestyle='--')
#ax2.set_ylabel('Intensity')

plt.show()

plt.figure(figsize=(10,10))
plt.title('1-Hourly Change in Direction')
plt.xlabel('Time (hrs)')
plt.ylabel('Total Power')

leg=['NE','NW','SW','SE']
for k in range(0,4): 
    plt.plot(x2,quad[k,:],label=leg[k])
plt.legend()
plt.show()
plt.savefig('C:\Users\Kenneth\Desktop\FixedPlots\BandOH_#'+np.str(k)+'.jpeg')


for i in range(0,300):
    for ii in range(0,301):
        data3[i,ii]=np.log10(np.average(10**data1[i,ii,:]))


t=np.sum(10**data3[:,:])
ind = np.unravel_index(np.argmax(data3, axis=None), data.shape)
xmax=float(int(ind[1])-150)
ymax=float(int(ind[0])-150)
psmax=np.sqrt(xmax**2+ymax**2)
theta=np.arctan2(ymax,xmax)*180.0/(np.pi)
plt.savefig('C:\Users\Kenneth\Desktop\FixedPlots\BandOH_#'+np.str(k)+'.jpeg')

#
#
#
#plt.figure(figsize=(10,8))
#
#
#circle1 = plt.Circle((0, 0), 50, color='k', fill=False)
#circle2 = plt.Circle((0, 0), 100, color='k', fill=False)
#circle3 = plt.Circle((0, 0), 150, color='k', fill=False)
#
#circle1 = plt.Circle((0, 0), 50, color='k', fill=False)
#circle2 = plt.Circle((0, 0), 100, color='k', fill=False)
#circle3 = plt.Circle((0, 0), 150, color='k', fill=False)
#
#circle11 = plt.Circle((0, 0), 10,linestyle=':', color='k', fill=False)
#circle21 = plt.Circle((0, 0), 20,linestyle=':', color='k', fill=False)
#circle31 = plt.Circle((0, 0), 30,linestyle=':', color='k', fill=False)
#circle41 = plt.Circle((0, 0), 40,linestyle=':', color='k', fill=False)
#
#circle12 = plt.Circle((0, 0), 110,linestyle=':', color='k', fill=False)
#circle22 = plt.Circle((0, 0), 120,linestyle=':', color='k', fill=False)
#circle32 = plt.Circle((0, 0), 130,linestyle=':', color='k', fill=False)
#circle42 = plt.Circle((0, 0), 140,linestyle=':', color='k', fill=False)
#
#circle13 = plt.Circle((0, 0), 60,linestyle=':', color='k', fill=False)
#circle23 = plt.Circle((0, 0), 70,linestyle=':', color='k', fill=False)
#circle33 = plt.Circle((0, 0), 80,linestyle=':', color='k', fill=False)
#circle43 = plt.Circle((0, 0), 90,linestyle=':', color='k', fill=False)
#
#plt.pcolormesh(x,y,data3,cmap='jet',vmin=-11.5,vmax=-6.5)
#plt.plot()
#
#plt.title('AMTM 24hr Avgerage')
#
#plt.xlabel('Phase Speed (E-W) [m/s]')
#plt.ylabel('Phase Speed (N-S) [m/s]')
#plt.colorbar(label='log$_{10}$(PSD) [m$^{2}$/s$^{2}$]')
#plt.plot((0.0,xmax),(0.0,ymax))
#
#plt.plot(x0,y,color='k',lw='0.5')
#plt.plot(x,y0,color='k',lw='0.5')
#plt.gcf().gca().add_artist(circle1)
#plt.gcf().gca().add_artist(circle2)
#plt.gcf().gca().add_artist(circle3)
#plt.gcf().gca().add_artist(circle11)
#plt.gcf().gca().add_artist(circle21)
#plt.gcf().gca().add_artist(circle31)
#plt.gcf().gca().add_artist(circle41)
#plt.gcf().gca().add_artist(circle12)
#plt.gcf().gca().add_artist(circle22)
#plt.gcf().gca().add_artist(circle32)
#plt.gcf().gca().add_artist(circle42)
#plt.gcf().gca().add_artist(circle13)
#plt.gcf().gca().add_artist(circle23)
#plt.gcf().gca().add_artist(circle33)
#plt.gcf().gca().add_artist(circle43)
#
#TP='Total Power'+"{:.2E}".format(Decimal(np.str(t)))
#plt.text(-150,140,TP,color='white',fontsize=12)
#plt.text(78,130,'Theta='+np.str(int(theta))+'[deg]',color='white',fontsize=12)
#plt.text(78,140,'Max_Val='+np.str(int(psmax))+'[m/s]',color='white',fontsize=12)
#
#plt.show()
#plt.savefig('C:\Users\Kenneth\Desktop\AMTM-3hr\AMTM_24hrMean.jpg')

