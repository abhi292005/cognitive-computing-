#Ques1
import pandas as pd
df=pd.DataFrame({'Tid' : [1,2,3,4,5,6,7,8,9,10],
                 'Refund' : ['Yes','No','No','Yes','No','No','Yes','No','No','No'],
                 'Marital Status' : ['Single','Married','Single','Married','Divorced','Married','Divorced','Single','Married','Single'],
                 'Taxable Income' : ['125K','100K','70K','120K','95K','60K','220K','85K','75K','90K'],
                 'Cheat' : ['No','No','No','No','Yes','No','No','Yes','No','Yes']
                })
print(df)
     
   Tid Refund Marital Status Taxable Income Cheat
0    1    Yes         Single           125K    No
1    2     No        Married           100K    No
2    3     No         Single            70K    No
3    4    Yes        Married           120K    No
4    5     No       Divorced            95K   Yes
5    6     No        Married            60K    No
6    7    Yes       Divorced           220K    No
7    8     No         Single            85K   Yes
8    9     No        Married            75K    No
9   10     No         Single            90K   Yes

#Ques2
srow=df.iloc[[0,4,7,8]]
print(srow)
     
   Tid Refund Marital Status Taxable Income Cheat
0    1    Yes         Single           125K    No
4    5     No       Divorced            95K   Yes
7    8     No         Single            85K   Yes
8    9     No        Married            75K    No

#Ques3
s=df.loc[3:7]
print(s)
print()
t=df.iloc[[4,5,6,7,8],[2,3,4]]
print(t)
print()
u=df.iloc[[0,1,2,3,4,5,6,7,8,9],[1,2,3]]
print(u)
     
   Tid Refund Marital Status Taxable Income Cheat
3    4    Yes        Married           120K    No
4    5     No       Divorced            95K   Yes
5    6     No        Married            60K    No
6    7    Yes       Divorced           220K    No
7    8     No         Single            85K   Yes

  Marital Status Taxable Income Cheat
4       Divorced            95K   Yes
5        Married            60K    No
6       Divorced           220K    No
7         Single            85K   Yes
8        Married            75K    No

  Refund Marital Status Taxable Income
0    Yes         Single           125K
1     No        Married           100K
2     No         Single            70K
3    Yes        Married           120K
4     No       Divorced            95K
5     No        Married            60K
6    Yes       Divorced           220K
7     No         Single            85K
8     No        Married            75K
9     No         Single            90K

import csv

with open('file.csv','w',newline='') as file:
  writer=csv.writer(file)
  writer.writerow(["SNO","NAME","RNO"])
  writer.writerow([1,"abc",11])
  writer.writerow([2,"def",12])
  writer.writerow([3,"ghi",13])
  writer.writerow([4,"jkl",14])
  writer.writerow([5,"mno",15])
  writer.writerow([6,"pqr",16])

     

#Ques 4
import pandas as pd
pd.read_csv('file.csv',nrows=5)
     
SNO	NAME	RNO
0	1	abc	11
1	2	def	12
2	3	ghi	13
3	4	jkl	14
4	5	mno	15

#Ques 5
import pandas as pd
data=pd.read_csv('file.csv')

data.drop(4,axis=0,inplace=True)  #Row 4 deleted
data.drop("RNO",axis=1,inplace=True) #Column 3 deleted
print(data)
     
   SNO NAME
0    1  abc
1    2  def
2    3  ghi
3    4  jkl
5    6  pqr

import csv

with open('employees.csv','w',newline='') as file:
  writer=csv.writer(file)
  writer.writerow(["Employee_ID","Name","Department","Age","Salary","Years_of_Experience","Joining_Date","Gender","Bonus","Rating"])
  writer.writerow([101,"Alice","HR",29,50000,4,"2020-03-15","Female",5000,4.5])
  writer.writerow([102,"Bob","IT",34,70000,8,"2017-07-19","Male",7000,4.0])
  writer.writerow([103,"Charlie","IT",41,65000,10,"2013-06-01","Male",6000,3.8])
  writer.writerow([104,"Diana","Marketing",28,55000,3,"2021-02-10","Female",4500,4.7])
  writer.writerow([105,"Edward","Sales",38,60000,12,"2010-11-25","Male",5000,3.5])

     

#Ques 6
import pandas as pd

