import hashlib,time

def user_sign(request):
    client_time = request.POST.get('time','')
    client_sign = request.POST.get('sign','')
    if client_time =='' or client_sign == '':
        return "sign null"

    #服务器时间
    now_time = time.time()
    server_time = str(now_time).split('.')[0]
    #获取时间差
    time_dif=int(server_time)-int(client_time)
    if time_dif>=60:
        return "timeout"

    #签名检查
    md5 = hashlib.md5()
    sign_str = client_time + "&mengxue"
    sign_bytes_utf8 = sign_str.encode(encoding = 'utf-8')
    md5.update(sign_bytes_utf8)
    server_sign = md5.hexdigest()
    if server_sign!=client_sign:
        return "sign error."
    else:
        return "sign right."
