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
