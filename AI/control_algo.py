from .weather_ai import xgb


def control_algo(precipitation, max_temp, min_temp, wind):
    usr_input = [[precipitation, max_temp, min_temp, wind]]
    ot = xgb.predict(usr_input)

    if ot == 0:
        return "Drizzle"
    elif ot == 1:
        return "Fog"
    elif ot == 2:
        return "Rain"
    elif ot == 3:
        return "Snow"
    else:
        return "Sun"
