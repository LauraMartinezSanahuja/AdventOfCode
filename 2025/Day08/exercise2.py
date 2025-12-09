from math import sqrt

data_file = "example.txt"
data_file = "data.txt"

result: int = 0
junction_boxes: set[tuple[int, int, int]] = set()
junction_boxes_copy: set[tuple[int, int, int]] = set()
junc_euclid_distances: dict[tuple[tuple[int, int, int], tuple[int, int, int]], float] = {}
junc_in_circuits: dict[tuple[int, int, int], int] = {}
circuits: dict[int, list[tuple[int, int, int]]] = {}
base_circuit_id: int = 0


def euclidean_distance(box1: tuple[int, int, int], box2: tuple[int, int, int]) -> float:
    return sqrt((box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2 + (box1[2] - box2[2]) ** 2)


with open(data_file, "r") as file:
    for line in file:
        junction_boxes.add(tuple(int(x) for x in line.strip().split(',')))
    junction_boxes = sorted(junction_boxes)
    junction_boxes_copy = junction_boxes.copy()

for box1 in junction_boxes:
    circuits[base_circuit_id] = [box1]
    junc_in_circuits[box1] = base_circuit_id
    base_circuit_id += 1
    for box2 in junction_boxes:
        if (
            box1 != box2
            and (box1, box2) not in junc_euclid_distances
            and (box2, box1) not in junc_euclid_distances
        ):
            dist = euclidean_distance(box1, box2)
            junc_euclid_distances[(box1, box2)] = dist

junc_euclid_distance_values = list(junc_euclid_distances.values())
junc_euclid_distance_values.sort()

found_last = False
for min_dist in junc_euclid_distance_values:
    if found_last:
        break
    for (box1, box2), dist in junc_euclid_distances.items():
        if dist == min_dist:
            in_circuit1 = box1 in junc_in_circuits
            in_circuit2 = box2 in junc_in_circuits

            circuit_id1 = junc_in_circuits[box1]
            circuit_id2 = junc_in_circuits[box2]
            if circuit_id1 == circuit_id2:
                continue

            print(len(set(junc_in_circuits.values())))
            if len(set(junc_in_circuits.values())) == 2:
                print('Found the last connection!')
                print(f'Box1: {box1}, Box2: {box2}')
                result = box1[0] * box2[0]
                found_last = True
                break

            for box in circuits[circuit_id2]:
                circuits[circuit_id1].append(box)
                junc_in_circuits[box] = circuit_id1
            del circuits[circuit_id2]

print(f'Result: {result}')
