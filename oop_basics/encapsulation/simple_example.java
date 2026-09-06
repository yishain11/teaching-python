public class Animal {
    public String name;
    private int age;
    # constructor
    public Animal(String name, int age){
        this.name = name;
        this.age = age;
    }

    public int getAge(){
        return this.age;
    }

}

class Dog extends Animal {
    # constructor
    public Dog(String name, int age){
        super(name,age)
    }

    public void printAge(){
        System.out.println(this.age) # X - PRIVATE in Animal
    }
}

class Main {
    public static void main(String[] args) {
        Animal a = new Animal("Cat", 3,);

        System.out.println(a.name);      // public — OK
        System.out.println(a.getAge());  // protected — OK (same package)
        System.out.println(a.age)        // X - private!

        Dog d = new Dog("Rex", 5, "Labrador");
        d.showInfo();
    }
}
