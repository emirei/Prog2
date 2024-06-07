#include <cstdlib>
// Person class
//Redovisat för Viktor Lindström 21/05/2024

class Person{
	public:
		Person(int);
		int getAge();
		void setAge(int);
		double getDecades();
		int fib();
	private:
		int age;
		int _fib(int);
	};
 
Person::Person(int a){
	age = a;
	}
 
int Person::getAge(){
	return age;
	}
 
void Person::setAge(int a){
	age = a;
	}

double Person::getDecades(){
	return age/10.0;
	}

int Person::fib(){
	return _fib(age);
}

int Person::_fib(int a){
	if (a <= 1) {
		return a;
	} else {
		return (_fib(a-1) + _fib(a-2));
	}
	}




extern "C"{
	Person* Person_new(int a) {return new Person(a);}
	int Person_getAge(Person* person) {return person->getAge();}
	void Person_setAge(Person* person, int a) {person->setAge(a);}
	double Person_getDecades(Person* person) {return person->getDecades();}
	int Person_fib(Person* person) {return person->fib();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}
