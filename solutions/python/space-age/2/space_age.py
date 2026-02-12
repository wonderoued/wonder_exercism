class SpaceAge:
    # On définit les constantes orbitales
    PLANETS = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132
    }
    SECONDS_IN_EARTH_YEAR = 31557600 #

    def __init__(self, seconds):
        self.seconds = seconds #
        # On crée les méthodes dynamiquement
        for name, period in self.PLANETS.items():
            setattr(self, f"on_{name}", self._make_planet_method(period))

    def _make_planet_method(self, period):
        # Cette fonction crée et renvoie une méthode de calcul
        def calculate():
            age = self.seconds / (self.SECONDS_IN_EARTH_YEAR * period)
            return round(age, 2) # Arrondi à deux décimales
        return calculate