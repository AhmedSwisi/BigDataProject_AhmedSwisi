import pandas as pd
df=pd.read_csv('thebatmanfinal.csv',engine='python')
df_clean = df[df['language'] == "en"]
df_clean.drop
df_clean.to_csv('the_batman_final.csv')