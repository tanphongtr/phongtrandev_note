// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;

namespace Test
{
    class Program
    {

        static void Main(string[] args)
        {
            VFastEngine vFastEngine = new VFastEngine(model: "test");
            Machine machine = new Machine(vFastEngine);
            machine.run();
        }

    }

    public interface IEngine
    {
        public string getModel();

        public void run();
    }


    public class Engine : IEngine
    {
        private string _model;

        public Engine(string model)
        {
            _model = model;
        }

        public virtual string getModel()
        {
            return _model;
        }

        public virtual void run()
        {
            Console.WriteLine($"The car {getModel()} running!");
        }
    }


    public class VFastEngine : Engine
    {
        private string _model;

        public VFastEngine(string model) : base(model)
        {
            _model = model;
        }

    }


    public class Machine
    {
        IEngine _engine;

        public Machine(IEngine engine)
        {
            _engine = engine;
        }

        public void run()
        {
            _engine.run();
        }
    }
    
    // container generic class
    public class Container<T>
    {
        private T _value;

        public Container(T value)
        {
            _value = value;
        }

        public T getValue()
        {
            return _value;
        }
    }

    // class using container
    public class Test
    {
        public void test()
        {
            Container<string> container = new Container<string>("test");
            Console.WriteLine(container.getValue());

            Queue<string> strings = new Queue<string>(new string[] {"1", "2"});
            strings.Enqueue("3");
        }

        public void test2()
        {

        }

        // bracket operator ahead of method name
    }

    // custom attribute parameter
    [AttributeUsage(AttributeTargets.Parameter)]
    public class CustomAttribute : Attribute
    {
        public bool IsValid(string value)
        {
            return value == "test";
        }

        public CustomAttribute(string value)
        {
            if (!IsValid(value))
            {
                throw new Exception("Invalid value");
            }
        }
    }

    // custom attribute usage
    [CustomAttribute("test")]
    public class Test2
    {
        [CustomAttribute("test2")]
        public void test()
        {

        }
    }


    // AttributeUsage, inherit ValidationAttribute

    // custom attribute parameter
    [AttributeUsage(AttributeTargets.Parameter)]
    public class CustomAttribute : Attribute
    {
        public bool IsValid(string value)
        {
            return value == "test";
        }

        public CustomAttribute(string value)
        {
            if (!IsValid(value))
            {
                throw new Exception("Invalid value");
            }
        }
    }
}

