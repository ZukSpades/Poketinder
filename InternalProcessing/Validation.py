import datetime


def validate_date(dd_mm):
    try:
        datetime.datetime.strptime(dd_mm, "%d/%m")
        return True
    except ValueError:
        print("ERROR: Invalid date format")
        return False

