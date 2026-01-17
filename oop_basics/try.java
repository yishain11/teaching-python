public class try {
/* try.java
 * Demonstration of public vs private fields and static methods in Java.
 * This file intentionally does not declare any public class, so the
 * filename does not need to match a public class name.
 */

class Person {
	public String name;
	public int age;
	private String ssn;
	private double salary;

	Person(String name, int age, String ssn, double salary) {
		this.name = name;
		this.age = age;
		this.ssn = ssn;
		this.salary = salary;
	}

	public String getSsn() {
		return ssn;
	}

	public void setSsn(String ssn) {
		this.ssn = ssn;
	}

	@Override
	public String toString() {
		return String.format("Person(name=%s, age=%d, salary=%.2f)", name, age, salary);
	}
}

class MathUtils {
	public static final String VERSION = "1.0";

	public static int add(int a, int b) {
		return a + b;
	}

	public static int multiply(int a, int b) {
		return a * b;
	}

	public static String version() {
		return VERSION;
	}
}

class Examples {
	public static void main(String[] args) {
		Person p = new Person("Alice", 30, "123-45-6789", 70000);

		System.out.println("Public access: " + p.name + ", " + p.age);
		// The following would not compile because ssn is private:
		// System.out.println(p.ssn);
		System.out.println("Private access via getter: " + p.getSsn());
		System.out.println(p.toString());

		System.out.println("MathUtils.add(2,3): " + MathUtils.add(2, 3));
		System.out.println("MathUtils.multiply(4,5): " + MathUtils.multiply(4, 5));
		System.out.println("MathUtils.version(): " + MathUtils.version());
	}
}

}
