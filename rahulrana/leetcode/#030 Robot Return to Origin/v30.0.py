# https://leetcode.com/problems/robot-return-to-origin/

def judgeCircle(moves):
    x, y = 0, 0
    for char in moves:
        if char == 'U':
            if y != 1:
                y += 1
        elif char == 'D':
            if y != -1:
                y -= 1
        elif char == 'L':
            if x != -1:
                x -= 1
        else:
            if x != 1:
                x += 1
    if x == 0 and y == 0:
        return x, y
    return x, y

moves = "DRLLDLLRURLURULLLRULLRLULLLDDUDLUUUDLLDLDRLDRURDURRLRDLDRDLDDURDUURLLUUURLDRLUULUUDRDRUDURLLRDRRDLDU"
print(judgeCircle(moves))