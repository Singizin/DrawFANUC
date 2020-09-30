def first(f, how_much):
    for i in range(1, how_much+1, 1):
        print(i)
        f.write('{num}:L P[{num}] 50mm/sec FINE    ;\n'.format(num=str(i)))
    f.write('/POS\n')


def write_point(f, num, x, y):
    point_string_1 = 'P[{}]{{\n'.format(num)
    point_string_2 = '   GP1:\n'
    point_string_3 = '	UF : 0, UT : 1,		CONFIG : \'N U T, 0, 0, 0\',\n'
    point_string_4 = '	X =   {x}.000  mm,	Y =   {y}.000  mm,	Z =   -50.000  mm,\n'.format(x=x, y=y)
    point_string_5 = '	W =   180.000 deg,	P =      .000 deg,	R =      .000 deg\n'
    point_string_6 = '};\n'
    result = point_string_1 + point_string_2 + point_string_3 + point_string_4 + point_string_5 + point_string_6
    f.write(result)


def make_file(points):
    f = open('NEW_PICTURE.LS', 'a')
    first(f, len(points))
    counter = 1
    for i in points:
        write_point(f, counter, i[0], i[1])
        counter = counter + 1
    f.write('/END\n')
    f.close()
