from dataclasses import dataclass

@dataclass(frozen=True)
class SolarSystem:
    planets: int = 20
    stars: int = 1

    def setPlanets(self, planets):
        self.planets = planets #errpr - not allowed

system1 = SolarSystem()
print(system1)

#system1.setPlanets(20)

#system1.planets = 10

print(system1)