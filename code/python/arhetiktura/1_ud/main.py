import numpy as np               
import matplotlib.pyplot as plt  

img = np.ones((800,800,3))

#Man ir 3 kontrolpunkti 
                #P0    P1      P2     P3
def DrawBezier(x0,y0, x1,y1, x2,y2, x3,y3):
    
    x = x0 # sākumpunkta definēšana pēc x ass
    y = y0 # sākumpunkta definēšana pēc y ass
    t = 0 # parametrs t, kas pieder intervālam no 0 līdz 1
    ts = 0.001 # solis, ar kuru mainās parametrs t. Jo mazāks ir solis ts,
    #jo vairāk punktu uz līknes uzzīmēs algoritms. 

    while t <= 1.0:  # kamēr nav sasniegts interavala gala punkts
        
        B0 = 1*(1-t) * (1-t) #rēķinam Beršteina 0.polinomu
        B1 = 2* (1-t) * t #rēķinam Beršteina 1.polinomu
        B2 = 1* t * t # #rēķinam Beršteina 2.polinomu
        B3 = t**3
        
       
        x = int(x0*B0 + x1*B1 + x2*B2 + x3*B3) #rēķinam līknes pikseļa koordinātes pēc x ass
        y = int(y0*B0 + y1*B1 + y2*B2 + y3*B3) #rēķinam līknes pikseļa koordinātes pēc y ass
        
        img[y,x] = (1,0,0) #zīmējam tekošo pikseli sarkanajā krāsā
        
        t=t+ts #palielinam t vērtību
        
    return
             # P0         P1          P2                P3
DrawBezier(300, 100,     10, 10,    500, 550,       200,100) #zīmējam līkni
    

plt.figure(figsize=(10,8), dpi = 100, facecolor='w')
plt.imshow(img)
plt.show()