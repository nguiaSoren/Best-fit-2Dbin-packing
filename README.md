# Best-fit-2Dbin-packing
Best-fit 2Dbin packing

This is a Best-fit 2Dbinpackingalgorithm.

We are given several types of products, several types of box with their prices and the total number of units of each product that must be put in the box.

This algorithm will select the best suitable boxes for the given product list. It will select the best boxes according to the dimensions of the products ( Height and length ), and the prices of the boxes.
Then it will add each unit of each product in the appropriate box

for example, we got:

product_Types_list = [Product("P0",40,340,2), Product("P1",100,10,10)]

quantityProducts = [100,10]

box_Types_list = [Box("B0",100,700,100), Box("B1",100,700,100)]


the program will add every products in corresponding boxes

![0](https://user-images.githubusercontent.com/63113307/155463805-c6bda98b-5b38-4fe2-b127-c5c586c90e07.jpg)


![1](https://user-images.githubusercontent.com/63113307/155463817-5ce051fa-c510-413f-93cb-f54e23698334.jpg)


