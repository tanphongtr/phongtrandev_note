```js
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

curl --location --request POST 'https://www.google.com/recaptcha/api/siteverify?secret={SECRET}&response={TOKEN}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "secret": "{SECRET}"
}'
```
