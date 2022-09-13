import pandas as pd

"""
Here panda library is used for conveniently manupulating the csv file
content as panda dataframe.
"""
#Reading in the csv file as dataframe
df = pd.read_csv("out.csv")

#Combining two data fields (date and time) into one data field (datetime)
df['DateTime'] = df['Date'].str.cat(df['Time'], sep=" ")
df.drop(["Date", "Time"], axis=1, inplace=True)

#DateTime field is formatted required for inserting into database
df[['DateTime']] = df[['DateTime']].apply(pd.to_datetime)

#Function for relocating data field
def move_column_inplace(df, col, pos):
    col = df.pop(col)
    df.insert(pos, col.name, col)
    
#Function is called for changing DataTime field location to clumn index 1 
move_column_inplace(df, 'DateTime', 1)

print(df)
