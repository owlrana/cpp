// Getters and Setters in cpp classes are useful to access/modify diff elements in your classes

# include <iostream>

using namespace std;

/*
class Movie {
    public:
        string title;
        string director;
        string rating;
        
        Movie (string aTitle, string aDirector, string aRating) {
            title = aTitle;
            director = aDirector;
            rating = aRating;
        }
};

int main()
{
    Movie avengers("The Avengers", "Joss Whedon", "PG-13");
    // now suppose we only have certain types of rating only
    // but there is nothing stopping us from having the rating of movie as "idiotic"
    avengers.rating = "idiotic";
    cout << avengers.rating;

    // thus we need a valid rating and don't want any user to input nonsense
    // this can be done by getter and setters



    return 0;
}
*/

// Thus, we now introduce the private attributes

class Movie {
    private: // cannot be accessed outside the class definition, hence nobody can mess with it
        string rating;
    public:
        string title;
        string director;
        // constructor can access rating as it is inside the class definition
        Movie (string aTitle, string aDirector, string aRating) {
            title = aTitle;
            director = aDirector;
            rating = aRating;
        }

        //any user who wants to now change the rating needs to go through this function
        void setRating (string aRating) {
            
            // rating = aRating; //  instead of just setting the rating directly, we can have rules
            if (aRating == "G" or aRating == "PG" or aRating == "PG-13" or aRating == "R" or aRating == "NR") {
                rating = aRating;
            } else {
                rating = "NR"; // set it as Not Rated
            }
            // if the user does not enter a valid rating
        }

        // to get the rating that is set
        string getRating () {
            return rating;
        }
};

int main()
{
    Movie avengers("The Avengers", "Joss Whedon", "PG-13");
    // avengers.rating; // this will result in an error now as rating is now private!!
    
    // you can still set the rating as dog, but you need to go through the setter and it's rules
    avengers.setRating("PG-13");

    // cout << avengers.rating; // this also wont work as it is private variable of our class
    cout << avengers.getRating() << endl;

    avengers.setRating("dawg");
    cout << avengers.getRating() << endl;

    return 0;
}

// This is the perfect way to control how user interacts with our class
// private variables are strinctly private, not like in python. There is no mangling. You just cant access!