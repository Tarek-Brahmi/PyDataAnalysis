import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    x,y=df["Year"],df["CSIRO Adjusted Sea Level"]

    gradient, intercept, r_value, p_value, std_err = linregress(x,y)
    xmin,xmax=df['Year'].min(),df['Year'].max()
    fig, ax = plt.subplots(figsize=(10,5))
    x1=np.linspace(xmin,np.int64(2050),5)
    y1=gradient*x1+intercept
    x2=np.linspace(np.int64(2000),np.int64(2050),5)
    y2=gradient*x2+intercept


    df.plot(kind='scatter', x='Year', y='CSIRO Adjusted Sea Level',title="Rise in Sea Level", grid=True,fontsize=10, ax=ax) 
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    plt.plot(x1,y1,'-r')

    plt.plot(x2,y2,'-b')
    plt.show(block=True)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()