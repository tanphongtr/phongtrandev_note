List:
- [decorators](#decorators).

# Python
- [OOP in Python](https://voz.vn/t/object-oriented-programming-trong-python.693116/)

# pip
### Uninstall all packages

```
$ pip uninstall -y -r <(pip freeze)
```


### Install a package

```
$ pip install <package-name>

$ pip install -r requirements.txt
```


# jupyter/ipython

```
$ pip install jupyter
```

Run:
```
$ ipython
or
$ jupyter notebook

```

### Time in jupyter/ipython
```
%%time
```
![image](https://user-images.githubusercontent.com/11567406/203929196-90376b6e-44a8-4c46-be07-03aa1fcbf6bb.png)


### Virtual environment
```
python3 -m venv virtual_env
```

```
source /Users/phongtran/Repositories/Python/virtual_env/bin/activate
```

Using in VSCode:
```/Users/phongtran/Repositories/Python/virtual_env/bin/python```
![image](https://user-images.githubusercontent.com/11567406/203928328-a54853d8-2443-449b-9750-42824077a9cb.png)


### Decorators


```py

# func này trả về wrap_f, nên lưu ý mọi param truyền từ @warp phải phụ thuộc vào wrap_f
def warp(test):
    print('this is wrap')
    def wrap_f(test):
        test()
    return wrap_f

@warp(
    test='test'
)
def test():
    print('this is test')
```

```py
def as_string():
    print("sdfsdf")

    def inner(func):
        print('inner', func)
        return func

    return inner


@as_string()
def number(a=3):
    print('num', a)


number(a=8)
```


magic method:
```py
def __init__(self, name):
    self.name = name

def __str__(self):
    return self.name

def __repr__(self):
    
    
    
```


# Multithread

https://realpython.com/python-gil/ (bản dịch: http://doanguyen.com/python-gil)
