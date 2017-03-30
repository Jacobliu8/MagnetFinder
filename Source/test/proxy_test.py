import socket
from unittest import TestCase
from unittest import skip
from urllib import request
from urllib.request import Request

from app.Models import ProxyServer
from app.Proxy import proxy_test, get_proxy_list, proxy_setting


class TestProxy(TestCase):
    def test_no_proxy(self):
        result = proxy_test()
        self.assertEqual(result, True, "no proxy, can't visit google")

    @skip("demonstrating skipping")
    def test_setting_proxy(self):
        get_proxy_list()

    def test_proxy(self):
        result = proxy_setting([self.proxy])
        self.assertEqual(result, True, "set proxy, can visit google")

    def setUp(self):
        self.proxy = ProxyServer(proxy_address="http://10.222.124.59:23/", speed='100kbit')

    def test_machine_host_getadd_is_ok(self):
        print(socket.getaddrinfo('10.222.124.59', 23))

    def test_proxy_is_ok(self):
        proxy = "http://10.222.124.59:808/"
        proxy_support = request.ProxyHandler({'http': proxy})
        # Build opener with ProxyHandler object
        opener = request.build_opener(proxy_support)
        # Install opener to request
        request.install_opener(opener)
        # Open url
        rs = Request('http://www.google.com', headers={
            'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
        r = request.urlopen(rs, timeout=1000)
        print(r.getcode())
        self.assertEqual(r.getcode(), 200, 'pass testing')
