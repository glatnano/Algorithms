def quick_sort(liste):
    # Eğer liste boş ya da tek elemanlıysa sıralama yapmaya gerek yok
    if len(liste) <= 1:
        return liste
    
    # Listeyi sıralamak için ortadaki elemanı pivot seçiyoruz
    pivot = liste[len(liste) // 2]
    
    # Pivot'tan küçük olanları, eşit olanları ve büyük olanları ayırıyoruz
    left = []
    middle = []
    right = []
    
    for x in liste:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    
    # Sol ve sağ kısımları yeniden sıralayarak birleştiriyoruz
    return quick_sort(left) + middle + quick_sort(right)

# Örnek kullanım
dizi = [12, 1, 51, 4, 100, 124, 45]
siralı_dizi = quick_sort(dizi)
print(siralı_dizi)  # Çıktı: [1, 4, 12, 45, 51, 100, 124]
