import pandas as pd

df = pd.read_excel('sample.xlsx')
print(df)

summary1 = df.describe()
print(summary1)

sorted_df = df.sort_values(by = ['국어'], ascending=True)
print(sorted_df)

filterd_df = df[df['반'] ==  '1반']
print(filterd_df)

korean_df = pd.pivot_table(df, index='반', values='국어', aggfunc=['mean', 'median'])
print(korean_df)

df['총점'] = df.iloc[:, 2:].sum(axis=1)

top_students = df.loc[df.groupby('반')['총점'].idxmax()]
print(top_students)

output_path = 'top_students.xlsx'
top_students.to_excel(output_path, index=False)

