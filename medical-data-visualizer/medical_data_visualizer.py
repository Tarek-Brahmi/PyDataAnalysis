import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = ((df["weight"]/(df["height"]**2))*10000 > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad.
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0.
# If the value is more than 1, make the value 1.
for i in df.index:
    if df.at[i, "cholesterol"] == 1:
        df.at[i, "cholesterol"] = 0
    if df.at[i, "cholesterol"] > 1:
        df.at[i, "cholesterol"] = 1
    if df.at[i, 'gluc'] == 1:
        df.at[i, 'gluc'] = 0
    if df.at[i, 'gluc'] > 1:
        df.at[i, 'gluc'] = 1
# Draw Categorical Plot


def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio', 'id'], value_vars=[
                     'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = None
    fig, ax = plt.subplots(figsize=(10, 8))
    # Draw the catplot with 'sns.catplot()'
    sns.catplot(x="variable", col_wrap=4, hue="cardio",
                kind="count", col="cardio", data=df_cat,ax=ax)
    
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df.drop(df[df['ap_lo'] <= df['ap_hi']].index, inplace=True)
    df.drop(df[df['height'] >= df['height'].quantile(0.025)].index, inplace=True)
    df.drop(df[df['height'] >= df['height'].quantile(0.975)].index, inplace=True)
    df.drop(df[df['weight'] <= df['weight'].quantile(0.025)].index, inplace=True)
    df.drop(df[df['weight'] >= df['weight'].quantile(0.975)].index, inplace=True)
    df_heat = df

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(df.corr())
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(corr, mask=mask,
                annot=True, center=0,
                linewidths=.5, fmt='0.1f', ax=ax)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
draw_cat_plot()
draw_heat_map()