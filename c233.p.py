import pandas as pd

data = pd.read_csv('studentData.csv')

df['Total_marks_obtained']=df.iloc[:,[2,3,4]].sum(axis = 1)

df.loc[df['Total_marks_obtained'] > 250, 'Grade'] = 'A'

df.loc[df['Total_marks_obtained'] < 250, 'Grade'] = 'B'

df['Percentage'] = (df['Total_marks_obtained']/300) * 100

print("Report Card Of All Students\n",df)


