import openpyxl
from openpyxl import Workbook,load_workbook
from datetime import datetime, timedelta
book=load_workbook('missions.xlsx')
sheet=book.active
i=2
while sheet['C'+str(i)].value!=None:#if there is a date for the mission
    delta=sheet['C'+str(i)].value-datetime.strptime('01/01/2024', '%d/%m/%Y')
    dt=delta.days*86400/149597871#finds the t equivalent
    sheet['E'+str(i)].value=dt-365*0.000577483#the starting date on the 8-planets simulation 
    sheet['G'+str(i)].value,sheet['H'+str(i)].value=0,0#initial dates on the 4-planets simulation
    if sheet['B'+str(i)].value<4:# if the mission is to one of the inner planets(who appear in the 4-planets simulation)
        sheet['G'+str(i)].value=dt-20*0.000577483#the starting date on the 4-planets simulation
    if sheet['D'+str(i)].value==None:#if there isn't any specified ending date
        sheet['F'+str(i)].value=dt+365*0.000577483#the ending date on the 8-planets simulation
        if sheet['B'+str(i)].value<4:
            sheet['H'+str(i)].value=dt+20*0.000577483#the ending date on the 4-planets simulation
    else:#if there is a specified date for the ending of the (part of the) mission
        sdelta=sheet['D'+str(i)].value-datetime.strptime('01/01/2024', '%d/%m/%Y')
        dt=sdelta.days*86400/149597871#the t equivalent of the specified ending date
        if sheet['B'+str(i)].value<4:
            sheet['H'+str(i)].value=dt#the ending date on the 4-planets simulation
            
    i=i+1
book.save('missions.xlsx')
