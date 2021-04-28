# https://leetcode.com/problems/robot-return-to-origin/

def judgeCircle(moves):
    x = y = 0
    for char in moves:
        if char == 'U':
            y += 1
        elif char == 'D':
            y -= 1
        elif char == 'L':
            x -= 1
        else:
            x += 1
    return x == y == 0

moves = "DRLLDLLRURLURULLLRULLRLULLLDDUDLUUUDLLDLDRLDRURDURRLRDLDRDLDDURDUURLLUUURLDRLUULUUDRDRUDURLLRDRRDLDU"
print(judgeCircle(moves))

# 60ms; faster than 56%
# 14.4MB; less than 30#