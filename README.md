# django_note

## Conditional View Processing
https://docs.djangoproject.com/en/4.1/topics/conditional-view-processing/



```py
from django.views.decorators.http import condition, last_modified
from django.contrib.auth import get_user_model
import datetime

def latest_update(request, *args, **kwargs):
    # code sẽ luôn chạy vào đây, nếu last_login không có gì thay đổi sẽ lấy data từ cache
    # ngược lại sẽ chạy vào view index
    print("latest_update")
    return get_user_model().objects.latest('last_login').last_login

# @cache_page(60 * 15) # last_modified sẽ không hoạt động nếu dùng cache_page
@last_modified(latest_update)
def index(request):
    date = datetime.datetime.now()
    return HttpResponse(f'{date} - {request.user}')
```
