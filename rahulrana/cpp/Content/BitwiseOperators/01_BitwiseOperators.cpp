/*
    -- THE BITWISE OPERATORS ---
    Common bitwise operators are:
        1.  "&" AND
            Both bits MUST be 1.
            Eg. 1 & 1 = 1
                0 & 1 = 0
                1 & 0 = 0
                0 & 0 = 0
        
        2. "|" OR
            At least one bit should be 1.
            Eg. 1 or 1 = 1
                0 or 1 = 1
                1 or 0 = 1
                0 or 0 = 0

        3. "~" NOT
            Flips all bits.
            Eg. ~101 = 010
                ~01 = 10

        4. "^" XOR
            Exclusive Or. Exactly one of the bits should be 1.
            Eg. 1 ^ 1 = 0
                0 ^ 1 = 1
                1 ^ 0 = 1
                0 ^ 0 = 0

        5. "<<" ">>" Shift operators.
            Shifts bits to the left or the right. Inserts new bits as zero.
            Eg. 5 << 1 - Shifts all bits of 5 to 1 left
                5 ( 00000101 ) << 1 = ( 00001010 ) [shift all to elft, inserts extra bit "0" to the right]
                ( 00001010 ) ==> 10
                Similarly, 2 (00000010) << 1 ==> 4 ( 00000100 )
                Also, 3 ( 00000011 ) << 1 ==> 6 ( 00000110 )
                And, 8 ( 00001000 ) << 1 ==> 16 ( 00010000 )
            
            There is a pattern to be observed:
            Shifting bits to the left basically doubles the number.
            Meaning, a << 1 ==> 2*a
            The reason why this happens is in the way bits work. It is all in the power of 2s.
            Similarly, shifting left by 2 places is like multiplying a number by 4.
            Generally:
                    Shifting a's bits to left by value 'b' means ==>
                        a << b == > ( a*(2^b) )

            THE REVERSE IS NOT TRUE!
            Shifting bits to the right does not always half the value (in case of odd numbers ofc) 



*/