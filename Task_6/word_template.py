import docx
import os

date = str(input("Please enter today's date: "))
name = str(input("Please enter your full name: ")).upper()
roll_number = str(input("Please enter your roll number: "))
year = str(input("Please enter year: "))
leave_days = str(input("Please enter number of requested leave days: "))
start_day = str(input("Please enter start day of the leave: "))
end_day = str(input("Please enter end day of the leave: "))
name = 'PAWEL PINKOWICZ'

doc = docx.Document('test.docx')
num_par = doc.paragraphs
for i in range(len(num_par)):
    print(i, doc.paragraphs[i].text)

date_par = doc.paragraphs[2].add_run(' {0}'.format(date))
name_par = doc.paragraphs[4].add_run(' {0}'.format(name))
roll_number_par = doc.paragraphs[5].add_run(' {0}'.format(roll_number))
year_par = doc.paragraphs[6].add_run(' {0}'.format(year))
doc.save('new.docx')

main_text = doc.paragraphs[16].text
main_text = main_text.replace('____', leave_days, 1)
main_text = main_text.replace('____________', start_day, 1)
main_text = main_text.replace('___________', end_day, 1)
doc.paragraphs[16].text = main_text
#words = main_text.rsplit()
print(main_text)
# print(words)

doc.save('new.docx')