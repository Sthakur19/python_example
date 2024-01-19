class CookieJar(object):
    def __init__(self):
        self._is_open = False

    def take(self):
        if not self._is_open:
            raise ValueError("Cookie jar is closed")
        return "Cookie"

    def open_jar(self):
        self._is_open = True

    def close_jar(self):
        self._is_open = False

    def is_open(self):
        return self._is_open

class SelfClosing:
    def __init__(self, cookie_jar):
        self.cookie_jar = cookie_jar

    def __enter__(self):
        if not self.cookie_jar.is_open():
            self.cookie_jar.open_jar()
        return self.cookie_jar

    def __exit__(self, exc_type, exc_value, traceback):
        self.cookie_jar.close_jar()


cookie_jar = CookieJar()

with SelfClosing(cookie_jar) as jar:
    cookie = jar.take()

print(cookie_jar.is_open())  
