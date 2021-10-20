#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    nb_sec = temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3]
    return nb_sec

temps = (3,23,1,34)
ma_valeur = tempsEnSeconde(temps)  
print(ma_valeur)


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jours = seconde // 86400
    heures = (seconde - jours * 86400) // 3600
    minutes = (seconde - (jours * 86400) - (heures * 3600)) // 60
    secondes = (seconde - (jours * 86400) - (heures * 3600) - (minutes * 60))
    return (jours, heures, minutes, secondes)
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")