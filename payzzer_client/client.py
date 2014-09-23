import base64
import datetime
import requests
import requests.exceptions
import time
from payzzer_client.accounts import Accounts
from payzzer_client.boards import Boards


class Client(object):
    def __init__(self, username, password, allow_insecure=False):
        self._api_url = 'https://api.payzzer.com/v2'
        self._allow_insecure = allow_insecure
        b64username = base64.encodestring(username).strip()
        b64password = base64.encodestring(password).strip()
        self._api_token = '{0}:{1}'.format(b64username, b64password)

    def _build_url(self, endpoint):
        if not endpoint.startswith('/'):
            endpoint = '/{0}'.format(endpoint)
        return '{0}{1}'.format(self._api_url, endpoint)

    def _request(self, endpoint, data=None, **kwargs):
        if data is None:
            data = {}
        data.update({
            'auth_token': self._api_token,
        })
        url = self._build_url(endpoint)
        try:
            return requests.post(url, data=data, **kwargs)
        except requests.exceptions.SSLError, e:
            if self._allow_insecure:
                return requests.post(url, data=data, verify=False)
            raise e

    def _prepare_date(self, date, is_date_from=True):
        if isinstance(date, int):
            return date

        if is_date_from:
            if date is None:
                date = datetime.datetime.today().replace(hour=0, minute=0, second=0)
            if isinstance(date, datetime.date):
                date = datetime.datetime.combine(date, datetime.time(0, 0, 0))
        else:
            if date is None:
                date = datetime.datetime.today().replace(hour=23, minute=59, second=59)
            if isinstance(date, datetime.date):
                date = datetime.datetime.combine(date, datetime.time(23, 59, 59))
        return time.mktime(date.timetuple())

    def get_boards(self):
        boards = self._request('/setup/get_boards')
        return Boards(boards.json())

    def get_accounts(self, board, page=0):
        accounts = self._request('/board/{0}/get_accounts_browse_report/{1}'.format(board.id, page))
        # merge accounts_with_summaries_list with data from next_page
        return Accounts(accounts.json())

    def get_total_summary_report(self, board, page=0, date_from=None, date_to=None):
        data = {
            'date_range_from': self._prepare_date(date_from, True),
            'date_range_to': self._prepare_date(date_to, False),
        }
        report = {'has_next_page': True, 'operation_list': []}
        while report.get('has_next_page'):
            operation_list = report['operation_list']
            new_report = self._request('/board/{0}/get_total_summary_report/{1}'.format(board.id, page), data=data).json()
            new_report.get('operation_list', []).extend(operation_list)
            report.update(new_report)
            page += 1
        return report
