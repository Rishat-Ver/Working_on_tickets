from datetime import date


MONTHS_RU = {
    "January": "января", "February": "февраля", "March": "марта", "April": "апреля",
    "May": "мая", "June": "июня", "July": "июля", "August": "августа",
    "September": "сентября", "October": "октября", "November": "ноября", "December": "декабря"
}

def format_date(date: date) -> str:
    day = date.strftime("%d")
    month = date.strftime("%B")
    return f"{day} {MONTHS_RU[month]}"