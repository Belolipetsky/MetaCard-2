# utils/database.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_sheet():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    # Открываем Google Таблицу по названию (создайте её заранее)
    sheet = client.open("MetacardBotUsers").sheet1
    return sheet

def add_user(user_id, username, name, phone, date_reg):
    sheet = get_sheet()
    sheet.append_row([user_id, username, name, phone, "0", date_reg, ""])
