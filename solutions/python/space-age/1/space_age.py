class SpaceAge:
    SECONDS_IN_EARTH_YEAR = 31557600
    def __init__(self, seconds):
        self.seconds = seconds

    def _calculate_age(self, orbital_period):
        """Méthode interne pour éviter la duplication de code (DRY)."""
        age = self.seconds / (self.SECONDS_IN_EARTH_YEAR * orbital_period)
        return round(age, 2)
    def on_mercury(self):
        return self._calculate_age(0.2408467)

    def on_venus(self):
        return self._calculate_age(0.61519726)

    def on_earth(self):
        return self._calculate_age(1.0)

    def on_mars(self):
        return self._calculate_age(1.8808158)

    def on_jupiter(self):
        return self._calculate_age(11.862615)

    def on_saturn(self):
        return self._calculate_age(29.447498)

    def on_uranus(self):
        return self._calculate_age(84.016846)

    def on_neptune(self):
        return self._calculate_age(164.79132)


