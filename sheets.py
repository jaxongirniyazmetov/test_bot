import os
import json
import base64
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_sheet():
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    b64_creds = os.getenv("GOOGLE_CREDS_B64")

    if not b64_creds:
        raise Exception("GOOGLE_CREDS_B64 environment variable not found.")

    creds_dict = json.loads(base64.b64decode(b64_creds))
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    sheet_name = os.getenv('GOOGLE_SHEET_NAME')
    sheet = client.open(sheet_name).sheet1
    return sheet