data=pd.read_csv('employees.csv')
#a
print('Number of rows: ',data.shape[0])
print('Number of columns: ',data.shape[1])
print()
print()

#b
print("Data Info:")
data.info()
print()
print()


#c
print('Data description:')
print(data.describe())
print()
print()



#d
f=data.head(2)
l=data.tail(1)
print('First two entries:')
print(f)
print()
print('Last one entry:')
print(l)
print()
print()


#e
print('Mean salary:',data['Salary'].mean())
print('Total bonus',data['Bonus'].sum())
print('Youngest employee age: ',data['Age'].min())
print('Highest performance rating: ',data['Rating'].max())
print()
print()


#f
data.sort_values("Salary",axis=0,ascending=True,inplace=True,na_position='last')
print(data)
print()
print()


#g
li=list()
for value in data['Rating']:
  if(value>=4.5):
    li.append('Excellent')
  elif(value>=4 and value<4.5):
    li.append('Good')
  else:
    li.append('Average')

data['Category']=li
print(data)
print()
print()


#h
print(data.isnull())
print(data)
print()
print()


#i
data.columns=['ID','Name','Department','Age','Salary','Years_of_Experience','Joining_Date','Gender','Bonus','Rating','Category']
print(data)
print()
print()



#j
print('More than 5 years of experience:')
print(data.loc[data['Years_of_Experience']>5])
print()
print()
print('IT department:')
print(data.loc[data['Department']=='IT'])
print()
print()



#k
tax=list()
for val in data['Salary']:
  tax.append(val*0.10)
data['Tax']=tax
print(data)
print()
print()



#l
data.to_csv('employees_updated.csv')
print('Saved into new csv!!')
     
Number of rows:  5
Number of columns:  10


Data Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 10 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   Employee_ID          5 non-null      int64  
 1   Name                 5 non-null      object 
 2   Department           5 non-null      object 
 3   Age                  5 non-null      int64  
 4   Salary               5 non-null      int64  
 5   Years_of_Experience  5 non-null      int64  
 6   Joining_Date         5 non-null      object 
 7   Gender               5 non-null      object 
 8   Bonus                5 non-null      int64  
 9   Rating               5 non-null      float64
dtypes: float64(1), int64(5), object(4)
memory usage: 532.0+ bytes


Data description:
       Employee_ID        Age       Salary  Years_of_Experience   Bonus  \
count     5.000000   5.000000      5.00000             5.000000     5.0   
mean    103.000000  34.000000  60000.00000             7.400000  5500.0   
std       1.581139   5.612486   7905.69415             3.847077  1000.0   
min     101.000000  28.000000  50000.00000             3.000000  4500.0   
25%     102.000000  29.000000  55000.00000             4.000000  5000.0   
50%     103.000000  34.000000  60000.00000             8.000000  5000.0   
75%     104.000000  38.000000  65000.00000            10.000000  6000.0   
max     105.000000  41.000000  70000.00000            12.000000  7000.0   

         Rating  
count  5.000000  
mean   4.100000  
std    0.494975  
min    3.500000  
25%    3.800000  
50%    4.000000  
75%    4.500000  
max    4.700000  


First two entries:
   Employee_ID   Name Department  Age  Salary  Years_of_Experience  \
0          101  Alice         HR   29   50000                    4   
1          102    Bob         IT   34   70000                    8   

  Joining_Date  Gender  Bonus  Rating  
0   2020-03-15  Female   5000     4.5  
1   2017-07-19    Male   7000     4.0  

Last one entry:
   Employee_ID    Name Department  Age  Salary  Years_of_Experience  \
4          105  Edward      Sales   38   60000                   12   

  Joining_Date Gender  Bonus  Rating  
4   2010-11-25   Male   5000     3.5  


Mean salary: 60000.0
Total bonus 27500
Youngest employee age:  28
Highest performance rating:  4.7


   Employee_ID     Name Department  Age  Salary  Years_of_Experience  \
0          101    Alice         HR   29   50000                    4   
3          104    Diana  Marketing   28   55000                    3   
4          105   Edward      Sales   38   60000                   12   
2          103  Charlie         IT   41   65000                   10   
1          102      Bob         IT   34   70000                    8   

  Joining_Date  Gender  Bonus  Rating  
