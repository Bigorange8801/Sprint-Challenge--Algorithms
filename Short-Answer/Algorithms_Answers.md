#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - This would almost appear to be O(n^3) however, the extra n's are canceled by a = a + n * n which rapidly decreases the amount it take for a to be greater than or equal to n

b) O(nlogn) - Since the second loop is not growing by 1 but rather doubles, as n grows, the second loop takes less time to complete. The first loop take n times to complete thus giving n * log(n)

c) O(n) - The function is recursively called the number of bunnies there are since bunnies-1 is called until the base case is reached where bunnies == 0

## Exercise II

floor = 0

drop egg from floor: if egg does not break increase floor. drop egg from increased floor else if egg breaks then stop. Eggs from this floor onward will break.

The runtime complexity of this would be O(n) because we have a single loop. 
