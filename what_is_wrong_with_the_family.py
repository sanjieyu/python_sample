# Author:Yi Sun(Tim) 2023-5-10

'''
Michael always knew that there was something wrong with his family. Many strangers were introduced to him as part of it.
Michael should figure this out. He's spent almost a month parsing the family archives. He has all father-son connections of his entire family collected in one place.
With all that data Michael can easily understand who the strangers are. Or maybe the only stranger in this family is Michael? Let's see.
You have a list of family ties between father and son. Each element on this list has two elements. The first is the father's name, the second is the son's name.
All names in the family are unique. Check if the family tree is correct. There are no strangers in the family tree. All connections in the family are natural.
Input: A list of lists. Each element has two strings. The list has at least one element
Output: Bool. Is the family tree correct.
'''

def is_family(tree: list[list[str]]) -> bool:
    family = dict()
    for member in tree:
        if (member[1] in family):
            if family[member[1]] != "":
                return False
            else: family[member[1]] = member[0]
        else: family[member[1]] = member[0]
        if (member[0] not in family):
            family[member[0]] = ""
    num = [1 if value == "" else 0 for value in family.values()].count(1)
    if num != 1:
        return False
    for member in family:
        path = set()
        current = member
        path.add(current)
        while family[current] != "":
            if family[current] not in path:
                path.add(family[current])
                current = family[current]
            else:
                return False
    return True

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
      ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == False, 'Can you be a father to your father?'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Jack']
    ]) == False, 'Can you be a father to your brother?'
    assert is_family([
      ['Logan', 'William'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    assert is_family([
      ['Jack', 'Mike'],
      ['Logan',  'Mike'],
      ['Logan', 'Jack'],
    ]) == False, 'Two fathers'
    print("Looks like you know everything. It is time for 'Check'!")