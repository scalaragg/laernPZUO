def circle_area(radius):
    area = radius*radius*3.14
    return area
circle = circle_area(2)
print(circle)


def max_of_tree(a,b,c):
    max = 0
    if a>max:
        max=a
    
    if max<b:
        max=b
    
    if max<c:
        max=c
    print(max)
max_of_tree(8,15,3)
