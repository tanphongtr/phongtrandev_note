# Get thuộc tính object

```csharp
var properties = typeof(Student)
    .GetProperties(BindingFlags.Public | BindingFlags.Instance)
    .ToList();

foreach (var property in properties)
{
    Console.WriteLine($"{property.Name} {property.MetadataToken}");
}

```