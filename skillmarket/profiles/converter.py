from django.contrib.auth import get_user_model
from django.http import Http404

class UsernameConverter:
    regex = r"[A-Za-z](?:[A-Za-z0-9]|_(?=[A-Za-z0-9])){4,31}"
    
    def to_python(self, value):
        User = get_user_model()
        user = User.objects.filter(username=value)
        if not user.exists():
            raise Http404("User not found!")
        return value
    
    def to_url(self, value):
        return value