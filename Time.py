from datetime import datetime


def time():
    now = datetime.now()
    ctime = now.strftime("%r")
    return ctime


def date():
    from datetime import date
    today = date.today()
    cdate = today.strftime("%d/%m/%Y")
    return cdate


time()
