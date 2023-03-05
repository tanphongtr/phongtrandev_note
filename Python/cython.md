```pip install Cython```

1. Cài đặt Cython: Bạn có thể cài đặt Cython bằng pip bằng cách chạy lệnh sau trong terminal hoặc command prompt:
````pip install Cython````

2. Tạo file setup.py với nội dung sau:
```python
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("sum.pyx")
)
```

3. Tạo file sum.pyx:
```python
def sum_of_n_numbers(n):
    cdef int i, sum
    sum = 0
    for i in range(n):
        sum += i
    return sum
```

4. Chạy lệnh sau để biên dịch file sum.pyx thành file sum.c:
```python setup.py build_ext --inplace```

Khi quá trình build hoàn tất, bạn sẽ có một file sum.so được tạo ra trong cùng thư mục với file sum.pyx. File này chứa hàm tính tổng của các số từ 0 đến n đã được mã hoá bằng Cython.

5. Sử dụng hàm sum_of_n_numbers trong file sum.pyx:
Bạn có thể import hàm sum_of_n_numbers từ file mã hoá và sử dụng như bình thường. Ví dụ:


```python
import sum

# sử dụng hàm sum_of_n_numbers từ file mã hoá
result = sum.sum_of_n_numbers(10)
print(result)
```