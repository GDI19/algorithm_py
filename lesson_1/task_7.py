print('Введите три стороны чтобы узнать какой это треугольник')
x = int(input('Введите 1-ю сторону: '))
y = int(input('Введите 2-ю сторону: '))
z = int(input('Введите 3-ю сторону: '))

if x + y <= z or x + z <= y or y + z <= x:
    print('Из данных сторон нельзя построить треугольник')
else:
    if x == y:
        if y == z:
            print('Треугольник равносторонний')
        else:
            print('Треугольник равнобедренный')
    elif x == z:
        print('Треугольник равнобедренный')
    elif y == z:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')