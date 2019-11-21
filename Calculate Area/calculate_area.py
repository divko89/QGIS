uri='C:/Users/PATH_TO_YOUR_FILE/FILENAME.shp' #Set Path to shapefile here
layer = iface.addVectorLayer(uri, 'LAYERNAME', 'ogr')    #Set preffered LAYERNAME

def calculate_attributes():
    with edit(layer):
        for feature in layer.getFeatures():
            feature.setAttribute(feature.fieldNameIndex('AREA'), feature.geometry().area())
            layer.updateFeature(feature)

calculate_attributes()


