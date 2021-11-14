
# https://docs.github.com/cn/rest/guides/getting-started-with-the-rest-api


def pretty_print(jsons):
    for key in jsons:
        print(key, "= ", jsons[key])

import requests
url = 'https://api.github.com/users/defunkt'

query_data = {}
my_header = {}

r = requests.get(url, params=query_data, headers=my_header)
pretty_print(r.headers)
# pretty_print(r.json())

""" 
响应头
Server =  GitHub.com
Date =  Mon, 18 Oct 2021 03:22:29 GMT
Content-Type =  application/json; charset=utf-8  #! 响应头为 application/json;
Cache-Control =  public, max-age=60, s-maxage=60
Vary =  Accept, Accept-Encoding, Accept, X-Requested-With
ETag =  W/"6638bf1566d1423a46ca6a4bec9057a2e841bfa61da1346b6a6aa350ef7aa443"
Last-Modified =  Thu, 29 Jul 2021 11:10:23 GMT
X-GitHub-Media-Type =  github.v3; format=json #! 任何以 X- 开头的标头都是自定义标头，不包含在 HTTP 规范中
Access-Control-Expose-Headers =  ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, Deprecation, Sunset
Access-Control-Allow-Origin =  *
Strict-Transport-Security =  max-age=31536000; includeSubdomains; preload
X-Frame-Options =  deny
X-Content-Type-Options =  nosniff
X-XSS-Protection =  0
Referrer-Policy =  origin-when-cross-origin, strict-origin-when-cross-origin
Content-Security-Policy =  default-src 'none'
Content-Encoding =  gzip
X-RateLimit-Limit =  60 #! 这对标头指示在滚动时间段（通常为一小时）内一个客户端可以发出多少个请求，
X-RateLimit-Remaining =  47 #! 以及该客户端已使用多少个此类请求
X-RateLimit-Reset =  1634529930
X-RateLimit-Resource =  core
X-RateLimit-Used =  13
Accept-Ranges =  bytes
Content-Length =  482
X-GitHub-Request-Id =  DAFA:5F99:22B489F:24B0F81:616CE889
"""

