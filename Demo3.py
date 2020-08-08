
from PyPDF2 import PdfFileReader, PdfFileWriter
write_obj=PdfFileWriter()
pdf_list=["E:\\Demo3\\1. Values & Ethics In Profession.pdf","E:\\Demo3\\EM Theory SKB Sir Updated.pdf"]
for i in pdf_list:
	read_obj= PdfFileReader(i)
	pages=read_obj.getNumPages()
	#print(pages)
	for p in range(pages):
		pd=read_obj.getPage(p)
		write_obj.addPage(pd)
write_obj.encrypt('Subha123','Misti123',True)
pdf_concat=open("E:\\Demo3\\Concat_1st.pdf",'wb')
write_obj.write(pdf_concat)
