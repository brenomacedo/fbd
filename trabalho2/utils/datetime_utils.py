import sys
sys.path.append("..")

import datetime

def getDate(inputString: str):
    dateString = input(inputString)
    try:
        datetime.datetime.strptime('%d/%m/%Y')
        dateInfo = dateString.split('/')
        return datetime.date(dateInfo[2], dateInfo[1], dateInfo[0])
    except:
        raise Exception(f"Formato da data inválido! ({dateString})")

def getTime(inputString: str):
    timeString = input(inputString)
    try:
        datetime.datetime.strptime('%H:%M')
        timeInfo = timeString.split(':')
        return datetime.time(timeInfo[0], timeInfo[1])
    except:
        raise Exception(f"Formato do horário inválido! ({timeString})")