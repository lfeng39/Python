def Headers(site_brand):
    if 'taobao' == site_brand:
        headers = {
            'authority': 's.taobao.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'sec-fetch-user': '?1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'referer': 'https://www.taobao.com/?spm=a230r.1.0.0.18434f0fZ0XBOG',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
            'cookie': 'thw=cn; v=0; cna=ba/BFhNadHgCARsSEUxw1LSm; cookie2=1e442ba61c5425457fbebe075e26de5f; t=add1e52914eb6b2016ee6d22120993af; _tb_token_=71ee7533e5de4; _samesite_flag_=true; uc3=lg2=UtASsssmOIJ0bQ%3D%3D&id2=UoLfdCpv5t6I&nk2=0%2BFaWwjTPm8%3D&vt3=F8dBxdsXGDvOYjaB7kg%3D; csg=6c8ad4c6; lgc=%5Cu554A%5Cu54E9%5Cu8DEF%5Cu8FC7; dnk=%5Cu554A%5Cu54E9%5Cu8DEF%5Cu8FC7; skt=c149b9211e8c32ee; existShop=MTU4MDkxMjY2MA%3D%3D; uc4=id4=0%40UOrptUgWFjW%2BSDCzGvbpHBpU%2BNI%3D&nk4=0%400VoIkNFbMLOWIlARu3ield73yQ%3D%3D; tracknick=%5Cu554A%5Cu54E9%5Cu8DEF%5Cu8FC7; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; enc=WmrrgcHnzMECUXK5Bd0pEoDu5afsV9a894wVWiyPk4vBa6PjkJJ2om7H9JCVtpwO5%2B0QWiuQzvoXN3IKdiHeaA%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _m_h5_tk=3368371eacfccc8f82862a86dd7b8dfd_1582826745984; _m_h5_tk_enc=ce0978d905508de861ab72e478d76a9a; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=UtASsssmfaCONGki4KTH3w%3D%3D&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie14=UoTUOLr0PocV7g%3D%3D&cart_m=0&tag=10&lng=zh_CN; mt=ci=-1_0; isg=BD09yBmkPwUVjZtnjAo1pyidTJk32nEskr7nYP-CeRTDNl1oxyqB_Atk5GpwrYnk; l=dBg7ckIgQhWWcsvkBOCanurza77OSIRYYuPzaNbMi_5BA6T6xJ7OoRsl8F96VjWfT2LB4Tn8Nrv9-etuZ7DmndK-g3fPaxDc.; JSESSIONID=37DFFF827495F13075CA01C510DE2A11'
        }
    elif 'zhihu' == site_brand:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'
        }
    elif 'amazon' == site_brand:
         headers = {
            'authority': 'www.amazon.com',
            'method': 'GET',
            'path': '/s?k=led+outdoor&ref=nb_sb_noss_2',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'cache-control': 'max-age=0',
            'cookie': 'session-id=142-0742346-9197407; ubid-main=133-7610726-3999729; x-main="4kcZZToPabr9kasOAP@fUF?gnBEFaM5G"; at-main=Atza|IwEBIHakK7hcNKZ8SnOHIESyAbGkJm881U1DzVVSDUsQtW4m9IBGj3eRSHyCTielSYV5LFEZgM52WDU-iPqlVlfoyFH50lsV1lcHWTw-Lx0TKAQtyZ6lNtbPPeR61oLvW9lrKdJhmGKMyb_q4CM05NPDtIWwNwNlfDHJlWJiyMvDVj_ei_0q8rIGvCsv0iSo5UecLdunGbhQcvp1cCOQl9JecTQY; sess-at-main="QG3NzTZK9Oq/AnB9D2p9/kHvrdx2o/40aMhb9ncESI0="; sst-main=Sst1|PQFB0bUIS1fXsMsV2S59DyOUCW5nwqhMy78gX87n0biokDXU_fAKXLMZr9qeysTcdSa7CZu1fReugmLsmJSOEcuOW6rifXNp3uuO-9JwzfegBoGOwKCMPvM2DVFb9vKeL8qsOvwdE1CF1nsDPO7C67FLmrV3ReHONyDcqc58rITDQebzhrYOXYIRj-Lx4memd-sVbkKPZGLrw7pE7Flqpoodv66BW8DlE1lWRyZv5DvGAIivV_7JHGD3hJCJM_WYWjmiQJfLy4fx_c_iVECH2s1IHTppiitYq8kwq54gZUOfmO4; lc-main=en_US; session-id-time=2082787201l; csd-key=eyJ3YXNtVGVzdGVkIjp0cnVlLCJ3YXNtQ29tcGF0aWJsZSI6dHJ1ZSwid2ViQ3J5cHRvVGVzdGVkIjpmYWxzZSwidiI6MSwia2lkIjoiYjVjNzZlIiwia2V5IjoiVDk4S251VHI2aWMvdE44OGVYcEhsVXBOdjM1dEdsdjR2UEJZOVpNL052SjVmRzNsMEV4RjlzdStQcU9LZ1dTQ1owSTF4bWQ3amJXY1RUSE55OWJleDNaMGRYSG93eW5kRk1aaDF2c2Zpc0ZZTmdFeXllZ2lybktCNUd4Y0REdUF3eEhiUit5RytoU1QvSnZvTDh5SnRiT1JJVDBqanJtK2N3blFGbGpXTHZRYnhjSkZiNWJ6MTdJL0ZZUmRockZ3ejI3Z20wVGVwRFVmNHRGc1A1K3RZbFVSTHp4ckNQWHBCMm8xQ0RqTVIrK0l0dVNhelR6Q2FyVEl0UmJUdE0yZ2xVUGtqYU44UDRoUEl2NzFQT25QVWVBQWpMSWRkMURrSXlJb0FXZlBKalByaE9pOXV4Q0RVSjVYVUdrVzJtY0J6cFJHMEtydTg0R1QyZEs4R2JuQzNBPT0ifQ==; session-token="iYYndurGfOfXDEnCsH9uwyeX7b0S+ZABM97JVwXRTvNCEaqpBjoPjB5SmgoBsH8RZRpnTyH3FR3j0vVnX2Jlm96lE8f/iksXfejUBpTe5aVQQ6iCjhz/i/rSjgLeZ2aG8khFYc6fXz/7BaqN2qGUsVjZ+NDN0VmQXQHey4LkWKp58hQbDH6JW9jFkhDwgPC7hfZhQDMsUMH4ZaycRAq2qYLsqy5iTaJW5pUsXmBnZgaCx2DW3EkX9TEmOtVijRRhEt6ML6qD0/+9mVgz1Y26ig=="; csm-hit=adb:adblk_no&t:1608966225254&tb:FCA9V8C9Y22B2CENQZCH+s-QNQR62MA46RMT9NTY65E|1608966225254',
        }
    elif 'ins' == site_brand:
        headers = {
            "Origin": "https://www.instagram.com/",
            "Referer": "https://www.instagram.com/_8_jjini/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/58.0.3029.110 Safari/537.36",
            "Host": "www.instagram.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "accept-encoding": "gzip, deflate, sdch, br",
            "accept-language": "zh-CN,zh;q=0.8",
            "X-Instragram-AJAX": "1",
            "X-Requested-With": "XMLHttpRequest",
            "Upgrade-Insecure-Requests": "1",
        }
        headers = {
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
    else:
        pass
    return headers