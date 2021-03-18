import pyreadr

path = r'C:\Users\Jonma\Documents\BGU\semester 10\NLP2\enron-mysqldump.RData'
print('reading...')
result = pyreadr.read_r(path)  # also works for Rds

print(result.keys())  # let's check what objects we got
df1 = result["df1"]  # extract the pandas data frame for object df1

print('done')
