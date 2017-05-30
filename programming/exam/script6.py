import arcpy, os
city = arcpy.GetParameterAsText(0)
country = arcpy.GetParameterAsText(1)
Workspace = arcpy.GetParameterAsText(2)

arcpy.MakeFeatureLayer_management(city, 'city')
arcpy.MakeFeatureLayer_management(country, 'country')

university = arcpy.SelectLayerByAttribute_management("city", "NEW_SELECTION", '"UNIVERSITY"=1')
intersection = arcpy.SelectLayerByLocation_management("country", "INTERSECT", university)

arcpy.CreateFeatureclass_management(Workspace, 'out', "POINT", spatial_reference="city")

outFc=os.path.join(Workspace, 'out.shp')
arcpy.AddField_management(os.path.join(Workspace, 'out.shp'), "CITY", "TEXT")
arcpy.AddField_management(os.path.join(Workspace, 'out.shp'), "AREA", "DOUBLE")
arcpy.AddField_management(os.path.join(Workspace, 'out.shp'), "POPULATION", "INTEGER")

with arcpy.da.InsertCursor(outFc, ["SHAPE@XY","CITY", "POPULATION"]) as cursorInsert, arcpy.da.SearchCursor(university, ["SHAPE@XY","NAME", "POPULATION"]) as cursorSearch:
    for row in cursorSearch:
        cursorInsert.insertRow(row)
    del(cursorInsert)
    del(cursorSearch)


area = []
with  arcpy.da.SearchCursor(intersection, "AREA") as cursorSearch:
    for row in cursorSearch:
        area.append(row[0])
    del (cursorSearch)



cursorUpdate =  arcpy.da.UpdateCursor(outFc, "AREA")
i = 0
for row in cursorUpdate:
    try:
        row = area[i]
        arcpy.AddMessage(row)
        cursorUpdate.updateRow([row])
    except:
        pass
    i += 1
del(cursorUpdate)


