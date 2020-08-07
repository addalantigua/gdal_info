from lib2to3.pgen2 import driver

from osgeo import gdal

# fn stores the Location for the stitched image
fn = "/Users/addalantigua/Desktop/rachels  folder/image.tif"
# fn2 will hold the compressed image
fn2 = "/Users/addalantigua/Desktop/rachels  folder/image2.tif"
# Opens the dataset and saves it to dataset
dataset = gdal.Open(fn)
# checks to see if data opened correctly
if not dataset:
    print("no good")

# attempt at compressing file
#src_ds = gdal.Open(fn)
#dst_ds = gdal.Translate(fn2, src_ds, strict=0, options=["TILED=YES", "COMPRESS=PACKBITS"])


# prints information about image
print("Driver: {}/{}".format(dataset.GetDriver().ShortName,
                            dataset.GetDriver().LongName))
print("Size is {} x {} x {}".format(dataset.RasterXSize,
                                    dataset.RasterYSize,
                                    dataset.RasterCount))
print("Projection is {}".format(dataset.GetProjection()))

geotransform = dataset.GetGeoTransform()
if geotransform:
    print("Origin = ({}, {})".format(geotransform[0], geotransform[3]))
    print("Pixel Size = ({}, {})".format(geotransform[1], geotransform[5]))

# More  in depth information
print (gdal.Info(dataset))


