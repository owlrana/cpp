/*
    --- Some more problems that we can solve by bits manipulation ---

    1. Finding if the given number is even or odd
        ->  Every number is represented in it's binary form through 0s and 1s.
            If a number has it's FIRST PLACE from RIGHT ==> 1, then the number is odd
            This can be understood as every other power of 2 contributes an even number
            
            Eg.
                00001010 is even (10)
                00001011 is odd (11)
                00001000 is even (16)
                00001001 is odd (17)

            But how do you check if a given number is odd or even?
            ->  By doing & with 1.
            
            Eg. ( 5 & 1 ) ==> 1 MEANS ODD
                    5 = 00000101
                    1 = 00000001
                ==> 1 means ODD //  can also be said:
                                    if (5 & 1)
                                        cout << "Num is odd";
                                        
            Similarly, for even:
                ( 4 & 1 ) ==> 0 MEANS EVEN

*/