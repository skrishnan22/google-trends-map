import urllib
from bs4 import BeautifulSoup
import json
import time
import matplotlib.animation as animation
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt


map = Basemap()                                                   
map.drawcoastlines()                                       #setting up a world map using Basemap    
map.drawcountries()                                                  
map.bluemarble()                                                 
                                                           
url="http://hawttrends.appspot.com/api/terms/"             #extracting trends data using api
data = json.loads(urllib.urlopen(url).read())               

plt.title('GOOGLE TRENDS MAP')
x=[]
y=[]
point=[]

                                                                                                                                                                                   
longitudes=[74.38,-60.00,105.55,134.08,-120.69,8.56,25.3,-101.376,-2.25,7.80,23.25,101.68,37.95,113.61,8.077,-71.21,-58.57,-75.92,13.38,10.13]                  

latitudes=[22.52,-36.30,21.05,-23.05,64.008,56.28,62.61,39.31,53.47,46.60,-29.68,3.15,0.98,-0.33,10.00,-34.05,-2.06,5.11,42.59,50.74]                              
                                                                                                                                                                                                                                                                                                                                                                             
#creating list for country
country_codes=['3','30','28','8','13','49','50','1','9','46','40','34','37','19','52','38','18','32','27','15']     

#extracting 
l=len(country_codes)
i=0

for i in range(0,len(latitudes)):
   x1,y1=map(longitudes[i],latitudes[i])
   x.append(x1)
   y.append(y1)


for i in range(0,len(latitudes)):
    point.append(plt.text(x[i],y[i],"first",fontsize=7,color='white',bbox=dict(facecolor='black', alpha=0.5)))
            
def init():
    
    for i in range(0,len(latitudes)):                                                                       
     point[i].set_text(" ")                                                                                 #changing trend text in the plot        
                                                                                              
    return point                                                                                                          


def animate(num):                                                                                               
                                                                                                                
    for i in range(0,len(latitudes)):
        point[i].set_text(data[country_codes[i]][num])                                                      #thanks to http://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/   
        
    return point                                                                                        #for a great tutorial on matplotlib animation                        
                                                                                                                
anim = animation.FuncAnimation(plt.gcf(), animate, init_func=init,frames=10, interval=3000, blit=True)

plt.show()
    
    

        
   


