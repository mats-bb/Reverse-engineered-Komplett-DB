import datetime
import holidays
import pandas as pd
import os

os.sys.path.append('scripts')
from util.utils import save_to_json

YEAR = 2023
no_holidays = holidays.country_holidays('NO')
DATA_GEN_PATH = r"data\data_gen"


def get_dates_in_year(year):

    start_date = pd.Timestamp(year, 1, 1)
    end_date = pd.Timestamp(year, 12, 31)
    all_dates = pd.date_range(start=start_date, end=end_date)

    return [date.date() for date in all_dates]


def get_last_date_by_month(year):

    last_date_by_month = []

    for month in range(1, 13): 

        if month == 12:
            last_day_of_month = datetime.date(year, month, 31)
        else:
            last_day_of_month = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
        

        last_date_by_month.append(last_day_of_month)

    return last_date_by_month


def get_day_number_of_week(date):

    return date.weekday() + 1


def get_day_number_of_month(date):

    day_number = date.day
    return day_number


def get_day_number_of_year(date):
   
    return int(date.strftime("%j"))

def get_month_number_of_year(date):

    return date.month

def get_week_number_of_year(date):

    _, iso_week, _ = date.isocalendar()

    return iso_week


def get_quarter_of_year(date):

    month_to_quarter = {
        1: 1, 2: 1, 3: 1,
        4: 2, 5: 2, 6: 2,
        7: 3, 8: 3, 9: 3,
        10: 4, 11: 4, 12: 4
    }

    month = date.month
    
    return month_to_quarter[month]


def get_day_name(date):

    return date.strftime("%A")
    

def get_month_name(date):

    return date.strftime("%B")


def get_year(date):

    return date.year


def generate_date_list(year):
    
    date_rows = []
    all_dates = get_dates_in_year(year)
    
    for date_ in all_dates:
        d = {}

        d["date"] = str(date_)
        d["day_of_week"] = get_day_number_of_week(date_)
        d["day_of_month"] = get_day_number_of_month(date_)
        d["day_of_year"] = get_day_number_of_year(date_)
        d["week_number"] = get_week_number_of_year(date_)
        d["year"] = get_year(date_)
        d["name_of_day"] = get_day_name(date_)
        d["name_of_month"] = get_month_name(date_)
        d["month_number"] = get_month_number_of_year(date_)
        d["quarter"] = get_quarter_of_year(date_)
        d["full_date_description"] = f"{get_month_name(date_)} {get_day_number_of_month(date_)}, {get_year(date_)}"

        if date_ in get_last_date_by_month(year):
            d["month_end_flag"] = "Month end"
        else:
            d["month_end_flag"] = "Not month end"

        if get_day_name(date_) in ["Saturday", "Sunday"]:
            d["weekday_flag"] = "Weekend"
        else:
            d["weekday_flag"] = "Weekday"

        if date_ in no_holidays:
            d["holiday_flag"] = "Holiday"
        else:
            d["holiday_flag"] = "Not holiday"

        date_rows.append(d)

    return date_rows

def generate_date_data(year):

    date_rows = generate_date_list(year)
    save_to_json(DATA_GEN_PATH, f"{YEAR}_date_data.json", date_rows)

generate_date_data(YEAR)