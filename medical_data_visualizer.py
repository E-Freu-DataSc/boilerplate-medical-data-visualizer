import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("medical_examination.csv")

df["overweight"] = (df["weight"] / ((df["height"] / 100) ** 2)).apply(lambda x: 1 if x > 25 else 0)

# 3: Normalizar colesterol y glucosa
df["cholesterol"] = df["cholesterol"].apply(lambda x: 0 if x == 1 else 1)
df["gluc"] = df["gluc"].apply(lambda x: 0 if x == 1 else 1)

# 4: 
def draw_cat_plot(df_cat):
    # Melt the data frame to format it for graph
    df_cat = pd.melt(df_cat, id_vars=["id", "cardio"], 
                     value_vars=["gluc", "smoke", "alco", "active", "overweight"], 
                     var_name="Feature", value_name="value")
    
    # Nueva columna de conteo de los valores en "value" de las "feature" llamada total
    df_cat = df_cat.groupby(["Feature", "cardio", "value"]).size().reset_index(name="total")

  
    fig = sns.catplot(data=df_cat, x="Feature", y="total", hue="value", col="cardio", kind="bar", height=5, aspect=1.2)
    
    
    plt.show()


    fig.savefig("catplot.png")

    return fig


# 11: Define function to draw heatmap
def draw_heat_map(df_heat):
    # 12. Filter rows where diastolic pressure is not higher than systolic
    conditions = (
        (df_heat['ap_lo'] <= df_heat['ap_hi']) &  # Diastolic pressure should not exceed systolic
        (df_heat['height'] >= df_heat['height'].quantile(0.025)) &  # Height above 2.5th percentile
        (df_heat['height'] <= df_heat['height'].quantile(0.975)) &  # Height below 97.5th percentile
        (df_heat['weight'] >= df_heat['weight'].quantile(0.025)) &  # Weight above 2.5th percentile
        (df_heat['weight'] <= df_heat['weight'].quantile(0.975))    # Weight below 97.5th percentile
    )
    
    df_heat_cleaned = df_heat[conditions]

    # 13. Calculate correlation matrix
    corr = df_heat_cleaned.corr()

    # 14. Generate mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 15. Set up the heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)

    # 16. Display the heatmap
    plt.show()

    # 17. Save the figure
    fig.savefig('heatmap.png')
    return fig

# 18: Call the function with the cleaned data
