def baca_suhu():
    suhu = 15.0

    while suhu <= 38.0:
        yield suhu
        suhu += 1.0

data_sensor = baca_suhu()

print("=" * 55)
print("sistem pemantauan suhu sensor")
print("=" * 55)
print(f"{'No':<6}{'suhu':<15}{'status':<15}")
print("=" * 55)

for nomor in range(1, 11):
    suhu = next(data_sensor)
    if suhu < 20.0:
        status = "Dingin"
    elif suhu < 30.0:
        status = "Normal"
    else:
        status = "Panas"
    print(f"{nomor:<6}{suhu:<15.1f}{status:<15}")
print("=" * 55)
print("Pemantauan selesai.")