# RSA Encryption

I am implementing an RSA algorithm for string encryption

## How it works

It uses prime numbers to generate a public __(e, n)__ and a private (d) key.

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

---
## How to generate the keys

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
5. Choose __d__ such that __e * d mod φ(n) = 1__
