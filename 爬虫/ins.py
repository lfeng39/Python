# -*- coding:utf-8 -*-
import requests
import re
import json
import urllib.parse
import hashlib
import sys

header = {
            ':authority': 'i.instagram.com',
            ':method': 'GET',
            ':path': '/api/v1/collections/list/?collection_types=%5B%22ALL_MEDIA_AUTO_COLLECTION%22%2C%22MEDIA%22%5D&include_public_only=0&get_cover_media_lists=true&max_id=',
            ':scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'cookie': 'mid=YPkNSQAEAAFUQdFTHy1rpV81LURf; ig_did=0ACC4A71-78EE-4636-AE0C-5AFA776B6D20; ig_nrcb=1; csrftoken=16x9jauJXvAit4gHseyJlaJnK8NZqRDw; ds_user_id=207843075; sessionid=207843075%3AwdSgrNlyUlgnQ6%3A7; shbid="6728\054207843075\0541659507754:01f79be1bd3fd9c0d1f23626f283aa868647fc2d2ff7689f32db29c0485888363a51ba2f"; shbts="1627971754\054207843075\0541659507754:01f7a70d7caa296323c76e4006912c65aa26aa227b3a4d2c892401b2af22cd3ce8f815a8"; rur="PRN\054207843075\0541659510585:01f70db2cbb7a1c8767372303422250e1c434c2cb9f8c62848619b77f2bf5896a9a7968f”',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '”Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92”',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'x-asbd-id': '437806',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR0NEI82xTw3LYlloRKoSpsMXKNkz2l3otrFWcewmHkbaLwx'

            # 'set-cookie': 'rur=PRN; Domain=.instagram.com; HttpOnly; Path=/; Secure',
            # 'set-cookie': 'ds_user_id=11859524403; Domain=.instagram.com; expires=Mon, 15-Jul-2019 09:22:48 GMT; Max-Age=7776000; Path=/; Secure',
            # 'set-cookie': 'urlgen="{\"45.63.123.251\": 20473}:1hGKIi:7bh3mEau4gMVhrzWRTvtjs9hJ2Q"; Domain=.instagram.com; HttpOnly; Path=/; Secure',
            # 'set-cookie': 'csrftoken=Or4nQ1T3xidf6CYyTE7vueF46B73JmAd; Domain=.instagram.com; expires=Tue, 14-Apr-2020 09:22:48 GMT; Max-Age=31449600; Path=/; Secure'
        }

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

BASE_URL = 'https://www.instagram.com'
ACCOUNT_MEDIAS = "http://www.instagram.com/graphql/query/?query_hash=42323d64886122307be10013ad2dcc44&variables=%s"
ACCOUNT_PAGE = 'https://www.instagram.com/%s'

proxies = {
    'http': 'http://34.92.250.101:39390',
    'https': 'http://34.92.250.101:39390',
}


# 一次设置proxy的办法，将它设置在一次session会话中，这样就不用每次都在调用requests的时候指定proxies参数了
# s = requests.session()
# s.proxies = {'http': '121.193.143.249:80'}

def get_shared_data(html=''):
    """get window._sharedData from page,return the dict loaded by window._sharedData str
    """
    if html:
        target_text = html
    else:
        header = generate_header()
        response = requests.get(BASE_URL, proxies=proxies, headers=header)
        target_text = response.text
    regx = r"\s*.*\s*<script.*?>.*_sharedData\s*=\s*(.*?);<\/script>"
    match_result = re.match(regx, target_text, re.S)
    data = json.loads(match_result.group(1))

    return data

# def get_rhx_gis():
#     """get the rhx_gis value from sharedData
#     """
#     share_data = get_shared_data()
#     return share_data['rhx_gis']

def get_account(user_name):
    """get the account info by username
    :param user_name:
    :return:
    """
    url = get_account_link(user_name)
    header = generate_header()
    response = requests.get(url, headers=header, proxies=proxies)
    data = get_shared_data(response.text)
    account = resolve_account_data(data)
    return account

