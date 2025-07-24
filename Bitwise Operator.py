# Bitwise operator :

     # to perform binary operation bit by bit on integers . 

            # . AND (&)
            # . OR  (|)
            # . XOR (^)
            # . left shift (<<)
            # . right shift (>>)


a = 5 
b = 3
print(a&b)

print(a|b)

print(a^b)

print(a<<1)

print(a>>1)

# to know this we have to know how to convert binary into decimal and vice versa.

  # Binary into decimal :
         # eg : 
          # binary num   :  0    1    0    1
          # position     :  3    2    1    0
          # power        :  2^3 2^2  2^1  2^0
          #              :  8    4    2    1 
          # (x) b.n      :  0    4    0    1
          # and power 
          # add last row :  0+4+0+1 =  5    this is the decimal number of 0101


    # decimal into binary :
        # take decimal number and find lcm by putting 2 in side . 
        # eg :

        #   2 |_5__      
        #   2 |_2__- 1
        #     |_1__- 0     ^
        #                  |
        #       __________| 

        #  right these numbers form left to right together  101 is the binary num of 5 .
        #  this is also written as 0101 coz of it has in the form of 4 bits . 