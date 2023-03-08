# Object-oriented programming (OOP)

## Abstraction (Tính trừu tượng)

```cs
public abstract class Animal
{
    public abstract void Eat();
}
```

## Encapsulation (Tính đóng gói)

```cs
public class Animal
{
    private string _name;
    public string Name
    {
        get { return _name; }
        set { _name = value; }
    }
}
```

## Inheritance (Tính kế thừa)

```cs
public class Animal
{
    public void Eat()
    {
        Console.WriteLine("Eating...");
    }
}

public class Dog : Animal
{
    public void Bark()
    {
        Console.WriteLine("Barking...");
    }
}
```

## Polymorphism (Tính đa hình)

```cs
public class Animal
{
    public virtual void Eat()
    {
        Console.WriteLine("Eating...");
    }
}

public class Dog : Animal
{
    public override void Eat()
    {
        Console.WriteLine("Eating bread...");
    }

    public void Eat(string food)
    {
        Console.WriteLine($"Eating {food}...");
    }

    public void Eat(string food, int amount)
    {
        Console.WriteLine($"Eating {amount} {food}...");
    }
}
```


# SOLID

## Single Responsibility Principle (SRP)

> A class should have only one reason to change.

```cs
public class Customer
{
    public void Add()
    {
        // Add customer to database
    }

    public void SendEmail()
    {
        // Send email to customer
    }
}
```

## Open-Closed Principle (OCP)

> You should be able to extend a class’s behavior, without modifying it.

```cs
public class Customer
{
    public void Add()
    {
        // Add customer to database
    }
}

public class CustomerRepository
{
    public void Add(Customer customer)
    {
        // Add customer to database
    }
}
```


## Liskov Substitution Principle (LSP)

> Derived classes must be substitutable for their base classes.

```cs
public class Rectangle
{
    public virtual int Width { get; set; }
    public virtual int Height { get; set; }

    public Rectangle()
    {
    }

    public Rectangle(int width, int height)
    {
        Width = width;
        Height = height;
    }

    public override string ToString()
    {
        return $"{nameof(Width)}: {Width}, {nameof(Height)}: {Height}";
    }
}

public class Square : Rectangle
{
    public override int Width
    {
        set { base.Width = base.Height = value; }
    }

    public override int Height
    {
        set { base.Width = base.Height = value; }
    }
}
```

## Interface Segregation Principle (ISP)

> Make fine grained interfaces that are client specific.

```cs
public interface IShape
{
    void Draw();
}

public class Circle : IShape
{
    public void Draw()
    {
        // Draw a circle
    }
}

public class Square : IShape
{
    public void Draw()
    {
        // Draw a square
    }
}
```

## Dependency Inversion Principle (DIP)

> Depend on abstractions, not on concretions.

```cs
public interface IShape
{
    void Draw();
}

public class Circle : IShape
{
    public void Draw()
    {
        // Draw a circle
    }
}

public class Square : IShape
{
    public void Draw()
    {
        // Draw a square
    }
}

public class ShapeDrawer
{
    private readonly IShape _shape;

    public ShapeDrawer(IShape shape)
    {
        _shape = shape;
    }

    public void Draw()
    {
        _shape.Draw();
    }
}
```

# Design Patterns

## Creational Patterns

### Abstract Factory

> Provide an interface for creating families of related or dependent objects without specifying their concrete classes.

```cs
public interface IShape
{
    void Draw();
}

public class Circle : IShape
{
    public void Draw()
    {
        // Draw a circle
    }
}

public class Square : IShape
{
    public void Draw()
    {
        // Draw a square
    }
}

public interface IShapeFactory
{
    IShape Create();
}

public class CircleFactory : IShapeFactory
{
    public IShape Create()
    {
        return new Circle();
    }
}

public class SquareFactory : IShapeFactory
{
    public IShape Create()
    {
        return new Square();
    }
}

public class ShapeDrawer
{
    private readonly IShapeFactory _shapeFactory;

    public ShapeDrawer(IShapeFactory shapeFactory)
    {
        _shapeFactory = shapeFactory;
    }

    public void Draw()
    {
        var shape = _shapeFactory.Create();
        shape.Draw();
    }
}
```


# ACID SQL

> Việc đảm bảo ACID cho các giao dịch trong cơ sở dữ liệu rất quan trọng để đảm bảo tính toàn vẹn và độ tin cậy của dữ liệu.

## Atomicity (Tính nguyên tố)

> A transaction is atomic if it is an indivisible and irreducible series of database operations such that either all occur, or nothing occurs.

> Một giao dịch phải được thực thi hoặc không được thực thi hoàn toàn. Nếu một phần của giao dịch thất bại, thì tất cả các thay đổi được áp dụng bởi giao dịch đó sẽ bị hủy bỏ.

```sql
BEGIN TRANSACTION;
UPDATE Customers SET ContactName = 'Alfred Schmidt', City= 'Frankfurt' WHERE CustomerID = 1;
UPDATE Orders SET OrderDate = '2018-01-18' WHERE CustomerID = 1;
COMMIT;
```

## Consistency (Tính nhất quán)

> A transaction is consistent if it brings the database from one valid state to another.

> Một giao dịch phải đảm bảo rằng cơ sở dữ liệu nằm trong trạng thái hợp lệ trước và sau khi giao dịch được thực hiện. Ví dụ, nếu cơ sở dữ liệu yêu cầu một khóa duy nhất cho mỗi hàng trong bảng, thì giao dịch phải đảm bảo rằng không có hai hàng trùng lặp nào được chèn vào bảng trong cùng một thời điểm.


## Isolation (Tính độc lập)

> A transaction is isolated if the concurrent execution of transactions results in a system state that would be obtained if transactions were executed serially, i.e., one after the other.

> Mỗi giao dịch phải chạy trong một không gian độc lập, không ảnh hưởng đến các giao dịch khác đang chạy đồng thời trên cùng một cơ sở dữ liệu. Điều này đảm bảo rằng các thay đổi của một giao dịch sẽ không được xem trước hoặc ảnh hưởng bởi các giao dịch khác.


## Durability (Tính bền vững)

> A transaction is durable if once it has been committed, it will remain so, even in the event of power loss, crashes, or errors.

> Một giao dịch đã hoàn tất sẽ được lưu trữ một cách an toàn và không thể bị mất hoặc hỏng trong trường hợp có lỗi hệ thống hoặc máy chủ bị sập.

# SQL Injection

> SQL Injection là một kỹ thuật tấn công cho phép hacker thực thi các câu lệnh SQL trên một website thông qua các input từ người dùng.
