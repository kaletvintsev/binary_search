def binary_search(sorted_list, value):
    
    low = 0
    hight = len(sorted_list)-1
    
    while low <= hight:
    
        middle = (low + hight) // 2
        gues = sorted_list[middle]
        
        if value == gues:
            return gues
        elif gues < val:
            low = middle + 1
        elif gues > val:
            hight = middle - 1
            
    return None
         
