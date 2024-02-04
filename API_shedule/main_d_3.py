import datetime

import schedule


def print_mes(mes, inter):
    current_date = datetime.datetime.now()
    current_time = current_date.strftime('%H')
    if not inter[0] <= current_time <= inter[1]:
        if current_time == '12':
            print(mes * 12)
        else:
            print(mes * (int(current_time) % 12))

message = input()
interwal = input().split('-')
schedule.every().minutes.at(":00").do(print_mes, message, interwal)

while True:
    schedule.run_pending()
