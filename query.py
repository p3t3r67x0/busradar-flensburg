from fake_useragent import UserAgent
from urllib.parse import urlparse
from httpx import AsyncClient

#from main import app

ua = UserAgent()


async def request_cookie(url_base):
    async with AsyncClient(app=app) as ac:
        r = ac.get(url_base, timeout=20)

        if r.status_code == 200:
            cookie = r.headers['set-cookie'].split(';')

        if len(cookie) >= 0:
            sec_id = cookie[0].split('=')[1]

            return sec_id


async def request_data(url_base, url_detail, cookie):
    domain = urlparse(url_base).netloc

    cookies = httpx.Cookies()
    cookies.set('secId', cookie, domain=domain)

    headers = {'user-agent': ua.random, 'referer': url_base}

    async with AsyncClient(app=app) as ac:
        r = ac.get(url_detail, headers=headers, cookies=cookies)

        return r.json()
