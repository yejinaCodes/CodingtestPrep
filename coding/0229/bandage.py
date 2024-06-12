def solution(bandage, health, attacks):
    answer = 0
    
    fullhealth = health
    time = 0
    loop = bandage[0]
    sequential_keeper = 0
    

    while(len(attacks)>0):
        #health가 최대치가 넘지 않도록 유지해주기
        if health > fullhealth:
            health = fullhealth

        time += 1
        sequential_keeper += 1
        if(attacks[0][0] == time):
            time_attack, kill = attacks.pop(0)
            health -= kill
            sequential_keeper = 0
        elif(sequential_keeper == loop):
            health += (loop + bandage[1])
            sequential_keeper = 0
        elif (health<fullhealth):
            health += bandage[1]   


    if(health>0):
        return (health)
    else:
        return (-1)
    
    #return answer