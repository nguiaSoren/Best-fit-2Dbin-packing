# Made the 2022-02-28 by OBOUNOU LEKOGO NGUIA Benaja Soren , (gitHub username = nguiaSoren)
class Product:
    def __init__(self, id, H, L,nbStackedMax):
        # H = height of each unit , L = length of each unit
        # nbStackedMax = maximum number of units that can be stacked
        self.id = id
        self.H = H
        self.L = L
        self.nbStackedMax = nbStackedMax 
    def __repr__(self):
        return f" Product H: {self.H}, Product L: {self.L} with nbEmpileMax: {self.nbStackedMax }  \n"
    
# default box class that we have
class Box:
    def __init__(self, id, H, L,priceBox):
        self.id = id
        self.H = H
        self.L = L
        self.priceBox = priceBox

# Container Box ( box we will use to store products)      
class BoxContainer(Box):
    def __init__(self, id, H, L, priceBox , productQuantities, nbStackedMax = []):
        super().__init__(id, H, L, priceBox)
        # copy of product_Types_list; represent the quantity (number of units) of each product in the box
        self.productQuantities = productQuantities
        # number of units of product_Types_list[i] we can stack together ( 1 stack of 3 products for example)
        self.nbStackedMax = nbStackedMax
        # we are looking for the number of unit of product_Types_list[i] we can stack in THIS BOX given the box.H 
        for productType in product_Types_list :
            # (box.H)50 / product.H(20) = 2.5 so 2 units in a stack in this box
            # if number of units of product_Types_list[i] we can stack in this box is above product_Types_list[i].nbStackedMax, take default one
            stackedMax = self.H // productType.H if self.H // productType.H <= productType.nbStackedMax else productType.nbStackedMax
            self.nbStackedMax.append(stackedMax)
    def getRemainingLength(self): 
        # total length of all products in box
        total =  0
        for i, (nbUnits,productCustomStackedMax) in enumerate(zip(self.productQuantities,self.nbStackedMax)):
            # 5 (nbUnits of product[i]) / 2 (nbStackedMax) = 2.5 , so it's 2 + 2 + 1 = 5 ( 3 different stacks), se we need to round up the result 
            #  -(-5//2) = 3 stacks of product_Types_list[i] (each stack contains 2 units of product_Types_list[i] and last stack contains 1 unit)
            nbStackedProducts = -(-nbUnits //productCustomStackedMax) if  productCustomStackedMax != 0 else 0
            # total += ( 3 stack of product_Types_list[i] * product_Types_list[i].L )        - - 
            # for example, 1 unit of product_Types_list[i].L = 40; we have 3 stacks of those - - -
            # so total length of those stacks for product_Types_list[i] is 3*40 = 120
            total += nbStackedProducts * product_Types_list[i].L
        return self.L - total
    def __repr__(self):
        return f" Box id: {self.id}, Box H: {self.H}, Box.L: {self.L}, priceBox: {self.priceBox}, productQuantities: {self.productQuantities} , nbStackedMax: {self.nbStackedMax} \n"


# first Product , id = "P0", height = 74, length = 114, nbStackedMax = 3      
# second Product , id = "P1", height = 4000, length = 1000, nbStackedMax = 1  
product_Types_list = [Product("P0",74,114,3), Product("P1",70,4000,5),Product("P2",4000,1000,1),Product("P3",157,143,1), Product("P4",145,330,4)] 
product_Types_list1 = [Product("P0",40,340,2), Product("P1",100,10,10)]
# list of quantity of products we wanna buy
# we wanna store in boxes 89 units of product_Types_list[0] or 61 units of product_Types_list[2] 
quantityProducts = [85,49,61,41,18]
quantityProducts2 = [100,10]
quantityProducts1 = [1000,1500]
# len(product_Types_list) must be equal to len(quantityProducts)

#box_Types_list = [Box("B0",8000,3000,10), Box("B1",3090,4722,10), Box("B2",9009,2046,10), Box("B3",766,3639,10)]
box_Types_list = [Box("B0",8000,3000,10), Box("B1",3090,4722,10), Box("B2",9009,2046,10), Box("B3",766,3639,10)]
box_Types_list1 = [Box("B0",100,700,100), Box("B1",100,700,100)]
# keep track of number of boxes we bought
# boxBoughtNumberList[0] represents the number of box_Types_list[0] we bought               
boxBoughtNumberList = [0 for _ in range(len(box_Types_list ))]
# Container boxes we have
ourBoxes = []
        
def indices(lst, item):
    # find every indices of an item, even if it's duplicate in list
    return [i for i, x in enumerate(lst) if x == item]

# find perfect box for box_Types_list[index]
def perfectBoxFor(index):
    currentProduct = product_Types_list[index] 
    # find all boxes whose Length is superior to current product length (product_Types_list[index].L)
    # this length is the tresholdL
    tresHoldL = currentProduct.L
    # order indexes by descending order according to length
    biggestLIndexes = [b[0] for b in sorted(enumerate([boxType.L for boxType in box_Types_list]),key=lambda i:i[1],reverse=True)]
    # find all indexes of boxes whose length is superior or equal to tresHoldL
    biggestLIndexes = [i for i in biggestLIndexes if box_Types_list[i].L > tresHoldL ]
    # total height of a FULL stack of product_Types_list[index] 
    # this total height is the tresholdHValue
    tresHoldH = currentProduct.H * currentProduct.nbStackedMax
    # find index(es) of all boxes whose Height is superior or equal to tresHoldH and that are already in our biggestLIndexes 
    biggestHIndexes = [i for i in biggestLIndexes if box_Types_list[i].H > tresHoldH]
    # case no boxes can't sustain maximum maximum height, try with minimum_height (default height of currentProduct)
    if biggestHIndexes == []:
        biggestHIndexes = [i for i in biggestLIndexes if box_Types_list[i].H >= currentProduct.H]
    # Find biggest Length(s) of box in our final found indexes to maximise space;
    # since it is in descending order , we know that biggest length is at index biggestHIndexes[0], but we could have boxes with the same length, that's why we're gonna double check 
    highestIndex = biggestHIndexes[0]
    bestFitBoxesIndexes = [i for i in biggestHIndexes if box_Types_list[i].L ==  box_Types_list[highestIndex].L ]
    # case we got boxes with same length and different heights, take the one with the biggestArea
    biggestAreas = [box_Types_list[i].L * box_Types_list[i].H  for i in bestFitBoxesIndexes]
    biggestAreasIndexes = indices(biggestAreas,max(biggestAreas))
    # take corresponding Box(es) index
    bestFitBoxesIndexes = [bestFitBoxesIndexes[i] for i in biggestAreasIndexes]
    # case we got boxes with same length and height but different prices
    # find lowest priceBox in our bestFitBoxesIndexes
    bestPrice = min([box_Types_list[index].priceBox for index in bestFitBoxesIndexes ])
    # find index corresponding to best price // index of 9 = 0
    priceIndex = [box_Types_list[index].priceBox for index in bestFitBoxesIndexes ].index(bestPrice)
    # apply it to perfect boxIndex
    # [10,15][0] = 10
    perfectBoxIndex = bestFitBoxesIndexes [priceIndex]
    # return perfect box
    return box_Types_list[perfectBoxIndex]

def addInBox(quantityProducts):
    # start adding product in boxes; start with product with biggestArea (descending order)
    # array of indexes of products with biggestAreas in descending order
    areasProduct = [product.L * product.H  for product in product_Types_list]
    IndexSortedByBiggestAreas = [b[0] for b in sorted(enumerate(areasProduct),key=lambda i:i[1],reverse=True)]
    for k in IndexSortedByBiggestAreas:  
        productQuantity = quantityProducts[k]
        # if it's empty, go to next products
        if productQuantity!= 0:
            letProductQuantity = productQuantity
            # fill out our current boxes first before adding to other 
            for i, box in enumerate(ourBoxes):
                # total products = 19, nbStackesMax = 4, totalStackNumber = 4 + 4 + 4 + 4 + 3 = 5 stacks = -(- 19 // 4) = 5 
                totalStackNumber = -(- productQuantity // box.nbStackedMax[k]) if box.nbStackedMax[k] != 0 else 0
                # box.L = 370 , one product.L (one stack.L) = 90; so 4 stacks per box; 4*90 = 360, with remainder of 10
                # 370 // 90 =  4 stacks per box
                nbStackForBox = box.getRemainingLength()  // product_Types_list[k].L
                if nbStackForBox <= 0:
                    continue
                nbStackForBox = totalStackNumber if nbStackForBox > totalStackNumber else nbStackForBox
                productsPerStack = box.nbStackedMax[k]
                nbProductsForBox= nbStackForBox * productsPerStack 
                nbProductsForBox = productQuantity if nbProductsForBox > productQuantity else nbProductsForBox   
                restToAdd = letProductQuantity  - (nbProductsForBox  * (i))
                # restToAdd < 0  means that nbProductsForBox is higher in this box than in others, so (nbProductsForBox * (i)) > letCommandProductQuantity; 
                nbProductsForBox =  restToAdd if restToAdd < nbProductsForBox and restToAdd > 0 else nbProductsForBox 
                ourBoxes[i].productQuantities[k] += nbProductsForBox
                productQuantity  -= nbProductsForBox
                       
            box = perfectBoxFor(k)
            boxIndex = box_Types_list.index(box) 
            # initialize box Container 
            box = BoxContainer(box.id, box.H, box.L, box.priceBox,[0 for _ in range(len(product_Types_list))], [])
            # same operation as previously
            totalStackNumber = -(- productQuantity // box.nbStackedMax[k]) if box.nbStackedMax[k] != 0 else 0
            nbStackForBox , productsPerStack = box.L  // product_Types_list[k].L, box. nbStackedMax[k]
            numberOfBoxes = -(-totalStackNumber  // nbStackForBox )
            # index of boxes
            for i in range(numberOfBoxes):
                nbProductsForBox = nbStackForBox  * productsPerStack
                # numbers left of products to add in a new box
                restToAdd = productQuantity - (nbProductsForBox  * (i))  
                nbProductsForBox =  restToAdd if restToAdd < nbProductsForBox and i == numberOfBoxes-1 else nbProductsForBox 
                container = BoxContainer(box.id,box.H,box.L,box.priceBox,[0 if i != k else nbProductsForBox  for i in range(len(product_Types_list))],[])
                boxBoughtNumberList[boxIndex] += 1
                ourBoxes.append(container)

       
addInBox(quantityProducts)
for j, box in enumerate(ourBoxes):
    print("C"+ str(j))
    print(box)

for j, box in enumerate(box_Types_list):
    strWord = "boxes bought" if boxBoughtNumberList[j] > 1 else "box bought"
    print("Box ID :", box.id , "---", boxBoughtNumberList[j] , strWord) 

