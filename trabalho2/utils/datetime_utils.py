import sys
sys.path.append("..")

import datetime

def getDate(inputString: str):
    dateString = input(inputString)
    try:
        return datetime.datetime.strptime(dateString, '%d/%m/%Y')
    except:
        raise Exception(f"Formato da data inválido! ({dateString})")

def getTime(inputString: str):
    timeString = input(inputString)
    try:
        return datetime.datetime.strptime(timeString, '%H:%M')
    except:
        raise Exception(f"Formato do horário inválido! ({timeString})")