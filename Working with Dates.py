from datetime import datetime

date_str = "2023-08-03"
date_obj = datetime.strptime(date_str, "%Y-%m-%d")
print("Date:", date_obj)
