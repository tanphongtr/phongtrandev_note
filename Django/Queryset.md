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
