import numpy as np
import matplotlib.pyplot as plt

# Beispielstädte (ungefähre Koordinaten, [lat, lon])
cities = {
    "Luxembourg": (49.6117, 6.1319),
    "Dortmund": (51.5136, 7.4653),
    "Bielefeld": (52.0302, 8.5325),
    "Münster": (51.9624, 7.6257),
    "Bochum": (51.4818, 7.2162),
    "Essen": (51.4556, 7.0116),
    "Düsseldorf": (51.2277, 6.7735),
    "Köln": (50.9375, 6.9603),
    "Siegen": (50.8748, 8.0243),
    "Wuppertal": (51.2562, 7.1508),
    "Hagen": (51.3671, 7.4633),
    "Berlin": (52.5200, 13.4050),
    "Hamburg": (53.5511, 9.9937),
    "Frankfurt": (50.1109, 8.6821),
    "München": (48.1351, 11.5820)
}

# Entfernung (euklidisch)
def distance(a, b):
    return np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# Balloon Loop Heuristic
def balloon_loop_heuristic(cities, start="Luxembourg"):
    names = list(cities.keys())
    coords = np.array(list(cities.values()))
    start_idx = names.index(start)

    # Entfernteste Stadt vom Start finden
    dists = [distance(coords[start_idx], c) for c in coords]
    farthest_idx = int(np.argmax(dists))

    # Split in "Hinweg" und "Rückweg" Cluster
    outward = [i for i in range(len(names)) if i != start_idx and coords[i][1] <= coords[farthest_idx][1]]
    inward = [i for i in range(len(names)) if i != start_idx and coords[i][1] > coords[farthest_idx][1]]

    # Sortiere entlang grob nach Longitude
    outward_sorted = sorted(outward, key=lambda i: coords[i][1])
    inward_sorted = sorted(inward, key=lambda i: -coords[i][1])

    route = [start_idx] + outward_sorted + [farthest_idx] + inward_sorted + [start_idx]
    return [names[i] for i in route]

# Route berechnen
route = balloon_loop_heuristic(cities)
print("Balloon Loop Route:", " -> ".join(route))

# Plotten
coords = np.array(list(cities.values()))
plt.figure(figsize=(8,6))
for name, (x,y) in cities.items():
    plt.scatter(y, x, c="blue")
    plt.text(y+0.1, x+0.1, name, fontsize=8)

# Route zeichnen
indices = [list(cities.keys()).index(city) for city in route]
for i in range(len(indices)-1):
    a, b = coords[indices[i]], coords[indices[i+1]]
    plt.plot([a[1], b[1]], [a[0], b[0]], "r-")

plt.title("Balloon Loop Heuristic Route")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.savefig("../results/example_route.png")
plt.show()
