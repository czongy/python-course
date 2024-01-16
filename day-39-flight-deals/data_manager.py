import requests
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from google.oauth2 import service_account


class DataManager:
    def __init__(self):
        load_dotenv()
        # self.headers = {
        #     "Authorization": f"Basic {os.environ['BASIC_AUTH']}"
        # }
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'keys.json'

        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        self.SAMPLE_SPREADSHEET_ID = os.environ['GOOGLE_SID']
        self.service = build('sheets', 'v4', credentials=credentials)
        self.sheet = self.service.spreadsheets()

    def get_request(self, cell_range):
        # get_endpoint = os.environ["SHEETY_ENDPOINT"]
        # get_res = requests.get(url=get_endpoint, headers=self.headers)
        # get_res.raise_for_status()
        # return get_res.json()
        result = self.sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                    range=cell_range).execute()
        return result.get('values', [])[1:len(result['values'])]

    def update_request(self, cell_range, body):
        # print(objectid)
        # put_endpoint = os.environ["SHEETY_ENDPOINT"] + f"/{objectid}"
        # put_params = params
        # put_res = requests.put(url=put_endpoint, json=put_params, headers=self.headers)
        # put_res.raise_for_status()
        result = self.sheet.values().update(
            spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
            range=cell_range,
            valueInputOption="USER_ENTERED",
            body=body
        ).execute()