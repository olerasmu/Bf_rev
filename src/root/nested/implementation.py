'''
Created on 25. mars 2014

@author: olerasmu
'''
import math
class Bf_reverse(object):
    
    def __init__(self, filepath = None):
        self.filepath = filepath
        
        
    fileTab = []
    butterflyTab = []
    
    
    def fileSize(self):
        tempFile = open(self.filepath, 'rb')
        tempFile.seek(0,2)
        size = tempFile.tell()
        tempFile.seek(0,0)
        tempFile.close()
        return size
    
    #Slit the file into blocks of 128 bit (16*8 bytes)    
    def blockifyFile(self):
        with open(self.filepath, 'r') as newfile:
            bytes = str(newfile.read(16))
            while bytes:
                self.butterflyTab.append(bytes)
                print bytes, " byte"
                bytes = str(newfile.read(16))
            #print ("File has been divided into blocks")
            
    def blockifyFileTwo(self):
        with open(self.filepath, 'r') as newfile:
            for i in range(0, self.fileSize()/16):
                byte = newfile.read(16)
                print byte, " byte"
                self.butterflyTab.append(byte)
            
    def fileifyBlocks(self):
        #self.fileTab.pop()
        with open('rev_hourglass.txt', 'a') as rev_hourglass_file:
            #count = 0
            for byte in self.fileTab:
                rev_hourglass_file.write(byte)
                #count += 1    
                #print "This is the nr 1 count: ", count
    
    #Initialize the butterfly function. Variable j is controlled from here
    def initiateButterfly(self, d, n):
        self.fileTab = [None]*n
        print (self.fileTab)
        for j in range(d, 0, -1):
            print ("Its j: ", j)
            #print "this is j: ", j
            self.executeButterfly(j, n, d)
    
    count = 0
    #Execute the butterfly algorithm
    def executeButterfly(self, j, n, d):
        #print ("execute")
        #print ("this is j: ", j)    
        for k in range(int((n/math.pow(2, j))-1), -1, -1):
            #print ("this is k: ", k)
            if j == d:
                for i in range(int(math.pow(2, j-1)), 0, -1):
                    indexOne = int(i+k*math.pow(2, j))-1
                    indexTwo = int(i+k*math.pow(2, j)+math.pow(2, j-1))-1
                    #print indexOne, " ", indexTwo
                    self.count += 1
                    self.w(self.butterflyTab[indexOne], self.butterflyTab[indexTwo], indexOne, indexTwo)
            else:   
                for i in range(int(math.pow(2, j-1)), 0, -1):
                    indexOne = int(i+k*math.pow(2, j))-1
                    indexTwo = int(i+k*math.pow(2, j)+math.pow(2, j-1))-1
                    #print indexOne, " ", indexTwo, " from else you know"
                    self.count += 1
                    self.w(self.fileTab[indexOne], self.fileTab[indexTwo], indexOne, indexTwo)
                #print ("this is i: ", i)
                #print ("this is index one: ", indexOne, " and this is index two: ", indexTwo)
                #===============================================================
                # temp = [int(i+k*math.pow(2, j))-1, int(i+k*math.pow(2, j)+math.pow(2, j-1))-1]
                # print temp
                #===============================================================
        #print ("count: ", self.count)
        #print (self.butterflyTab)      
    
    count = 0
    def w(self, blockOne, blockTwo, indexOne, indexTwo):
        self.count += 1
        self.fileTab[indexOne] = blockOne
        self.fileTab[indexTwo] = blockTwo
        #print self.count
        
bf_rev = Bf_reverse(filepath = 'C:\\Users\\olerasmu\\Documents\\workspace\\Butterfly\\src\\root\\nested\\bf_hourglass.txt')
print bf_rev.fileSize()
#bf_rev.blockifyFile()
bf_rev.blockifyFileTwo()
print "Butterflytab: ", bf_rev.butterflyTab
print "filetab: ", bf_rev.fileTab
n = len(bf_rev.butterflyTab)
print "This is n", n
d = int(math.log(n, 2))

bf_rev.initiateButterfly(d, n)
print bf_rev.filepath
print "This is filetab after: ", bf_rev.fileTab
print len(bf_rev.fileTab)
bf_rev.fileifyBlocks()

