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
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'rtt': '350',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
            'accept': 'text/html,*/*',
            'x-requested-with': 'XMLHttpRequest',
            'downlink': '1.45',
            'ect': '3g',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.amazon.com/s?k=baby+monitor&sprefix=bab%2Caps%2C297&ref=nb_sb_ss_ts-doa-p_1_3',
            'accept-language': 'zh-CN,zh;q=0.9',
            # 'cookie': 'session-id=133-9242345-7882433; i18n-prefs=USD; ubid-main=131-6777554-5563620; lc-main=en_US; session-id-time=2082787201l; skin=noskin; session-token=Ndof0MdqXo/1NNBgx5tLtfZJ/yveZAFOn4k//g/miRTIbTDsg5AfL1cmsHC3guDLQjbrRGalJfBX+1X/LFv4F5PtKPri29zKCHCysytIpt4OPCIoP5h61bS95YmW8ZQRjXTXwQ/qCk/LyTaJjUiF6oUNx5PsccRaL0W/ymnAupLvotXnrOz4amHldjk8lAjH; csm-hit=tb:s-KZT0PF2SNSNDBR0TH1ZY|1647587549510&t:1647587550711&adb:adblk_no',
            'cookie': 'session-id=147-1122365-4740253; session-id-time=2082787201l; i18n-prefs=USD; skin=noskin; ubid-main=135-6782372-6842461; lc-main=en_US; session-token=RbFJddhjZUa5vox+FlUJE/xOprFZTI8ujE1A0ij61C0R3f7//29BPgC+TmrFSSAxxO30Vn9d1998Ct+PY9PzcKC6Qnu3iFShNkxqG+ua0IUaqcZ83atQFfrzD0sOsMP3c8kXJjrSobpR7rjz4Y3RWk6WMeGXegcnVu307RJia5guC4DOoRSvieN9LdZMRgW0; csm-hit=tb:s-7T3ZD5V0KA63JS40D8YH|1645690257257&t:1645690258208&adb:adblk_no',
        }
    else:
        pass
    return headers