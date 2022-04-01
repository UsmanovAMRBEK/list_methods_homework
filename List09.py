def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    l=[fruits.count("apple")]
    if fruits[0]=="apple":
        l.append(0)
    
    if fruits[1]=="apple":
        l.append(1)

    if fruits[2]=="apple":
        l.append(2)

    if fruits[3]=="apple":
        l.append(3)

    if fruits[4]=="apple":
        l.append(4)
    return l
fruits = ["apple", "banana", "apple", "pear", "apple"]
print(main(fruits))