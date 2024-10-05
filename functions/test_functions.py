def getPrecipitationData(data):
    try:
        total_precipitation = 0
        for parameter_data in data['data']:
            if parameter_data['parameter'] == 'precip_1h:mm':    #mm/1h
                for location in parameter_data['coordinates']:
                    for entry in location['dates']:
                        total_precipitation+=entry['value']
        
        return total_precipitation

    except KeyError:
        raise ValueError("Precipitation data not found in the response")

def getEvaporationData(data):
    try:
        evaporation = data.get('evaporation', 0)
        return evaporation
    except KeyError:
        raise ValueError("Evaporation data not found in the response")

def getAtmosphericPressureData(data):
    try:
        pressure = data.get('pressure', 1013.25)
        return pressure
    except KeyError:
        raise ValueError("Atmospheric pressure data not found in the response")

def getAirDensityData(data):
    try:
        density = data.get('air_density', 1.225)
        return density
    except KeyError:
        raise ValueError("Air density data not found in the response")

def getCloudData(data):
    try:
        cloud_cover = data.get('cloud_cover', 0)
        return cloud_cover
    except KeyError:
        raise ValueError("Cloud cover data not found in the response")

def getAtmosphericStabilityData(data):

   # data (dict): JSON data from API

    try:
        stability_index = data.get('stability_index', None)
        if stability_index is None:
            raise ValueError("Atmospheric stability data not found")
        return stability_index
    except KeyError:
        raise ValueError("Atmospheric stability data not found in the response")

