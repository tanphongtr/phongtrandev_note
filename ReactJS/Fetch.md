To fetch data from a REST API with React Query, you can use the useQuery hook provided by the library. Here's an example of how you might use the useQuery hook to fetch data from a REST API:

```ts
import React from 'react';
import { useQuery } from 'react-query';

function MyComponent() {
  const { data, error, loading } = useQuery('user', () =>
    fetch('https://my-api.com/user/1').then(res => res.json())
  );

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <div>
      <p>Name: {data.name}</p>
      <p>Email: {data.email}</p>
    </div>
  );
}
```
