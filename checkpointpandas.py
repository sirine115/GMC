import pandas as pd
import numpy as np


exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df=pd.DataFrame(exam_data,index=labels)

#Question 1 
df.head(3)
#Question 2 
df = df.dropna()
#Question 3 
name_score_df = df[['name', 'score']]
#question 4
exam_data1= {'name': ["Suresh"],
'score': [15.5] ,
'attempts': [1], 
'qualify': ["yes"]}
labels1 = ['k']
df1=pd.DataFrame(exam_data1,index=labels1)
new_data=pd.concat([df,df1])
#Question 5 
new_data.drop('attempts',axis=1)
#Question 6 
new_data['Success'] = new_data['score'].apply(lambda x: 1 if x > 10 else 0)
print(new_data)
#Question 7 
new_data.to_csv('my_data.csv', index=False)
