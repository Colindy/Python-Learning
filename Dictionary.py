##  Dictionary Fun

alien1 = {'xpos' : 0, 'ypos' : 0, 'speed' : 'slow'}

if alien1['speed'] == 'slow':
    xinc = 1
elif alien1['speed'] == 'medium':
    xinc = 2
elif alien1['speed'] == 'fast':
    xinc = 3

alien1['xpos'] = (alien1['xpos'] + xinc)

print(alien1)