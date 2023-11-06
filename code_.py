from georay import *

from georay import Collection

collection = Collection('./Dataset/')
images = collection.extract()
new_images = collection.map_geo(pixel3,images)
new_images2 = collection.map_geo(filter23,new_images)
collection.print_geo(new_images2)




