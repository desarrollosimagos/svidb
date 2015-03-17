from django.contrib.auth.models import User

User._meta.get_field_by_name('username')[0].max_length=255
