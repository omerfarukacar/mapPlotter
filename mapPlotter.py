import gmplot

# Harita oluşturulurken zoom yapılması için örnek koordinatlar
first_gmap = gmplot.GoogleMapPlotter(40.965328, 29.0878688, 15)  

# enlem boylam verilerinin kaydedildiği tablo
file_name = 'lat_lon.txt'

with open(file_name, "r") as file:
    lines = file.readlines()

    for line in lines:
        line = line.strip()

        start_latitude = 'latitude:'
        end_latitude = ',longitude:'
        start_longitude = 'longitude:'
        end_longitude = '\n'

        latitude_list = line[line.find(start_latitude) + len(start_latitude):line.rfind(end_latitude)]
        longitude_list = line[line.find(start_longitude) + len(start_longitude):line.rfind(end_longitude)]
        first_gmap.marker(float(latitude_list),float(longitude_list),"cornflowerblue")

# daha iyi çözünürlük ve yazısız harita için google api key alınmalıdır
# https://mapsplatform.google.com/pricing/
first_gmap.apikey = "AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8"  

first_gmap.draw( "first_gmap.html" )  
