def solution(players, callings):
    rankDic = {}
    playerDic = {}
    
    for i, player in enumerate(players):
        rankDic[i] = player
        playerDic[player] = i
        
    for callPlayer in callings:
        currentRank = playerDic[callPlayer]
        prevRank = currentRank - 1
        prevPlayer = rankDic[prevRank]
        
        playerDic[callPlayer], playerDic[prevPlayer] = playerDic[prevPlayer], playerDic[callPlayer]
        rankDic[currentRank], rankDic[prevRank] = rankDic[prevRank], rankDic[currentRank]
    
    return [rankDic[i] for i in range(len(players))]