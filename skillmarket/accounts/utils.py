from django.http import HttpRequest

def get_ip(request: HttpRequest):
    x_ip: str = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_ip is not None:
        x_ip.split(',')[0]
    else:
        x_ip = request.META.get('HTTP_X_REAL_IP')
        if x_ip is not None:
            return x_ip
        x_ip = request.META.get('REMOTE_ADDR')
    return x_ip