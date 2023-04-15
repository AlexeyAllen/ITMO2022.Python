from PIL import Image, ImageDraw

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WINDOWWIDTH = 300
WINDOWHEIGHT = 300
GRIDWIDTH = 100
GRIDHEIGHT = 100
RW = WINDOWWIDTH / GRIDWIDTH
RH = WINDOWHEIGHT / GRIDHEIGHT
generations = 50


def initialConfiguration():
    gridImage = Image.open('gridImage.png')
    rgb_im = gridImage.convert('RGB')
    GRIDWIDTH, GRIDHEIGHT = rgb_im.size

    grid = [[0] * GRIDWIDTH for i in range(GRIDHEIGHT)]
    for x in range(GRIDWIDTH):
        for y in range(GRIDHEIGHT):
            pixVal = rgb_im.getpixel((x, y))
            if pixVal == BLACK:
                grid[x][y] = 1
            else:
                grid[x][y] = 0
    return grid


def tick(oldGrid):
    newGrid = [[0] * GRIDWIDTH for i in range(GRIDHEIGHT)]
    for n in range(0, generations):
        for x in range(1, GRIDWIDTH - 1):
            for y in range(1, GRIDHEIGHT - 1):
                newGrid[x][y] = oldGrid[x][y]
                neighbours = 0
                if oldGrid[x - 1][y - 1] == 1:
                    neighbours += 1
                if oldGrid[x][y - 1] == 1:
                    neighbours += 1
                if oldGrid[x + 1][y - 1] == 1:
                    neighbours += 1
                if oldGrid[x + 1][y] == 1:
                    neighbours += 1
                if oldGrid[x + 1][y + 1] == 1:
                    neighbours += 1
                if oldGrid[x][y + 1] == 1:
                    neighbours += 1
                if oldGrid[x - 1][y + 1] == 1:
                    neighbours += 1
                if oldGrid[x - 1][y] == 1:
                    neighbours += 1

                if oldGrid[x][y] == 1:
                    if neighbours == 2 or neighbours == 3:
                        newGrid[x][y] = 1
                    else:
                        newGrid[x][y] = 0
                elif neighbours == 3:
                    newGrid[x][y] = 1
                else:
                    newGrid[x][y] = 0
        return newGrid


def drawField(newGrid):
    final_image = Image.new('RGB', (1000, 1000), (255, 255, 255))
    draw = ImageDraw.Draw(final_image)

    for i in range(0, GRIDWIDTH):
        for j in range(0, GRIDHEIGHT):
            if (newGrid[i][j] == 1):
                draw.rectangle((i * 10, j * 10, i * 10 + 10, j * 10 + 10), BLACK)
            elif (newGrid[i][j] > 1):
                draw.rectangle((i * 10, j * 10, i * 10 + 10, j * 10 + 10), WHITE)

    final_image.show()
    final_image.save('life.png')


def main():
    drawField(tick(initialConfiguration()))


if __name__ == "__main__":
    main()
