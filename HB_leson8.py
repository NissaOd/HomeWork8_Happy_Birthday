from datetime import datetime, timedelta

birthday_dudes = [{'name': 'Nort', 'birthday': '1996-06-18'},
                {'name': 'Basi', 'birthday': '2010-06-22'},
                {'name': 'Nik', 'birthday': '2003-06-11'},
                {'name': 'Mikel', 'birthday': '1999-06-14'},
                {'name': 'Boomer', 'birthday': '1924-06-22'},
                {'name': 'Sloo', 'birthday': '1809-06-24'},
                {'name': 'Cok', 'birthday': '1946-06-23'},
                {'name': 'Bieva', 'birthday': '1992-06-31'}]


def birthdays_next_week(users: list) -> None:
	checked_dudes = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
	today_is = datetime.now().date()
	day_of_week = today_is.weekday()
	next_monday = (today_is + timedelta(days=7 - day_of_week))
	next_friday = (today_is + timedelta(days=11 - day_of_week))
	last_saturday = (next_monday - timedelta(days=2))

	for dude in users:
		get_dude_date = dude['birthday'].split('-')
		dude_date = datetime(year=today_is.year, month=int(get_dude_date[1]), day=int(get_dude_date[2])).date()
		if last_saturday <= dude_date < next_monday:
			checked_dudes['Monday'].append(dude['name'])
		elif next_monday <= dude_date <= next_friday:
			checked_dudes[dude_date.strftime('%A')].append(dude['name'])
	for day, celebrators in checked_dudes.items():
		if not celebrators:
			continue
		else:
			str_names = ', '.join(celebrators)
			print(f"{day}: {str_names}.")


birthdays_next_week(birthday_dudes)
