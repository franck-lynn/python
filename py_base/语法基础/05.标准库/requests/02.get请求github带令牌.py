# https://docs.github.com/cn/rest/guides/getting-started-with-the-rest-api
# https://blog.csdn.net/weixin_30386713/article/details/98981927
def pretty_print(jsons):
    for key in jsons:
        print(key, "= ", jsons[key])



import requests
# 读取环境变量文件
import os
from dotenv import load_dotenv
 

#! 指定配置文件地址, 必须提供load_dotenv的完整路径
# BASEDIR = os.path.abspath(os.path.dirname(__file__))
BASEDIR = "F:/node/config"
load_dotenv(os.path.join(BASEDIR, '.env'))
token = os.getenv('TOKEN')


# url = 'https://api.github.com/users/franck-lynn'
# 列出自己的仓库信息, 需要口令
url = 'https://api.github.com/users/franck-lynn/repos'
query_data = {}
my_header = {
    "Authorization": "token " + token
}

r = requests.get(url, params=query_data, headers=my_header)
# pretty_print(r.headers)
# pretty_print(r.json())
print(r.json())

# 响应头


""" 
    Server =  GitHub.com
    Date =  Mon, 18 Oct 2021 03:46:49 GMT
    Content-Type =  application/json; charset=utf-8
    Transfer-Encoding =  chunked
    Cache-Control =  private, max-age=60, s-maxage=60
    Vary =  Accept, Authorization, Cookie, X-GitHub-OTP, Accept-Encoding, Accept, X-Requested-With
    ETag =  W/"d5fb42104d260dfd351cf53094d1b0fac77d1930780c8824eaaf0155034debc9"
    Last-Modified =  Fri, 15 Oct 2021 16:34:52 GMT
    X-OAuth-Scopes =  admin:enterprise, admin:org, delete:packages, delete_repo, notifications, repo, user, workflow, write:discussion, write:packages
    X-Accepted-OAuth-Scopes =  
    X-GitHub-Media-Type =  github.v3; format=json
    X-RateLimit-Limit =  5000 #! 可以看到, 访问次数增加了每分钟 5000次
    X-RateLimit-Remaining =  4999
    X-RateLimit-Reset =  1634532409
    X-RateLimit-Used =  1
    X-RateLimit-Resource =  core
    Access-Control-Expose-Headers =  ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, Deprecation, Sunset
    Access-Control-Allow-Origin =  *
    Strict-Transport-Security =  max-age=31536000; includeSubdomains; preload
    X-Frame-Options =  deny
    X-Content-Type-Options =  nosniff
    X-XSS-Protection =  0
    Referrer-Policy =  origin-when-cross-origin, strict-origin-when-cross-origin
    Content-Security-Policy =  default-src 'none'
    Content-Encoding =  gzip
    X-GitHub-Request-Id =  F673:48E0:257BBE:2D698F:616CEE29
"""
# 获取用户的个人资料
""" 
    login =  franck-lynn
    id =  16490756
    node_id =  MDQ6VXNlcjE2NDkwNzU2
    avatar_url =  https://avatars.githubusercontent.com/u/16490756?v=4
    gravatar_id =  
    url =  https://api.github.com/users/franck-lynn
    html_url =  https://github.com/franck-lynn
    followers_url =  https://api.github.com/users/franck-lynn/followers
    following_url =  https://api.github.com/users/franck-lynn/following{/other_user}
    gists_url =  https://api.github.com/users/franck-lynn/gists{/gist_id}
    starred_url =  https://api.github.com/users/franck-lynn/starred{/owner}{/repo}
    subscriptions_url =  https://api.github.com/users/franck-lynn/subscriptions
    organizations_url =  https://api.github.com/users/franck-lynn/orgs
    repos_url =  https://api.github.com/users/franck-lynn/repos
    events_url =  https://api.github.com/users/franck-lynn/events{/privacy}
    received_events_url =  https://api.github.com/users/franck-lynn/received_events
    type =  User
    site_admin =  False
    name =  None
    company =  None
    blog =  
    location =  None
    email =  None
    hireable =  None
    bio =  None
    twitter_username =  None
    public_repos =  8
    public_gists =  0
    followers =  0
    following =  0
    created_at =  2015-12-30T15:22:57Z
    updated_at =  2021-10-15T16:34:52Z
    private_gists =  0
    total_private_repos =  0
    owned_private_repos =  0
    disk_usage =  72861
    collaborators =  0
    two_factor_authentication =  False
    plan =  {'name': 'free', 'space': 976562499, 'collaborators': 0, 'private_repos': 10000}
"""