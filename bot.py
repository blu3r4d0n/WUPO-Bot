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
    date=tables[i].df.loc[4,0]
    dateList=date.partition('T')
    time=dateList[1]+dateList[2]
    print(dateList[0])
    print("")
    print(time)
    print("")
    print(tables[i].df.loc[10,0])
    print("")
    
