from State import State

ex = State("Florida","Talahassee","FL",99989,"South",4)
print ex

ex2 = State("Apple","Talahassee","FL",99989,"South",4)

ex3 = State("Xylo","Talahassee","FL",99989,"South",4)

print ex.__gt__(ex3)

