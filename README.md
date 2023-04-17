# Microllect
btc wallet attacker 
an introduction to the Bitcoin (BTC) network and how addresses are made
[![HitCount](http://hits.dwyl.com/aryainjas/microllect.svg?style=flat)](http://hits.dwyl.com/aryainjas/microllect)
![Profile views](https://gpvc.arturio.dev/aryainjas)
[![CodeFactor](https://www.codefactor.io/repository/github/aryainjas/microllect/badge)](https://www.codefactor.io/repository/github/aryainjas/microllect)
![made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)
![built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)
![maintend](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
FROM IRAN <3

https://vahm.sellix.io/product/6300faa6ac76c

# Update chages:
cpu usage changed to defualt python runing scripts in windows os.
if you want to use older version(using your all cores to run the script) just add the cpu pool to the main code(microllect.py)
I DO NOT advice to use the old version;it may overheat and damage your hardware.
feel free to send pull requests and etc...
wish good learning yall.( Before using read the disclaimer section and be aware of your actions! )

![microllect film](https://user-images.githubusercontent.com/36337300/150638743-db136fbb-d65c-4f02-bb4e-4b975ed7d6aa.gif)

  
# Microllect
```
Fully automated btc wallet attack.
Just in case for learn about how bitcoin network working.
And learn the protocols that are running.
```
# If you like it give it a star
  [![PyPi license](https://badgen.net/pypi/license/pip/)](https://pypi.com/project/pip/)
  [![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
# Usage:
### Python3+

```
git clone https://github.com/aryainjas/Microllect.git

cd Microllect&& pip install -r requirements.txt

python Microllect.py

```
feel free to send your database.

# Proof of Concept*
```
Example: 
Public : 14F8WRfjxmKyyGYjBXkyyhsMBWumYtLPE9
Private : 5JTwNZeumbo25WtcTQhnzDzufwTvdWXhNANBnPUANNDszM5Kktd
Although this project can be used maliciously, it is simply an 
exploration into the Bitcoin protocol and advanced encryption and 
hashing techniques using Python.
```
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
# Private and Public Keys
A bitcoin wallet contains a collection of key pairs, each consisting of a private key and a public key. The private key (k) is a number, usually picked at random. From the private key, we use elliptic curve multiplication, a one-way cryptographic function, to generate a public key (K). From the public key (K), we use a one-way cryptographic hash function to generate a bitcoin address (A). In this section, we will start with generating the private key, look at the elliptic curve math that is used to turn that into a public key, and finally, generate a bitcoin address from the public key. The relationship between private key, public key, and bitcoin address is shown in Figure:
![private and public key 1](https://user-images.githubusercontent.com/36337300/150638764-d1884542-e5fc-44f7-b26c-874f07555d3a.png)

# Private Keys
A private key is simply a number, picked at random. Ownership and control over the private key is the root of user control over all funds associated with the corresponding bitcoin address. The private key is used to create signatures that are required to spend bitcoins by proving ownership of funds used in a transaction. The private key must remain secret at all times, because revealing it to third parties is equivalent to giving them control over the bitcoins secured by that key. The private key must also be backed up and protected from accidental loss, because if it’s lost it cannot be recovered and the funds secured by it are forever lost.
# Generating a private key from a random number
The first and most important step in generating keys is to find a secure source of entropy, or randomness. Creating a bitcoin key is essentially the same as “Pick a number between 1 and 2^256.” The exact method you use to pick that number does not matter as long as it is not predictable or repeatable. Bitcoin software uses the underlying operating system’s random number generators to produce 256 bits of entropy (randomness). Usually, the OS random number generator is initialized by a human source of randomness, which is why you may be asked to wiggle your mouse around for a few seconds. For the truly paranoid, nothing beats dice, pencil, and paper.

More accurately, the private key can be any number between  `1`  and  `n - 1`, where n is a constant (n = 1.158 * 10^77, slightly less than 2^256 defined as the order of the elliptic curve used in bitcoin. To create such a key, we randomly pick a 256-bit number and check that it is less than  `n - 1`. In programming terms, this is usually achieved by feeding a larger string of random bits, collected from a cryptographically secure source of randomness, into the SHA256 hash algorithm that will conveniently produce a 256-bit number. If the result is less than  `n - 1`, we have a suitable private key. Otherwise, we simply try again with another random number.
#### The following is a randomly generated private key (k) shown in hexadecimal format (256 binary digits shown as 64 hexadecimal digits, each 4 bits):
'''
1E99423A4ED27608A15A2616A2B0E9E52CED330AC530EDCC32C8FFC6A526AEDD
'''
### fun fact
The size of bitcoin’s private key space, 2^256 is an unfathomably large number. It is approximately 10^77 in decimal.
# Public keys
The public key is calculated from the private key using elliptic curve multiplication, which is irreversible: K=k*G where _k_ is the private key, _G_ is a constant point called the _generator point_ and _K_ is the resulting public key. The reverse operation, known as “finding the discrete logarithm”—calculating _k_ if you know _K_—is as difficult as trying all possible values of `k`, i.e., a brute-force search. Before we demonstrate how to generate a public key from a private key, let’s look at elliptic curve cryptography in a bit more detail.
# ### Elliptic Curve Cryptography Explained
Elliptic curve cryptography is a type of asymmetric or public-key cryptography based on the discrete logarithm problem as expressed by addition and multiplication on the points of an elliptic curve.
![elliptic curve](https://user-images.githubusercontent.com/36337300/150638791-32ee4360-f977-4f30-b9f1-359269a08215.png)

Bitcoin uses a specific elliptic curve and set of mathematical constants, as defined in a standard called  `secp256k1`, established by the  National Institute of Standards and Technology (NIST). The  `secp256k1`  curve is defined by the following function, which produces an elliptic curve:
![ellip form](https://user-images.githubusercontent.com/36337300/150638818-f938660b-883d-4bee-afcc-2f87917b1f1e.png)

The _mod p_ (modulo prime number p) indicates that this curve is over a finite field of prime order _p_, also written as F of p where p = 2^256 – 2^32 – 2^9 – 2^8 – 2^7 – 2^6 – 2^4 – 1, a very large prime number.
Because this curve is defined over a finite field of prime order instead of over the real numbers, it looks like a pattern of dots scattered in two dimensions, which makes it difficult to visualize. However, the math is identical as that of an elliptic curve over the real numbers.
![ellip curver with p=17](https://user-images.githubusercontent.com/36337300/150638830-fd98ea06-98af-482f-9d63-3993f887db3d.png)

### So, for example, the following is a point P with coordinates (x,y) that is a point on the `secp256k1` curve. You can check this yourself using Python:
"""
P = (55066263022277343669578718895168534326250603453777594175500187360389116729240, 32670510020758816978083085130507043184471273380659243275938904335757337482424)
"""
In elliptic curve math, there is a point called the  “point at infinity,” which roughly corresponds to the role of 0 in addition. On computers, it’s sometimes represented by x = y = 0 (which doesn’t satisfy the elliptic curve equation, but it’s an easy separate case that can be checked).

There is also  a + operator, called “addition,” which has some properties similar to the traditional addition of real numbers that grade school children learn. Given two points P1  and P2  on the elliptic curve, there is a third point P3  = P1  + P2, also on the elliptic curve.

Geometrically, this third point P3  is calculated by drawing a line between P1  and P2. This line will intersect the elliptic curve in exactly one additional place. Call this point P3' = (x, y). Then reflect in the x-axis to get P3  = (x, –y).

There are a couple of special cases that explain the need for the “point at infinity.”
If P1  and P2  are the same point, the line “between” P1  and P2  should extend to be the tangent on the curve at this point P1. This tangent will intersect the curve in exactly one new point. You can use techniques from calculus to determine the slope of the tangent line. These techniques curiously work, even though we are restricting our interest to points on the curve with two integer coordinates!

In some cases (i.e., if P1  and P2  have the same x values but different y values), the tangent line will be exactly vertical, in which case P3 = “point at infinity.”

If P1  is the “point at infinity,” then the sum P1  + P2  = P2. Similary, if P2  is the point at infinity, then P1  + P2  = P1. This shows how the point at infinity plays the role of 0.

It turns out that + is associative, which means that (A+B)`C = A`(B+C). That means we can write A+B+C without parentheses without any ambiguity.

Now that we have defined addition, we can define multiplication in the standard way that extends addition. For a point P on the elliptic curve, if k is a whole number, then kP = P + P + P + … + P (k times). Note that k is sometimes confusingly called an “exponent” in this case.
# conversion of a public key into a bitcoin address
![conversion of a public key into a bitcoin address](https://user-images.githubusercontent.com/36337300/150638841-861594a3-f240-47c2-9892-dfd5d25347ce.png)
![base58 check](https://user-images.githubusercontent.com/36337300/150638844-5a4cb861-3c7f-4ce7-808b-b572d02f91d0.png)


# Difference between public keys 
![pub key dif](https://user-images.githubusercontent.com/36337300/150638851-ea9408cc-e7a4-4f02-ace7-239ca7cd733d.png)

|  format|private key  |
|Hex|1E99423A4ED27608A15A2616A2B0E9E52CED330AC530EDCC32C8FFC6A526AEDD|
|WIF  |  5J3mBbAH58CpQ3Y5RNJpUKPE62SQ5tfcvU2JpbnkeyhfsYB1Jcn
# Creating master key
![creating master key](https://user-images.githubusercontent.com/36337300/150638854-90925b2b-45e5-4046-923e-f28be2d0fed0.png)
![parent and child](https://user-images.githubusercontent.com/36337300/150638857-542b8732-d7eb-40b9-ae87-db138702ce89.png)


## Donations
If you would like to support me, donations are very welcome.


You can use Paypal to donate using your own credit card. 
The payment is processed by PayPal but you don't need to have a
PayPal account or sign-up for one if you are paying by credit card.



You can also donate Bitcoin, Bitcoin Cash, Tron, Ethereum, Litecoin and etc ...

<a href="https://nowpayments.io/donation?api_key=8NWRRT9-GWM4NDE-JXPJF75-74ZY5D0" target="_blank">
<img src="https://nowpayments.io/images/embeds/donation-button-black.svg" alt="Crypto donation button by NOWPayments">
</a>


[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)]
  
# Disclaimer


The code within this repository comes with no guarantee, the use of this code is **your responsibility***. I take 'NO' responsibility and/or liability for how you choose to use any of the source code available here. By using any of the files available in this repository, you understand that you are AGREEING TO USE AT YOUR OWN RISK.
[![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://saythanks.io/to/aryainjas)
It's important to note that cracking Bitcoin wallets is illegal and unethical. It is against the law to access someone else's Bitcoin wallet without proper authorization.
it is important to use technology responsibly and ethically at all times.
