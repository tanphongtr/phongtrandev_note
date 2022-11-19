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

<img width="234" alt="image" src="https://user-images.githubusercontent.com/11567406/202834719-0d6b8699-b27f-47cb-b669-458d49b90812.png">

## aggregate()

```python
TUI_TOTE = model_list.all().aggregate(
    total=Coalesce(
        Sum('invoices__gifts__quantity', filter=Q(invoices__gifts__gift__code=Gift.CodeChoices.TUI_TOTE)), 0)
)['total']
```
