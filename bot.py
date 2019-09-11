import camelot
import requests
from datetime import date
def getPDF():
    baseUrl='https://www.winthrop.edu/uploadedFiles/Police/DailyCaseLog-'
    today=date.today()
    formatted_date = today.strftime("%B%Y")
    extension = ".pdf"
    monthext=formatted_date+extension
    url=baseUrl+monthext
    with open('/tmp/pol.pdf', 'wb') as f:
        f.write(requests.get(url).content)
    pdfFile='/tmp/pol.pdf'
    return pdfFile

file=getPDF()
tables=camelot.read_pdf('/tmp/pol.pdf', pages='all', strip_text=' .\n')
for i in range(len(tables)):
    dateTime=tables[i].df.loc[4,0]
    dateTimeList=dateTime.partition('T')
    time=dateTimeList[1]+dateTimeList[2]
    synopsis = tables[i].df.loc[10,0].split(":")[1]
    print(synopsis)
    #if(dateTimeList[i].split(":")[1]!=''):
    #    print(dateTimeList[0])
    #    print("")
    #    print(time)
    #    print("")
    #    synopsis = tables[i].df.loc[10,0]
    #    print(synopsis.split(": ")[1])
    #    print("")
    
    
