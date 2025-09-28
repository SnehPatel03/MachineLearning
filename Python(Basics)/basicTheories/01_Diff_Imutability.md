<!-- MUTABLE AND IMMUTABLE IN PY -->
<!-- Referance Concept in Py -->

In the Python all the types are treated as a object.
there are some Immutable Types like Int,String,tupels etc.

But actually what Immutable mean by is Understood by a example : 

username = "hitesh"

then we are changing is to another name like 

username = "patel"

well,at here  python is not going to yelling at you bcz in it works like given below

firstly a memory is created for a username for "hitesh"

then when we are going to change that one another memory is created names "patel" and then a username refers to a "patel" that means there is no any update happpen to "hitesh" but new memory is allocated and refeeance of username is pointed to it.

after that when no one is refering the "hitesh" memory block the garbage collection of python will delete it and make memory free.   