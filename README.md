# RSA Encryption

I am implementing an RSA algorithm for string encryption.

* __generate.py__ Takes two prime numbers as an input and returns the encryption keys.

* __encrypt.py__ Takes a string and the public keys as an input, transcodes it into a number, runs it through the algorithm and returns an encrypted number.

* __decrypt.py__ Takes an array of encrypted numbers, the private and the public key, runs them through the algorithm, turns the int array into a string and returns it.

---
## How does it do all that?

It uses prime numbers to generate a public __(e, n)__ and a private __(d)__ key.

### How to generate the keys

1. Select two large distinct prime numbers __p__ and __q__

2. Calculate their product __n__
```
n = p * q
```
3. Calculate __φ(n)__
```
φ(n) = (p - 1) * (q - 1)
```
4. Choose encryption exponent __e__ (also prime). Generally __c__ is _65,537_
```
1 < e < φ(n)
gcd(e, φ(n)) = 1
```
5. Choose __d__ such that
```
(e * d) mod φ(n) = 1
```

### To Encrypt
```
m ^ e mod n = c
```
* __m__ - The message. __m ^ e > n__ and __m < n__
* __e__ - Pubic key
* __n__ - Public key

### To Decrypt
```
c ^ d mod N = m
```
* __d__ - private key
* __n__ - public key
