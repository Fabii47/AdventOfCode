with open('input.txt', 'r') as file:
    lines = file.readlines()
    
    #Time:        54     70     82     75
    #Distance:   239   1142   1295   1253
    time = [int(t) for t in lines[0].split()[1:]]
    dist = [int(t) for t in lines[1].split()[1:]]
    move = [ 0, 0, 0, 0]
    
    
    for i in range(len(time)):
        for t in range(time[i]):
            velocity = t
            leftOverTime = time[i] - t
            distanceReached = velocity * leftOverTime
            if distanceReached > dist[i]:
                move[i] += 1
                
    print(move)
    
    product = 1
    for m in move:
        product *= m
        
    print(product)
        
    