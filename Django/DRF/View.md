# View

View của Django Rest Framework 

```py
from rest_framework import generics, viewsets

Serializer có 2 loại:
- Serializer: create
- ModelSerializer: create, update

Viewset có 2 loại:
- ViewSet: create
- ModelViewSet: create, update
```

# Serializer

BaseSerializer class that can be used to easily support alternative serialization and deserialization styles.

This class implements the same basic API as the Serializer class:

.data - Returns the outgoing primitive representation.  
.is_valid() - Deserializes and validates incoming data.  
.validated_data - Returns the validated incoming data.  
.errors - Returns any errors during validation.  
.save() - Persists the validated data into an object instance.  
There are four methods that can be overridden, depending on what functionality you want the serializer class to support:

.to_representation() - Override this to support serialization, for read operations.  
.to_internal_value() - Override this to support deserialization, for write operations.  
.create() and .update() - Override either or both of these to support saving instances.  