0   2020-03-15  Female   5000     4.5  
3   2021-02-10  Female   4500     4.7  
4   2010-11-25    Male   5000     3.5  
2   2013-06-01    Male   6000     3.8  
1   2017-07-19    Male   7000     4.0  


   Employee_ID     Name Department  Age  Salary  Years_of_Experience  \
0          101    Alice         HR   29   50000                    4   
3          104    Diana  Marketing   28   55000                    3   
4          105   Edward      Sales   38   60000                   12   
2          103  Charlie         IT   41   65000                   10   
1          102      Bob         IT   34   70000                    8   

  Joining_Date  Gender  Bonus  Rating   Category  
0   2020-03-15  Female   5000     4.5  Excellent  
3   2021-02-10  Female   4500     4.7  Excellent  
4   2010-11-25    Male   5000     3.5    Average  
2   2013-06-01    Male   6000     3.8    Average  
1   2017-07-19    Male   7000     4.0       Good  


   Employee_ID   Name  Department    Age  Salary  Years_of_Experience  \
0        False  False       False  False   False                False   
3        False  False       False  False   False                False   
4        False  False       False  False   False                False   
2        False  False       False  False   False                False   
1        False  False       False  False   False                False   

   Joining_Date  Gender  Bonus  Rating  Category  
0         False   False  False   False     False  
3         False   False  False   False     False  
4         False   False  False   False     False  
2         False   False  False   False     False  
1         False   False  False   False     False  
   Employee_ID     Name Department  Age  Salary  Years_of_Experience  \
0          101    Alice         HR   29   50000                    4   
3          104    Diana  Marketing   28   55000                    3   
4          105   Edward      Sales   38   60000                   12   
2          103  Charlie         IT   41   65000                   10   
1          102      Bob         IT   34   70000                    8   

  Joining_Date  Gender  Bonus  Rating   Category  
0   2020-03-15  Female   5000     4.5  Excellent  
3   2021-02-10  Female   4500     4.7  Excellent  
4   2010-11-25    Male   5000     3.5    Average  
2   2013-06-01    Male   6000     3.8    Average  
1   2017-07-19    Male   7000     4.0       Good  


    ID     Name Department  Age  Salary  Years_of_Experience Joining_Date  \
0  101    Alice         HR   29   50000                    4   2020-03-15   
3  104    Diana  Marketing   28   55000                    3   2021-02-10   
4  105   Edward      Sales   38   60000                   12   2010-11-25   
2  103  Charlie         IT   41   65000                   10   2013-06-01   
1  102      Bob         IT   34   70000                    8   2017-07-19   

   Gender  Bonus  Rating   Category  
0  Female   5000     4.5  Excellent  
3  Female   4500     4.7  Excellent  
4    Male   5000     3.5    Average  
2    Male   6000     3.8    Average  
1    Male   7000     4.0       Good  


More than 5 years of experience:
    ID     Name Department  Age  Salary  Years_of_Experience Joining_Date  \
4  105   Edward      Sales   38   60000                   12   2010-11-25   
2  103  Charlie         IT   41   65000                   10   2013-06-01   
1  102      Bob         IT   34   70000                    8   2017-07-19   

  Gender  Bonus  Rating Category  
4   Male   5000     3.5  Average  
2   Male   6000     3.8  Average  
1   Male   7000     4.0     Good  


IT department:
    ID     Name Department  Age  Salary  Years_of_Experience Joining_Date  \
2  103  Charlie         IT   41   65000                   10   2013-06-01   
1  102      Bob         IT   34   70000                    8   2017-07-19   

  Gender  Bonus  Rating Category  
2   Male   6000     3.8  Average  
1   Male   7000     4.0     Good  


    ID     Name Department  Age  Salary  Years_of_Experience Joining_Date  \
0  101    Alice         HR   29   50000                    4   2020-03-15   
3  104    Diana  Marketing   28   55000                    3   2021-02-10   
4  105   Edward      Sales   38   60000                   12   2010-11-25   
2  103  Charlie         IT   41   65000                   10   2013-06-01   
1  102      Bob         IT   34   70000                    8   2017-07-19   

   Gender  Bonus  Rating   Category     Tax  
0  Female   5000     4.5  Excellent  5000.0  
3  Female   4500     4.7  Excellent  5500.0  
4    Male   5000     3.5    Average  6000.0  
2    Male   6000     3.8    Average  6500.0  
1    Male   7000     4.0       Good  7000.0  


Saved into new csv!!