b= int(input("Enter the no of cities"))
mat = []

for i in range(0,b,1):
    c= []
    for j in range(0,b,1):
        if(i!=j):
            m = int(input("Enter the distance of city "+str(i)+" to city "+str(j)))
            c.append(m)
        else:
            m = 0
            c.append(m)
    mat.append(c)

for i in range(0,b,1):
    for j in range(0,b,1):
        print(mat[i][j],end=" ")
    print()
from random import *


def fitness(orig, sort):
    fitness = 0
    j = 0
    for i in range(0, len(sort), 1):
        fitness = fitness + orig[j][sort[i]]
        j = sort[i]
    fitness = fitness + orig[sort[len(sort) - 1] ][0]
    return fitness


class crossover(object):

    def __init__(self,parent1,parent2):
        self.parent1 = parent1
        self.parent2 = parent2
    def getchild(self,parent1,parent2):
        crossover_point = randint(0,len(parent1)-1)
        child = []
        child1 = []
        child2 = []
        for i in range(crossover_point,len(parent1),1):
            child.append(parent1[i])
        child1 = [x for x in parent2 if x not in child]
        import random
        random.shuffle(child)
        for i in range(0,len(child),1):
            child1.append(child[i])
        child = []
        for i in range(crossover_point,len(parent2),1):
            child.append(parent2[i])
        child2 = [x for x in parent1 if x not in child]
        random.shuffle(child)
        for i in range(0,len(child),1):
            child2.append(child[i])
        child = []
        child.append(child1)
        child.append(child2)
        return child
class mutation(object):
    def __init__(self,child):
        self.child = child
    def domutation(self,child):
        mut_crossover = randint(0, len(child[0][0]) - 2)
        shuffle(child[:][:][mut_crossover:len(child[0][0])])
        return child
rescount = 0
resultant = [[]]
while(rescount<=10):
            count = 0
            myarr = []
            for i in range(0,100,1):
                ra = []
                for i in range(1, b, 1):
                    ra.append(random())
                import numpy
                ra = numpy.array(ra)

                sort_index = numpy.argsort(ra)
                first = randint(0, b - 2)
                last = randint(first, b - 1)

                
                arr1 = []
                for i in range(first, last, 1):
                    arr1.append(i)
                arr2 = [x for x in range(0, b, 1) if x not in arr1]
                
                newarr = [x+1 for x in sort_index]
                
                myarr.append(newarr)
                count = count+1
                

            perarr =[]
            for i in range(0,100,1):
                score = fitness(mat,myarr[i])
                perarr.append(score)
                
            li=[]
            original_arr =[]
            myoriginalchild=[]
            for i in range(0,len(perarr),1):
                if(perarr[i]==min(perarr)):
                    li.append(i)
                    original_arr.append(myarr[i])
          
            print("original array ",original_arr)
            for i in range(0,len(original_arr)-1,1):
                mychild = crossover(original_arr[i],original_arr[i+1])
                myoriginalchild.append(mychild.getchild(original_arr[i],original_arr[i+1]))
            
            t= myoriginalchild
            
            mutation_func = mutation(myoriginalchild)
            new_mut = mutation_func.domutation(myoriginalchild)
            
            result = []
            myfit = 30238293
            for i in range(0,len(new_mut),1):
                for j in range(0,2,1):

                    if(myfit>fitness(mat,new_mut[i][j])):
                        result.append(new_mut[i][j])
                        myfit=fitness(mat,new_mut[i][j])


            print(fitness(mat,result[0]))
            origcount = result
            if(origcount==resultant):
                rescount = rescount+1
            else:
                resultant = origcount

print("result is",result)

print("===================================================OUTPUT=================================")
print("first travel city 0 then travel ")
for i in range(0,len(result[0]),1):
    print("city ",result[0][i]," then travel ")
print("then from city ",result[0][i]," travel back to city 0 ")
print("the total distance covered by salesman is ",fitness(mat,result[0]))
print("===========================================================================================")
