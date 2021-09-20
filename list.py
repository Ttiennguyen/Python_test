numbers  = [1,2,3,4,5]
names = ['tien','nguyen']

#truy suat phan tu
print numbers[0]
print names[1]

#ktr gia tri co trong mang
print "1" in numbers #false vi in ngoac 1 chu ko phai 1 trong mang
print 'tien' in names

#trich xuat mang con
print numbers [:2] #in dau mang [1,2]
print numbers [-2:] #in cuoi mang [4,5]

#xoa phan tu
del numbers [1] #xoa 1 phan tu [1, 3, 4, 5]
print numbers
del numbers [0:2] #xoa tu dau den khuc da dat la 2 [4, 5]
print numbers 

#noi 2 mang
a = [1,2]
b = [3,4]
print a+b

#them 1 phan tu vao mang
numbers.append(6)
print numbers

#lay phan tu cuoi mang
number = [1,2,3]
mynumber =number.pop()
print mynumber
print number