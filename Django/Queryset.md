# Queryset

## annotate()

```python
test = model_list.all() \
    .values('invoices__gifts__gift__code') \ # Group by
    .order_by('invoices__gifts__gift__code') \
    .annotate(
        count=Sum('invoices__gifts__quantity'),
    ).exclude(invoices__gifts__gift__code__isnull=True)
```

![image](https://user-images.githubusercontent.com/11567406/202834643-5109eeed-0ee3-42fa-96ad-d3a3fd8e65b5.png)
