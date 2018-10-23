#() + () = ()()                                     # => [combine]
#((())) + () = ((())())                             # => [absorb-right]
#() + ((())) = (()(()))                             # => [absorb-left]
#(())(()) + () = (())(()())                         # => [combined-absorb-right]
#() + (())(()) = (()())(())                         # => [combined-absorb-left]
#(())(()) + ((())) = ((())(())(()))                 # => [absorb-combined-right]
#((())) + (())(()) = ((())(())(()))                 # => [absorb-combined-left]
#() + (()) + ((())) = (()()) + ((())) = ((()())(()))# => [left-associative]

def count(S): 
    current_max = 0
    max = 0
    n = len(S) 
  
    # Traverse the input string 
    for i in xrange(n): 
        if S[i] == '(': 
            current_max += 1
  
            if current_max > max: 
                max = current_max 
        elif S[i] == ')': 
            if current_max > 0: 
                current_max -= 1
            else: 
                return -1
  
    # finally check for unbalanced string 
    if current_max != 0: 
        return -1
  
    return max

def solve(tings):
    #print 'length: ',len(tings)
    if len(tings) == 1:
        return tings
    elif len(tings)==2:
        left = tings[0]
        right = tings[1]
        print 'solving: ',left, right
        cl= count(left)
        cr= count(right)
        if cl==cr and cl==1:
            return left+right
        if cl==cr:
            return left+right
        if cl < cr:
            return '('+left+right[1:]
        if cl > cr:
            return left[:-1]+right+')'
    else:
        left = tings[0]
        right = tings[1]
        print 'solving: ',left, right
        cl= count(left)
        cr= count(right)
        if cl==cr and cl==1:
            return solve([left+right]+tings[2:])
        if cl==cr:
            return solve([left+right]+tings[2:])
        if cl < cr:
            return solve(['('+left+right[1:]]+tings[2:])
        if cl > cr:
            return solve([left[:-1]+right+')']+tings[2:])
        

while 1:
    a = raw_input()
    b=solve(a.split(' + '))
    print b
