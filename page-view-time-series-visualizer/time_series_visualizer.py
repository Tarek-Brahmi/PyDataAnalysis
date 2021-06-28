import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates=True,index_col=0)

# Clean data
df = df[
    (df["value"] > df["value"].quantile(0.025)) &
    (df["value"] < df["value"].quantile(0.975))
]
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(10,5))
    df.plot(kind='line',y='value',title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019", grid=True,fontsize=10, ax=ax)
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


    df["year"] = df.index.year
    df["month"] = df.index.month
    df["month"] = df["month"].apply(lambda data: months[data-1])
    df["month"] = pd.Categorical(df["month"], categories=months)
    # Draw bar plot
    df_pivot = pd.pivot_table(df,values="value",index="year",columns="month",aggfunc=np.mean)


    ax = df_pivot.plot(kind="bar")

    fig = ax.get_figure()

    fig.set_size_inches(10, 7)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    # Draw box plots (using Seaborn)
    df['Page Views']=df['value']
    fig, ax =plt.subplots(1,2)
    fig.set_size_inches((17,8))
    sns.boxplot(x='year',y='Page Views',data=df,ax=ax[0])
    df["month"] = df["month"].apply(lambda data: data[:3])
    sns.boxplot(x='month',y='Page Views',data=df,ax=ax[1])
    # Save image and return fig (don't change this part)
    
    fig.savefig('box_plot.png')
    return fig


#draw_line_plot()
draw_bar_plot()
draw_box_plot()

