# Admin

## admin.ModelAdmin

```py
# admin/model_admin.py

def changelist_view(self, request, extra_context=None):
    extra_context = extra_context or {}
    extra_context['title'] = 'Title'
    extra_context['subtitle'] = 'Sub Title'
    return super().changelist_view(request, extra_context=extra_context)

change_list_template = "ChangeList.html"
  
```
```
# templates/ChangeList.html
{{ title }}
{{ subtitle }}
```
