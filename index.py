import read
import purchase
import write
again="Y"
while again.upper()=="Y":
    a=read.read_file()
    b=purchase.purchase(a)
    write.over_write(a,b)
    again=input("\nIs any new customer waiting to buy a product? ")
print("\nThank you for shopping!")
print("Please check your invoice for your shopping details, \nWe created a receipt in a text file format for you.")
