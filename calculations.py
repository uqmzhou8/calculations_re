# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:29:10 2023

@author: zhoum
"""
for j in [400, 430, 450]:
    # rent_fur=input('What is the rent for furnished apartment \n')
    # rent_unf=input('What is the rent for unfurnished apartment \n')
    rent_fur=500
    rent_unf=j
    #Trying to find the breakeven point of furnished vs unfurnished rental
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    #sunk cost for both furnished (fur) and unfurnished (unf)
    ufur={'category': ['mattress', 'bedframe', 'fridge', 'washing machine', 'dryer'],
         'price':[100, 50,200, 100, 100]}
    ufur=pd.DataFrame(ufur)
    
    # unf={'categ'}
    
    #rent
    unf_r= np.repeat(450,6)
    fur_r=np.repeat(500,6)
    #to be used as main calculations and plotting
    # main_cal=pd.dataframe(#)
    
    cul_fur=[0]
    cul_unf=[ufur['price'].sum()]
    for i in range(24):
        val=cul_fur[i]+int(rent_fur)
        cul_fur.append(val)
        val_u=cul_unf[i]+int(rent_unf)
        cul_unf.append(val_u)
        
    # print(cul_fur)
    # print(cul_unf)
    
    plt.plot(np.array(cul_fur),color='red', label='furnished')
    plt.plot(np.array(cul_unf), color='green' , label='unfurnished')
    plt.title('Breakeven point plot of unfurnished at '+ str(rent_unf))
    plt.legend()
    plt.show()