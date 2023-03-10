from qgis.core import QgsApplication, QgsVectorLayer
#Starting a QGIS application
qgishome = 'C:/OSGeo4W/apps/qgis/'
QgsApplication.setPrefixPath(qgishome, True)
app = QgsApplication([], False)
app.initQgis()
fileName = 'C:/temp/dronephotos.shp'
vlayer = QgsVectorLayer(fileName, 'point', 'ogr')
print(vlayer.isValid())
