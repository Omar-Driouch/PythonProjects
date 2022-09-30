# searching for the Two Sum of target number using hashmap algorithm

def Search_by_Map(List, Target):
    array = [0] * len(List)
    a = 0
    b = 0
    for index, element in enumerate(List):

        if Target - element != array[index]:
            array[index] = Target - element
            for index2, element2 in enumerate(array):
                if element2 == element:
                     a = index
                     b = index2



    return ("The Sum  Target found at Index\nIndex(1) = " + str(a) + " and Index(2) = " +str(b)+" \nand that means List["+str(List[a])+"] + List["+str(List[b])+"] = "+ str(List[a]+List[b]) )


list = [2, 7, 3, 4, 5, 6, 7, 8, 9]

print(Search_by_Map(list, 6))
