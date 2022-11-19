# Queryset

## annotate()

```python
test = model_list.all() \
    .values('invoices__gifts__gift__code') \
    .order_by('invoices__gifts__gift__code') \
    .annotate(
        count=Sum('invoices__gifts__quantity'),
    ).exclude(invoices__gifts__gift__code__isnull=True)
```

```
code	count
DONG_HO_DEO_TAY	859
HOP_BAM_MONG_TAY	1404
LY_THUY_TINH	2383
MAY_LA_TOC	1485
TUI_TOTE	1225
UNICORN_KHONG_LO	102![image](https://user-images.githubusercontent.com/11567406/202834626-dcddb9c7-46a1-4267-acdb-e51b3ddf1c0a.png)
```
