### 1 команда
print(type('slovo'))
print('------'*10)
### 2 команда
print('slovo sochetanie '*2)
print('------'*10)
### 3 команда
kortez = (1,5,6,1,2,5,6)
for i in range(len(kortez)):
    print(kortez[i])
    print('------'*10)
### 4 команда
t1 = [1,2,6,1,7,9,45,32,4]
t2 = [2,4,7,1,25,6,34,123]
for i in range(len(t1)):
    if t1[i] in t2:
        print(t1[i])
print('------'*10)
### 5 команда
l = 5
print(int(str(5)*10) / 123)
