<!-- Behind the Scenes of Loops in system of Python -->
1.Iteration Tools : (For,comprehensions,Map and etc.)

That can be Used on Iterable Objects(List,String,File{Special hai Ye.})

2.Internal Method : iter() that desc the First and initial elem.

3.__next__ : method use to find there is further data for itering or Boundry Reached

if Boundry reached there is Exception Raised Called "Stop Itration" 

"""File iteration is something Unique in Iteration Side"""
in Direct Method there is readline() method for itering each line of File but internaly it has used the next method

open of file is internaly itering the file defaultly so there is no need of iter() method but in list there is not the same.

e.g.range(10)
range are also iterable and handled similarly like list etc.