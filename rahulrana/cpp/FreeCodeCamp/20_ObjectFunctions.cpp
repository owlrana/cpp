// Object Functions in C++, can also be called instance functions
// These are functions inside the classes so the class can use different functions in itself
// they can find information or modidy information within the class

# include <iostream>

using namespace std;

class Student {
    public:
        string name;
        string major;
        double gpa;
        
        Student (string aName, string aMajor, double aGpa) {
            name = aName;
            major = aMajor;
            gpa = aGpa;
        }

        // suppose the school has an honour-role which is decided by the GPA
        // thus for each object, we can find out if the object is on the honour-role or not
        bool hasHonours () {
            if(gpa >= 3.5){
                return true; // in cpp, it is "true" and NOT "True" like it is in python
            }
            return false; // "false" and NOT "False"
        }
        // mainly functions are used to get information, modifying values eg Getters, Setters etc
};

int main()
{
    Student student1 ("Jim", "Business", 2.4);
    Student student2 ("Pam", "Art", 3.6);

    cout << student1.name << ": " << student1.hasHonours() << endl; //0 means false and 1 means True
    cout << student2.name << ": " << student2.hasHonours() << endl;


    return 0;
}

// creating a function inside our class makes it very easy to change logic
// eg, if the system of honours is changed to gpa >= 4.0, then we only need to change our logic once
// and then it works for each specific object