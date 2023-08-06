__all__ = ['date_check']
def _leap_year(year: int) -> bool:
    if year%4 == 0:
        return True
    else:
        return False


def date_check (date):
    list_31_days = ['01', '03', '05', '07', '08', '10', '12']
    list_30_days = ['04', '06', '09', '11']
    list_28_days = ['02']
    day, month, year = date.split('.')
    if month in list_31_days and 0 < int(day) < 32 and 0< int(year) < 10000:
        return True
    elif month in list_30_days and 0 < int(day) < 31 and 0 < int(year) < 10000:
        return True
    elif month in list_28_days and 0 < int(day) < 30 and 0 < int(year) < 10000 and _leap_year(int(year)):
        return True
    elif month in list_28_days and 0 < int(day) < 29 and 0 < int(year) < 10000 and not _leap_year(int(year)):
        return True
    return False