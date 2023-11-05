
from pyspark.sql import SparkSession
import numpy as np
import pandas as pd

from typing import Iterator

from PIL import Image

from pyspark.sql.types import StructType, StructField, ArrayType, IntegerType

SparkSession.builder.appName("dummy_workload").master("spark://TotallyNormalPC:7077").getOrCreate()


class ImageBatch:
    def __init__(self, master_port, file_dir):
        # initialize a SparkSession
        self.spark = SparkSession.builder.appName("dummy_workload").master(master_port).getOrCreate()
        df = self.spark.read.format("image").option("dropInvalid", True).load(file_dir)
        self.df = df.select("image.*")

    def make_udf(self, func, args, out_col_name):
        # make a pandas iterator function from a function
        def udf_func(dataframe_batch_iterator: Iterator[pd.DataFrame]) -> Iterator[pd.DataFrame]:
            for dataframe_batch in dataframe_batch_iterator:
                dataframe_batch[out_col_name] = dataframe_batch.apply(func, args=args, axis=1)
                yield dataframe_batch
        return udf_func

    def map(self, func, args, out_col_name):
        # apply func on each image, and return a new ImageBatch, with a new schema
        new_schema = StructType(self.df.schema.fields + [StructField(out_col_name, ArrayType(IntegerType()), True)])
        new_df = self.df.mapInPandas(self.make_udf(func, args, out_col_name), new_schema)
        new_Image_Batch = self
        new_Image_Batch.df = new_df
        return new_Image_Batch

    def printSchema(self):
        self.df.printSchema()

    def show(self, *args, **kwargs):
        self.df.show(*args, **kwargs)

# Following is sample usage of ImageBatch

# file_dir = "Major-Players-in-Cloud-Computing.png"

# def convert_bgr_array_to_rgb_array(img_array):
#     B, G, R = img_array.T
#     return np.array((R, G, B)).T

# def resize_img(img_data, resize=True):
#     mode = 'RGBA' if (img_data.nChannels == 4) else 'RGB' 
#     img = Image.frombytes(mode=mode, data=img_data.data, size=[img_data.width, img_data.height])
#     img = img.convert('RGB') if (mode == 'RGBA') else img
#     img = img.resize([224, 224], resample=Image.Resampling.BICUBIC) if (resize) else img
#     # turn the first pixel's rgb values to 1
#     img.putpixel((0, 0), (1, 1, 1))
#     arr = convert_bgr_array_to_rgb_array(np.asarray(img))
#     arr = arr.reshape([224*224*3]) if (resize) else arr.reshape([img_data.width*img_data.height*3])
#     return arr

# image_df = ImageBatch("spark://TotallyNormalPC:7077", file_dir)
# resized_df = image_df.map(resize_img, (True,), "data_as_resized_array")
# resized_df.printSchema()
# another_resized_df = resized_df.map(resize_img, (False,), "data_as_array")
# another_resized_df.printSchema()
# another_resized_df.show(20, truncate=True)
