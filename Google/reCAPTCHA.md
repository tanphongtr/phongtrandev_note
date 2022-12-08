

```js
// Client

<script src="https://www.google.com/recaptcha/enterprise.js?render=6Lc-RGAjAAAAAMKRitTB9P0JivjtIXxxxxxxxxxx"></script>
<script>
grecaptcha.enterprise.ready(function() {
    grecaptcha.enterprise.execute('6Lc-RGAjAAAAAMKRitTB9P0JivjtIXxxxxxxxxxx', {action: 'submit'}).then(function(token) {
        console.log(token);
    });
});
</script>
```


```cURL
# Check token được tạo từ client
curl --location --request POST 'https://www.google.com/recaptcha/api/siteverify?secret={SECRET}&response={TOKEN}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "secret": "{SECRET}"
}'

# Response
{
    "success": true,
    "challenge_ts": "2022-12-07T15:54:26Z",
    "hostname": "localhost",
    "score": 0.9,
    "action": "submit"
}
```
