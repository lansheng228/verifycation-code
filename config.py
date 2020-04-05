authcode_font = "static/fonts/wqy-microhei.ttc"

# 使用方式举例，在django的view文件中使用：

def verify_code(request):
    vc = VerifycationCode()
    image_code, image_path = vc.generate()
    f = open(image_path, "r")
    buffer = f.read()
    f.close()
    vc.destroy()
    httpResponse = HttpResponse(content=buffer)
    request.session['auth_code'] = image_code.lower()  # 校验码不区分大小写
    return httpResponse
