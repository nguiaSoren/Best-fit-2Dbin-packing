# Best-fit-2Dbin-packing
Best-fit 2Dbin packing



```diff
+ Best-fit is an online algorithm for bin packing. Its input is a list of items of different sizes. 
+ Its output is a packing - a partition of the items into bins of fixed capacity, 
+ such that the sum of sizes of items in each bin is at most the capacity. Ideally, 
+ we would like to use as few bins as possible, but minimizing the number of bins is an NP-hard problem. 
+ The best-fit algorithm uses the following heuristic:

! It keeps a list of open bins, which is initially empty.
! When an item arrives, it find a bin with the maximum load into which the item can fit, if any.
! If such a bin is found, the new item is placed inside it.
! Otherwise, a new bin is opened and the coming item is placed inside it.
```

product_Types_list = [Product("P0",40,340,2), Product("P1",100,10,10)]

product_Types_list1 = [Product("P0",74,114,3), Product("P1",70,4000,5),Product("P2",4000,1000,1),Product("P3",157,143,1), Product("P4",145,330,4)] 

quantityProducts = [100,10]

quantityProducts1 = [85,49,61,41,18]


box_Types_list = [Box("B0",100,700,100), Box("B1",100,700,100)]

box_Types_list1 = [Box("B0",8000,3000,10), Box("B1",3090,4722,10), Box("B2",9009,2046,10), Box("B3",766,3639,10)]



![0](https://user-images.githubusercontent.com/63113307/155463805-c6bda98b-5b38-4fe2-b127-c5c586c90e07.jpg)


![1](https://user-images.githubusercontent.com/63113307/155463817-5ce051fa-c510-413f-93cb-f54e23698334.jpg)


