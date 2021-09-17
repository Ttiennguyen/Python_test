for letter in  "python":
    print "letter is ", letter 
number  = ['one', 'two', 'three']
for number in number:
    print "number",number

count =0
while (count <10):
    print "",count
    count+=1
#ham 
def sum(a,b):
    return (a+b)
print "",sum(7,4)

def plus(c, b=10):
    return (c+b)
print "",plus(2)
#xu ly chuoi
str1 = "hello"
print "",str1[1]

paragrap = """this is line 1
this is line 2
this is line 3"""
print "",paragrap

#noi chuoi
num1 = " haaaaaa"
num2 = "hiiii "
str = num1+ "" +num2
print"",str

#trich chuoi con
str = "chao tat ca moi nguoi"
print str[1:3]
print str[:-3]
print str[6]
print str[-4:5]
cout = len(str)
print "",cout
#tim va thay the noi dung
newstr= str.replace("chao","tam biet")
print newstr
print str.find("tat")
print str.find("khong")
#tach chuoi
str =  '$ con meo khong ngu ,'
print str.split(' ')    #tach chuoi tung phan
print str.strip('$'',')    # loai bo ki tu o 2 dau mang
print str.lstrip('$')   #loai bo ki tu o dau mang
print str.rstrip(',')   #loai bo o cuoi mang
string = "THIET LUN"
print string.lower()    #viet hoa thanh viet thuong
str1 ='thi'
print str1.upper()

#list
number = [1,2,3,4,5]
name = ['tien','nguyen']
print number[-3]
print name[0]
print "tien" in name

name =['a','b','c','d']
