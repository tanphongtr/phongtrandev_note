Clean Architecture là một phương pháp thiết kế kiến trúc phần mềm, tập trung vào việc tách biệt các thành phần của hệ thống và giữ cho mã nguồn luôn sạch đẹp, dễ bảo trì và mở rộng.

Trong Clean Architecture, hệ thống được chia thành nhiều lớp khác nhau, mỗi lớp có một nhiệm vụ cụ thể và giữ một số quy định nhất định. Các lớp này được xếp thành các vòng tròn (circles) với độ ưu tiên giảm dần khi đi từ trung tâm hệ thống ra ngoài.

Trong vòng tròn bên trong, các thành phần như Entities và Use Cases được định nghĩa, chúng chịu trách nhiệm cho việc xử lý logic nghiệp vụ và dữ liệu của hệ thống. Vòng tròn tiếp theo là Interface Adapters, các thành phần này sử dụng các thành phần bên trong để cung cấp giao diện cho người dùng hoặc các hệ thống bên ngoài. Cuối cùng, vòng tròn bên ngoài là các thành phần Frameworks & Drivers, chịu trách nhiệm cho các tác vụ cơ bản như truyền thông qua mạng, lưu trữ dữ liệu hoặc xử lý giao diện người dùng.

Mục đích chính của Clean Architecture là tạo ra một hệ thống linh hoạt, dễ dàng bảo trì, mở rộng và thích ứng với các yêu cầu thay đổi của khách hàng và thị trường.

https://www.ezzylearning.net/tutorial/a-guide-for-building-software-with-clean-architecture