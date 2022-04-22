import pandas as pd
import dateutil.parser as parser

file = str(input("Masukkan directory file (csv) : "))

df = pd.read_csv(file, encoding= 'unicode_escape')

a = str(input("Masukkan nama kolom kode unik user : "))
b = str(input("Masukkan nama kolom parameter Recency : "))
c = str(input("Masukkan nama kolom parameter Frequency : "))
d = str(input("Masukkan nama kolom parameter Monetary : "))

def delete_row(X,a,b) :
  print(X.isnull().sum())
  Y = X.dropna(subset=[a,b])
  print(Y.isnull().sum())
  return Y

df2 = delete_row(df,a,b)
print(df2.isnull().sum())

def rfm(X,a,b,c,d) :
  X[b] = X[b].apply(lambda date: parser.parse(date))

  present = X[b].max()

  Y = X.groupby(a).agg({
  c : 'nunique',
  d : 'sum',
  b : lambda x : (present - x.max()).days 
  }).reset_index()  

  Y['r_score'] = pd.cut(Y[b].sort_values(ascending=True), 4, labels=['1','2','3','4'])
  Y['f_score'] = pd.cut(Y[c].sort_values(ascending=False), 4, labels=['1','2','3','4'])
  Y['m_score'] = pd.cut(Y[d].sort_values(ascending=False), 4, labels=['1','2','3','4'])
  
  return Y

df3 = rfm(df2,a,b,c,d)

def segment(r,f,m) : 
  if r=='1' and f=='1' and m=='1' :
    return 'Best Customers'
  elif f=='1' :
    return 'Loyal Customers'
  elif m=='1' :
    return 'Big Spenders'
  elif r=='3' and f=='1' and m=='1' :
    return 'Almost Lost'
  elif r=='4' and f=='1' and m=='1' :
    return 'Lost Customers'
  elif r=='4' and f=='4' and m=='4' :
    return 'Lost Cheap Customers'
  
df3['Segment'] = df3.apply(lambda x : segment(x.r_score,x.f_score,x.m_score), axis=1)

filename = str(input('Masukkan nama file dengan format type .csv : '))
df3.to_csv(filename, index=False)

