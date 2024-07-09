import requests


class HTTPClient:
    def __init__(self):
        pass

    def get(self, url):
        """
        :param url: url endpoint to send GET request to
        :return: respond object
        """
        return requests.get(url)

    def post(self, url, data):
        """
        :param url: url endpoint to send POST request to
        :return: respond object
        """
        return requests.post(url, data=data)