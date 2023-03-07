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