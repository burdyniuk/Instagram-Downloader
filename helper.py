from datetime import datetime, date

def print_log(what):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    current_day = today.strftime("%d/%m/%y")
    print("["+current_day+", "+current_time+"]" + " " + str(what))