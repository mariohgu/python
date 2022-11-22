import pandas as pd

df_movies = pd.read_csv('C:\\Users\\user\\Documents\\Coding\\python\\numpy_pandas\\n_movies.csv')
aux = df_movies.loc[3:4,["duration","year"]]
tre = df_movies.iloc[344:346,0:2]
print(df_movies["year"]>2016)

print(aux)
print(tre)