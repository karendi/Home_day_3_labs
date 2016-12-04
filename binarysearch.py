class List(object):
    def __init__(self , a , b):
        #a is the length of the list to be created
        #b is the step or difference between consecutive values
        self.a = a
        self.b = b




class BinarySearch(List) :
    def __init__(self ) :
        super().__init__(self , a , b)
        self.length = 0 #returns the number of elements in an array

    def search(self , value):
        results = {}
        """should return a dictionary with count ,
         the number of times the  function iterated
         to find the index in question and the index itself"""


        #generate the list
        new_list = []
        for x in range(self.b , (self.a*self.b ), self.a):
            new_list.append(x)
        return new_list

        #length of the array
        self.length = len(new_list)

        #BinarySearch
        first = 0
        last = (self.length//2) #// absolute division
        found = False

        while first < last and not found:
            mid_point = (first + last)//2
            if new_list[mid_point] == value:
                
                found = True
            else:
                if value < new_list[midpoint]:
                    last = mid_point - 1
                else:
                    first = midpoint + 1
        return found
