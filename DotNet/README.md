// how to connect db in asp.net core
// https://docs.microsoft.com/en-us/ef/core/get-started/aspnetcore/new-db?tabs=netcore-cli
// https://docs.microsoft.com/en-us/ef/core/get-started/aspnetcore/existing-db?tabs=netcore-cli
// https://docs.microsoft.com/en-us/ef/core/get-started/aspnetcore/new-db-sqlite?tabs=netcore-cli
// https://docs.microsoft.com/en-us/ef/core/get-started/aspnetcore/existing-db-sqlite?tabs=netcore-cli


# Jupyter Notebook

# Install jupyterlab to default Python interpreter
```pip install jupyterlab```
# Install Dotnet Interactive dotnet tool
```dotnet tool install -g Microsoft.dotnet-interactive```
# Get Dotnet Interactive to register kernels with Jupyter  
```dotnet interactive jupyter install```

### This should list .net-csharp as one of the kernels which is what the C# notebooks will use.
```jupyter kernelspec list```

### Running JupyterLab
```jupyter lab```


# dotnet new mvc -o aspnetcoreapp


# .Net Runtime và .Net SDK

.NET Runtime và .NET SDK là hai thành phần quan trọng của nền tảng phát triển phần mềm .NET của Microsoft.

.NET Runtime là một môi trường thực thi cho các ứng dụng .NET. Nó cung cấp các thư viện và công cụ để thực thi các ứng dụng .NET trên máy tính của bạn. Khi bạn chạy một ứng dụng .NET trên máy tính của mình, .NET Runtime sẽ tự động được tải lên để thực thi ứng dụng đó.

.NET SDK (Software Development Kit) là một bộ công cụ phát triển phần mềm .NET. Nó bao gồm một tập hợp các công cụ, thư viện và tài liệu cần thiết để phát triển ứng dụng .NET. Nó bao gồm trình biên dịch để biên dịch mã nguồn .NET, các công cụ để tạo và quản lý các dự án .NET, cũng như các thư viện .NET để phát triển ứng dụng .NET. Khi bạn muốn phát triển ứng dụng .NET, bạn cần cài đặt .NET SDK để có thể sử dụng các công cụ và thư viện cần thiết.