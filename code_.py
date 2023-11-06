from georay import *

collection = Collection('./Dataset/')
new_collection = collection.map_geo(pixel3,collection.list)
new_collection2 = collection.map_geo(filter23,collection.list)
new_collection.print_geo()
new_collection2.print_geo()
