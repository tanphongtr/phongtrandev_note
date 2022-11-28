Ví dụ signal khi tạo 1 User

```py
# app_name/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from app.models import User

@receiver(post_save, sender=User)
def sample_signal(sender, instance=None, created=False, **kwargs):
    if created:
        print("User created!")
        pass
        
```



```py
# app_name/apps.py

from django.apps import AppConfig
from django.db.models.signals import post_save


class AppNameConfig(AppConfig):
    name = 'app_name'

    def ready(self) -> None:
        from . import signals
        post_save.connect(signals.sample_signal, sender=self.get_model('User'))
        return super().ready()
 ```
 
 
 ```py
 
# settings.py

# replace app_name in INSTALLED_APPS to app_name.apps.AppNameConfig

```

https://stackoverflow.com/questions/59435187/django-signals-not-working-when-placed-outside-models-py

https://stackoverflow.com/questions/37429726/overriding-appconfig-ready
