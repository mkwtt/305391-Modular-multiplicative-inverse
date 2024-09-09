# Extended Euclidean Algorithm

The Extended Euclidean Algorithm is an extension of the Euclidean Algorithm, which is used to find the greatest common divisor (GCD) of two integers. The extended version not only finds the GCD, but also finds integers \(x\) and \(y\) such that:

$$
a \cdot x + b \cdot y = \text{GCD}(a, b)
$$

This property is particularly useful when finding the modular multiplicative inverse, as we can use it to find an integer \(x\) such that:

$$
a \cdot x \equiv 1 \pmod{m}
$$

## Steps of the Extended Euclidean Algorithm:

1. **Apply the Euclidean Algorithm**: Use the division algorithm repeatedly to find the GCD of two numbers \(a\) and \(b\).
   
   $$
   a = b \cdot q + r
   $$

   where \(q\) is the quotient and \(r\) is the remainder. Repeat this step using \(b\) and \(r\) until the remainder is zero. The last non-zero remainder is the GCD.

2. **Back-substitution**: Once the GCD is found, backtrack through the steps of the Euclidean Algorithm to express the GCD as a linear combination of \(a\) and \(b\). This is done using the quotients from each division step.

3. **Find \(x\) and \(y\)**: The coefficients \(x\) and \(y\) from the back-substitution step are the solutions to the equation \(a \cdot x + b \cdot y = \text{GCD}(a, b)\).

4. **Modular Inverse**: If you need to find the modular inverse of \(a\) modulo \(m\), then the solution \(x\) (from the equation where \(GCD = 1\)) will be the inverse.

## Example:

Let's find the modular multiplicative inverse of \(a = 3\) modulo \(m = 7\).

1. **Apply Euclidean Algorithm:**
   
   $$
   7 = 3 \cdot 2 + 1
   $$

   $$
   3 = 1 \cdot 3 + 0
   $$

   The GCD is 1 (last non-zero remainder).

2. **Back-substitution:**

   From the first equation:

   $$
   1 = 7 - 3 \cdot 2
   $$

   So we can write:

   $$
   1 = 7 \cdot 1 + 3 \cdot (-2)
   $$

   In terms of \(x\) and \(y\):

   $$
   1 = 3 \cdot (-2) + 7 \cdot 1
   $$

   Thus, \(x = -2\). Since we want the inverse modulo 7, adjust \(x\) to be positive:

   $$
   x = -2 \equiv 5 \pmod{7}
   $$

So, the modular multiplicative inverse of 3 modulo 7 is 5.

This method can be generalized for any two numbers where you need to find their inverse modulo some value.
