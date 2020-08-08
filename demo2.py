ff=open("F:\\ test.txt",'a')
sf=open("F:\\ odi.txt",'r')
info=sf.read()
ff.write(info)
sf.close()
ff.close()
import os
import shutil
os.mkdir("F:\\ Match\\")"""
##shutil.move("F:\\ odi.txt","F:\\ Match\\")
#list=["F:\\ test.txt","E:\\Platelet_disorders.pdf","E:\\Untitled spreadsheet.xlsx"]
#for i in list:
	#shutil.copy(i,"F:\\ Match\\")
#f1=open("F:\\dot.txt",'w')
#set=["We are human\n","To err is human\n","Be a good human being"]
#f1.writelines(set)
#shutil.copy("F:\\dot.txt","F:\\ Match\\")
#import os
#os.rename("F:\\dot.txt","F:\\testing.txt")
"""filename=["F:\\Poi 1.txt","F:\\Poin 2.txt","F:\\Point 3.txt"]
for i in filename:
	j=i.split(" ")
	new=(j[0]+"new.txt")
	os.rename(i,new)

files=["F:\\Poinew.txt","F:\\Poinnew.txt","F:\\Pointnew.txt"]
for i in files:
	shutil.move(i,"F:\\ Match\\")

