# Questions related to the Advanced Python: Language Features course from LikedIn Learning Path

* how long is the lifetime of the variable? 
    * [Stack Overflow - default parameters change during execution](https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument)
    * [Scope in Python](https://www.scientecheasy.com/2022/12/scope-in-python.html/)
    * 
* lambdas 
    * how to use them other than using map?
        * [full guide ofn python lambdas](https://realpython.com/python-lambda/)
        * you can easly use it just to calcutae something e.g. return value (to not store it in a declared variable) `return lambda x : x + 2`
        * as a usuall function `a = lmbda x : x + 2` then `a(5)`
        * it can be also immediately invoked `(lambda x : x + 2)(5)`
    * is there a possibility to save it in a variable na duse as standard function?
        * YES! 
* is there a difference between using `a**2` and `a*a` in the term of computational complexity/performance?
    * according to my experiments - YES - it is related to the additional checks that `**` operator do to support among others fractional exponents, negative exponents
