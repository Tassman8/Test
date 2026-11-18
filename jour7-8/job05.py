def distance_gardien(nb_marches, hauteur_cm):
    hauteur_escalier_cm = nb_marches * hauteur_cm
    par_trajet_cm = 2 * hauteur_escalier_cm
    par_semaine_cm = par_trajet_cm * 5 * 7
    par_semaine_m = par_semaine_cm / 100

    print(f"Pour {nb_marches} marches de {hauteur_cm} cm, le gardien parcourt {par_semaine_m:.2f} m par semaine.")


distance_gardien(100, 20)
