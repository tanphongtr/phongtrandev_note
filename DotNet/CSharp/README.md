### abstract class và interface

abstract class có thể implement interface, nhưng interface không thể implement abstract class.

interface có thể implement nhiều interface, nhưng abstract class chỉ có thể implement 1 abstract class.


### Extention method

Extention method là một method được viết bên ngoài class, nhưng có thể được gọi như là method của class đó.
Mở rộng thêm các method cho các class có sẵn mà không cần thay đổi source code của class đó.

Ví dụ:

    public static class StringExtention
    {
        public static string ToUpperFirstLetter(this string str)
        {
            if (string.IsNullOrEmpty(str))
                return str;
            return char.ToUpper(str[0]) + str.Substring(1);
        }
    }

    string str = "hello";
    str.ToUpperFirstLetter(); // Hello


# Design Pattern
https://www.dofactory.com/net/adapter-design-pattern
