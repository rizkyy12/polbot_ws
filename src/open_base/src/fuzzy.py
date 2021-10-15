print ('implementasi logic fuzzy')

x_distance = input('masukkan nilai distance = ')
distance = float(x_distance)

#proses fuzzifikasi
if distance <= 0.2 :
    value_small = 1
    value_safe = 0
    value_big = 0

if distance > 0.2 and distance < 0.4:
    value_small = (0.4-distance)/(0.4-0.2)
    value_safe = 0
    value_big = 0

if distance > 0.2 and distance < 0.5:
    value_safe = (distance - 0.2)/(0.5-0.2)
    value_big = 0
    value_small = 0

if distance == 0.5 :
    value_small = 0
    value_safe = 1
    value_big = 0

if distance > 0.5 and distance < 0.8:
    value_small = 0
    value_safe = (0.8 - distance)/(0.8-0.5)
    value_big = 0

if distance > 0.6 and distance < 0.8:
    value_small = 0
    value_big = (distance-0.6)/(0.8-0.6)
    value_safe = 0

if distance >= 0.8 :
    value_small = 0
    value_safe = 0
    value_big = 1

print('derajat keanggoataan = ')
print('small ', value_small)
print('safe ', value_safe)
print('big ', value_big)

# Proses inferensi
# speed = []
# def fungsiinfslow (variabel_distance):
#     if variabel_distance != 0:
#         hasil_output = min(variabel_distance,0)
#         speed.append([hasil_output,1])

# def fungsiinfaverage (variabel_distance):
#     if variabel_distance != 0:
#         hasil_output = min(variabel_distance,0)
#         speed.append([hasil_output,2])

# def fungsiinffast (variabel_distance):
#     if variabel_distance != 0:
#         hasil_output = min(variabel_distance,0)
#         speed.append([hasil_output,3])


#speed buat ke vx vy
speed = 0
def fungsiinfslow (variabel_distance): 
    global speed
    if variabel_distance != 0:
        speed = 5

def fungsiinfaverage (variabel_distance):
    global speed
    if variabel_distance != 0:
        speed = 3

def fungsiinffast (variabel_distance):
    global speed
    if variabel_distance != 0:
        speed = 1

fungsiinfslow(value_small)
fungsiinfaverage(value_safe)
fungsiinffast(value_big)

print('Speed ', speed)

