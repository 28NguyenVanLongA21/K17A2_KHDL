def tinh_cuoc_taxi(km, so_cho):
    if so_cho == 4:
        gia_mo_cua = 11000
        gia_20km = 12100
        gia_tren_20km = 10000

        if km <= 0.8:
            cuoc_taxi = gia_mo_cua
        elif km <= 20:
            cuoc_taxi = gia_mo_cua + (km - 0.8) * gia_20km
        else:
            cuoc_taxi = gia_mo_cua + 19.2 * gia_20km + (km - 20) * gia_tren_20km

    elif so_cho == 7:
        gia_mo_cua = 13000
        gia_30km = 14100
        gia_tren_30km = 12000

        if km <= 0.8:
            cuoc_taxi = gia_mo_cua
        elif km <= 30:
            cuoc_taxi = gia_mo_cua + (km - 0.8) * gia_30km
        else:
            cuoc_taxi = gia_mo_cua + 29.2 * gia_30km + (km - 30) * gia_tren_30km

    else:
        cuoc_taxi = 0 
    return cuoc_taxi
km = float(input("Nhập số km di chuyển: "))
so_cho = int(input("Nhập số chỗ (4 hoặc 7): "))
cuoc_taxi = tinh_cuoc_taxi(km, so_cho)
if cuoc_taxi:
    print(f"Cước taxi cho {so_cho} chỗ và {km} km là: {cuoc_taxi} đồng")
else:
    print("Số chỗ không hợp lệ. Hỗ trợ xe 4 chỗ và 7 chỗ.")

