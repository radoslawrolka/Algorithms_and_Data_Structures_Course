# Radosław Rolka
from egz1btesty import runtests

"""
Zapisujemy ceny dostania sie do poszcególnych pol w tablicy result[paliwo_w_baku][planeta].
Bierzemy minimum z poprzedniej planety co dojedziemy, albo 1 tonę paliwa mniej i dotankujemy na obecnej.
Uprzednio jeszcze aktualizujemy wartosć teleportu do dalszej planety.
Złożoność: O( nE )
"""

def planets(map, fuel_cost, teleport, max_fuel):
    n = len(map)

    result = [[float('inf')]*n for _ in range(max_fuel+1)]
    for i in range(max_fuel+1):
        result[i][0] = fuel_cost[0] * i
    if teleport[0][0] != 0:
        result[0][teleport[0][0]] = teleport[0][1]

    for planet in range(1, n):
        dist = map[planet] - map[planet - 1]
        result[0][planet] = min(result[0][planet], result[dist][planet-1])
        to_teleport, teleport_cost = teleport[planet]
        if to_teleport != planet:
            result[0][to_teleport] = min(result[0][to_teleport], result[0][planet] + teleport_cost)
        for fuel in range(1, max_fuel-dist+1):
            result[fuel][planet] = min( result[fuel+dist][planet-1], result[fuel-1][planet] + fuel_cost[planet])
        for fuel in range(max_fuel-dist+1, max_fuel+1):
            result[fuel][planet] = result[fuel - 1][planet] + fuel_cost[planet]

    return result[0][n-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=True)
