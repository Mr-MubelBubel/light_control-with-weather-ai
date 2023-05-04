from .weather_ai import xgb


def control_algo(precipitation, max_temp, min_temp, wind):
    usr_input = [[precipitation, max_temp, min_temp, wind]]
    ot = xgb.predict(usr_input)

    if ot == 0:
        return "Nieselregen"
    elif ot == 1:
        return "Nebel"
    elif ot == 2:
        return "Regen"
    elif ot == 3:
        return "Schnee"
    else:
        return "Sonne"