def get_media_by_user_id(user_id, count=50, max_id=''):
    """get media info by user id
    :param id:
    :param count:
    :param max_id:
    :return:
    """
    index = 0
    medias = []
    has_next_page = True
    while index <= count and has_next_page:
        varibles = json.dumps({
            'id': str(user_id),
            'first': count,
            'after': str(max_id)
        }, separators=(',', ':'))  # 不指定separators的话key:value的:后会默认有空格，因为其默认separators为(', ', ': ')
        url = get_account_media_link(varibles)
        header = generate_header()
        response = requests.get(url, headers=header, proxies=proxies)

        media_json_data = json.loads(response.text)
        media_raw_data = media_json_data['data']['user']['edge_owner_to_timeline_media']['edges']

        if not media_raw_data:
            return medias

        for item in media_raw_data:
            if index == count:
                return medias
            index += 1
            medias.append(general_resolve_media(item['node']))
        max_id = media_json_data['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
        has_next_page = media_json_data['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
    return medias

def get_media_by_url(media_url):
    response = requests.get(get_media_url(media_url), proxies=proxies, headers=generate_header())
    media_json = json.loads(response.text)
    return general_resolve_media(media_json['graphql']['shortcode_media'])

def get_account_media_link(varibles):
    return ACCOUNT_MEDIAS % urllib.parse.quote(varibles)

def get_account_link(user_name):
    return ACCOUNT_PAGE % user_name

def get_media_url(media_url):
    return media_url.rstrip('/') + '/?__a=1'

# def generate_instagram_gis(varibles):
#     rhx_gis = get_rhx_gis()
#     gis_token = rhx_gis + ':' + varibles
#     x_instagram_token = hashlib.md5(gis_token.encode('utf-8')).hexdigest()
#     return x_instagram_token

def generate_header(gis_token=''):
    # todo: if have session, add the session key:value to header
    header = {
        'user-agent': USER_AGENT,
    }
    if gis_token:
        header['x-instagram-gis'] = gis_token
    return header

def general_resolve_media(media):
    res = {
        'id': media['id'],
        'type': media['__typename'][5:].lower(),
        'content': media['edge_media_to_caption']['edges'][0]['node']['text'],
        'title': 'title' in media and media['title'] or '',
        'shortcode': media['shortcode'],
        'preview_url': BASE_URL + '/p/' + media['shortcode'],
        'comments_count': media['edge_media_to_comment']['count'],
        'likes_count': media['edge_media_preview_like']['count'],
        'dimensions': 'dimensions' in media and media['dimensions'] or {},
        'display_url': media['display_url'],
        'owner_id': media['owner']['id'],
        'thumbnail_src': 'thumbnail_src' in media and media['thumbnail_src'] or '',
        'is_video': media['is_video'],
        'video_url': 'video_url' in media and media['video_url'] or ''
    }
    return res

def resolve_account_data(account_data):
    account = {
        'country': account_data['country_code'],
        'language': account_data['language_code'],
        'biography': account_data['entry_data']['ProfilePage'][0]['graphql']['user']['biography'],
        'followers_count': account_data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']['count'],
        'follow_count': account_data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_follow']['count'],
        'full_name': account_data['entry_data']['ProfilePage'][0]['graphql']['user']['full_name'],
        'id': account_data['entry_data']['ProfilePage'][0]['graphql']['user']['id'],
        'is_private': account_data['entry_data']['ProfilePage'][0]['graphql']['user']['is_private'],
        'is_verified': account_data['entry_data']['ProfilePage'][0]['graphql']['user']['is_verified'],
        'profile_pic_url': account_data['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url_hd'],
        'username': account_data['entry_data']['ProfilePage'][0]['graphql']['user']['username'],
    }
    return account

account = get_account('shaq')

result = get_media_by_user_id(account['id'], 56)

media = get_media_by_url('https://www.instagram.com/p/Bw3-Q2XhDMf/')

print(len(result))
print(result)