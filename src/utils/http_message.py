class HTTPMessage:
    def __init__(self, url, headers=None, params=None):
        self.url = url
        self.headers = headers or {}
        self.params = params or {}