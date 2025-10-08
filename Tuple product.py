def product_of_tuple(input_tuple):
  product = 1
  for number in input_tuple:
    product *= number
  return product

product1 = product_of_tuple((4, 3, 2, 2, -1, 18))
product2 = product_of_tuple((2, 4, 8, 8, 3, 2, 9))

print(product1)
print(product2)