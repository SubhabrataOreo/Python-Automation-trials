#creating a docoment file inside F drive
file=open("F:\\ test.txt",'w')
file.write('Data Science is fun\n')
list=["It's emerging\n","It's getting fancy day by day\n","It is no doubt the sexiest field in 21st Century to explore\n"]
file.writelines(list)
file2=open("F:\\ odi.txt",'w')
list2=["Data speaks the unspoken\n","It is very useful to get insights from data\n","We have enormous data around\n"]
file2.writelines(list2)
ff=open("F:\\ test.txt",'a')
sf=open("F:\\ odi.txt",'r')
info=sf.read()
ff.write(info)
file.close()
file2.close()