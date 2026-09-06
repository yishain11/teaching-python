// ─── Public class (accessible from anywhere) ───────────────────────────────
public class Animal {

    // public: accessible from anywhere
    public String name;

    // protected: accessible within same package + subclasses
    protected int age;

    // private: accessible only within this class
    private String secret;

    public Animal(String name, int age, String secret) {
        this.name = name;
        this.age = age;
        this.secret = secret;
    }

    // public method — anyone can call this
    public String getName() {
        return name;
    }

    // protected method — subclasses and same-package code can call this
    protected int getAge() {
        return age;
    }

    // private method — only used internally
    private String revealSecret() {
        return secret;
    }

    // public method that internally delegates to private method
    public String describe() {
        return name + " (age " + age + ") — secret: " + revealSecret();
    }
}


// ─── Subclass (inheritance + protected access) ──────────────────────────────
class Dog extends Animal {

    private String breed;

    public Dog(String name, int age, String breed) {
        super(name, age, "I love bones");
        this.breed = breed;
    }

    public void showInfo() {
        System.out.println("Name: " + name);         // public field — OK
        System.out.println("Age: " + getAge());      // protected method — OK
        System.out.println("Breed: " + breed);       // own private field — OK
        // System.out.println(secret);               // ERROR: private in Animal
        // System.out.println(revealSecret());       // ERROR: private in Animal
    }
}


// ─── Unrelated class (same package) ─────────────────────────────────────────
class Main {
    public static void main(String[] args) {
        Animal a = new Animal("Cat", 3, "I hate dogs");

        System.out.println(a.name);      // public — OK
        System.out.println(a.getAge());  // protected — OK (same package)
        System.out.println(a.describe()); // public — OK
        // System.out.println(a.secret);          // ERROR: private
        // System.out.println(a.revealSecret());  // ERROR: private

        Dog d = new Dog("Rex", 5, "Labrador");
        d.showInfo();
    }
}
