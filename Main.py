import GEN_LS

# размер "клетки"
step_size = 10
# точка начала желаемая, может быть смещена
start_point = [305, 160]
# Границы рабочей области, мм
x_max = 420
x_min = 210
y_max = 310
y_min = 20
# Высота
z_draw = -50

paper_width = (x_max - x_min) / step_size
paper_height = (y_max - y_min) / step_size
print(paper_width, paper_height)

filename = 'NEW_PROG.LS'
turtle = [1, 1, 4, 4, 4, 4, 1, 3, 3, 1, 3,
          1, 1, 1, 1, 4, 1, 4, 4, 4, 2, 4,
          2, 3, 2, 2, 2, 2, 4, 2, 3, 2,
          3, 3, 3, 2, 3, 3]
ship = [1, 4, 1, 4, 1, 4, 1, 4, 4, 4,
        2, 2, 2, 4, 1, 1, 1, 1, 1, 4,
        2, 4, 2, 4, 2, 2, 2, 2, 2, 2,
        2, 3, 2, 3, 2, 3, 1, 1, 1, 1,
        1, 3, 3, 3, 3, 3, 3, 3]
deer = [3, 3, 1, 1, 3, 1, 3, 3, 1, 4, 1, 3, 1, 4,
        1, 3, 1, 4, 4, 2, 2, 2, 2, 4, 2, 4, 4, 4,
        1, 4, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 2,
        3, 3, 2, 4, 4, 4, 4, 4, 4, 2, 3, 3, 2, 3,
        3, 2, 2, 2, 4, 4, 2, 4, 4, 2, 3, 3, 3, 3,
        3, 2, 3, 3, 3, 3, 2]
square = [1, 3, 2, 4]


# 1 - x+
# 2 - x-
# 3 - y+
# 4 - y-
# position[0] - x
# position[1] - y


class Picture:
    def __init__(self, start_point, path):
        self.start_point = start_point
        self.path = path

    def size(self):
        w = 0
        h = 0
        width_max = 0
        width_min = 0
        height_max = 0
        height_min = 0
        for i in self.path:
            if i == 1:
                w = w + 1
            if i == 2:
                w = w - 1
            if i == 3:
                h = h + 1
            if i == 4:
                h = h - 1
            if w > width_max:
                width_max = w
            elif w < width_min:
                width_min = w
            elif h > height_max:
                height_max = h
            elif h < height_min:
                height_min = h
        width = abs(width_max - width_min)
        height = abs(height_max - height_min)

        return width, height


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def gen_points(img):
    points = [img.start_point]
    pos = Position(img.start_point[0], img.start_point[1])
    size_w, size_h = img.size()
    if size_w > paper_width or size_h > paper_height:
        print('Не влезет')
    for i in img.path:
        if i == 1:
            pos.x = pos.x + step_size
        if i == 2:
            pos.x = pos.x - step_size
        if i == 3:
            pos.y = pos.y + step_size
        if i == 4:
            pos.y = pos.y - step_size
        if pos.x > x_max:
            for p in points:
                p[0] = p[0] - step_size
            pos.x = pos.x - step_size
        elif pos.x < x_min:
            for p in points:
                p[0] = p[0] + step_size
            pos.x = pos.x + step_size
        elif pos.y > y_max:
            for p in points:
                p[1] = p[1] - step_size
            pos.y = pos.y - step_size
        elif pos.y < y_min:
            for p in points:
                p[1] = p[1] + step_size
            pos.x = pos.x + step_size
        points.append([pos.x, pos.y])
    return points


image2 = Picture(start_point=start_point, path=ship)

print(gen_points(image2))
# GEN_LS.make_file(gen_points(image2), filename=filename)

print(image2.size())
