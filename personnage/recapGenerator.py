from .stats import Stats

class PersonnageRecapGenerator:
    @staticmethod
    def generer_recapitulatif(nom: str, classe_nom: str, stats: Stats) -> str:
        """Génère le récapitulatif formaté"""
        return "\n".join([
            "\n=== RÉCAPITULATIF DU PERSONNAGE ===",
            f"Nom : {nom}",
            f"Classe : {classe_nom}",
            f"PV : {stats.pv}",
            f"PM : {stats.pm}",
            f"Force : {stats.force}",
            f"Intelligence : {stats.intelligence}",
            f"Défense : {stats.defense}",
            f"Résistance magique : {stats.resistance_magique}",
            f"Agilité : {stats.agilite}",
            f"Chance : {stats.chance}",
            f"Endurance : {stats.endurance}",
            f"Esprit : {stats.esprit}\n"
        ])
