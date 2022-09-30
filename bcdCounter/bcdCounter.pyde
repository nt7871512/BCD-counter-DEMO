def setup():
    size(500,500)
    background(51)
    global n 
    n = 0
    
def bcdCodeGenerator(j):
    bcd = []
    for i in bin(j)[2:]:
       bcd.append(int(i))
       
    while(len(bcd)<4 ):
        bcd.insert(0,0)
    
    return bcd

def getBCD(bcd):
    expression = {}
    expression['a'] = bcd[2] | bcd[0] | (bcd[1] & bcd[3]) | ( bcd[1] |  bcd[3])^1    
    expression['b'] = bcd[1]^1 | (bcd[2]|bcd[3])^1 | (bcd[2]&bcd[3])
    expression['c'] = bcd[2]^1 | bcd[3] | bcd[1]
    expression['d'] = (bcd[1] | bcd[3])^1 | bcd[0] | bcd[2]&(bcd[3]^1) | (bcd[1]^1)&bcd[2] | bcd[1]&bcd[3]&(bcd[2]^1)
    expression['e'] = (bcd[3] | bcd[1])^1 | (bcd[2] & (bcd[3]^1))
    expression['f'] = (bcd[0]) | ( bcd[3]^1)&bcd[1] | (bcd[2] | bcd[3])^1 | bcd[1] & (bcd[2]^1)
    expression['g'] = (bcd[0]) | bcd[1] & (bcd[2]^1) | (bcd[1]^1) & bcd[2] | bcd[2]&(bcd[3]^1)
    
    return expression


def drawSegment(num):
    code = bcdCodeGenerator(num)
    expresstion = getBCD(code)
    on = color(219, 52, 52)
    colorSegment = {0:10 , 1:on}
        
    # a
    fill(colorSegment[expresstion['a']])
    rect(50, 25, 100 , 20, 10);
    
    # b
    fill(colorSegment[expresstion['b']])
    rect(150, 40, 20 , 100, 10);
    
    # c
    fill(colorSegment[expresstion['c']])
    rect(150, 140, 20 , 100, 10);
    
    # d
    fill(colorSegment[expresstion['d']])
    rect(50, 235, 100 , 20, 10);
    
    # e
    fill(colorSegment[expresstion['e']])
    rect(30, 140, 20 , 100, 10);
    
    # f
    fill(colorSegment[expresstion['f']])
    rect(30, 40, 20 , 100, 10);
    
    # g
    fill(colorSegment[expresstion['g']])
    rect(50, 130, 100 , 20, 10);
    
global bool
bool = True

def draw():
    global bool
    global n
    background(51)
    if bool:
        n %= 10
        drawSegment(n)
        n += 1
        """
        if n>9:
            bool = False
    else:
        n -= 1
        n %= 10
        drawSegment(n)
        
        if n==0:
            bool = True   
        """
    delay(1000)
        
    
    
    
    
    
