def change_third_pixel():
    pass
def check_second_pixel():
    pass


import georay
collection = georay.collection('./Dataset/my_collection')
new_collection = collection.map(change_third_pixel, collection)
new_collection = collection.filter(check_second_pixel, collection)



