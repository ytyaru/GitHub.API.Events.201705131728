#!python3
#encoding: utf-8
import requests
import datetime
import json
username = 'some_username'
token = 'some_access_token'
fine_name_min = '{0}_events_{1:%Y%m%d%H%M%S}.min.json'.format(username, datetime.datetime.now())
fine_name_format = '{0}_events_{1:%Y%m%d%H%M%S}.json'.format(username, datetime.datetime.now())
# https://developer.github.com/v3/#root-endpoint
endpoint_root = 'https://api.github.com'
# https://developer.github.com/v3/activity/events/#list-events-performed-by-a-user
endpoint_user_events = '/users/{username}/events'.format(username=username)
reqp = {
    'headers': {
        'User-Agent': username,                     # https://developer.github.com/v3/#user-agent-required
        'Accept': 'application/vnd.github.v3+json', # https://developer.github.com/v3/#current-version
        'Time-Zone': 'Asia/Tokyo',                  # https://developer.github.com/v3/#timezones
        'Authorization': 'token ' + token           # https://developer.github.com/v3/#oauth2-token-sent-in-a-header
    }
}
res = requests.get(endpoint_root + endpoint_user_events, **reqp)
print(res.text)
with open(fine_name_min, 'w') as f:
    f.write(res.text)
# with open()... 構文では空ファイルになってしまう
f = open(fine_name_format, "w")
json.dump(json.loads(res.text), f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
f.close()

