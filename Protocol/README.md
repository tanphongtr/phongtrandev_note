# Single sign-on
Có 2 giao thức phổ biến cho quy trình xác thực SSO  
There are two protocols for this authentication process
### SAML
**S**ecutiry **A**ssertion **M**arkup **L**ang  
https://github.com/onelogin/python3-saml
### OpenID
https://github.com/openid/python-openid


# Server-sent Event
https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events

Sự kiện do máy chủ gửi (SSE) là công nghệ đẩy máy chủ cho phép máy khách nhận các bản cập nhật tự động từ máy chủ thông qua kết nối HTTP và mô tả cách máy chủ có thể bắt đầu truyền dữ liệu tới máy khách sau khi kết nối máy khách ban đầu được thiết lập.

![image](https://user-images.githubusercontent.com/11567406/206900970-7e42f48e-c2b8-4d97-b906-f5ce0646018e.png)

VD: twitter sẽ luôn update số lượng comment, like, retweet

<img width="894" alt="image" src="https://user-images.githubusercontent.com/11567406/206901065-c4028727-4461-4f67-bd41-1fd90f619cdb.png">

```json
{"topic":"/tweet_engagement/1601616641158049792","payload":{"tweet_engagement":{"like_count":"2604"}}}
```


# Web Socket
