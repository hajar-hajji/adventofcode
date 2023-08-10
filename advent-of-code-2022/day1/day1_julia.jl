f = open("day1.txt")
data = read(f, String)
close(f)
data = split(data, "\n\n")
calories = map(x->split(x, "\n"), data)

""" En utilisant !isempty(y), nous nous assurons que y 
n'est pas vide avant de l'utiliser pour autre chose 
(par exemple la conversion en entier avec parse(Int, y))
"""
calories= map(x->filter(y->!isempty(y),x),calories) 
calories= map(x->map(y->parse(Int, y), x), calories)   # convert each element to integer
# ou bien : calories=[parse.(Int, liste) for liste in calories]
liste_sommes=map(y->sum(y),calories)
maximum=reduce(max, liste_sommes)   # reduce car liste_sommes est vector
println(maximum)
