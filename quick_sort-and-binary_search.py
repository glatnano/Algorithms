# Quick Sort (Hızlı Sıralama) Algoritması
def quick_sort(liste):
    if len(liste) <= 1:
        return liste
    pivot = liste[len(liste) // 2]
    left = [x for x in liste if x < pivot]
    middle = [x for x in liste if x == pivot]
    right = [x for x in liste if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Binary Search (İkili Arama) Algoritması
def binary_search(liste, hedef):
    low = 0
    high = len(liste) - 1
    while low <= high:
        mid = (low + high) // 2
        if liste[mid] == hedef:
            return mid
        elif liste[mid] < hedef:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Hedef bulunamazsa -1 döndür

# Örnek kullanım
dizi = [12, 1, 51, 4, 100, 124, 45]
hedef = 100

# Adım 1: Diziyi sıralıyoruz (Quick Sort)
sıralı_dizi = quick_sort(dizi)
print("Sıralı Dizi:", sıralı_dizi)

# Adım 2: Binary Search kullanarak hedefi arıyoruz
index = binary_search(sıralı_dizi, hedef)

if index != -1:
    print(f"Hedef {hedef}, dizide {index}. indekste bulundu.")
else:
    print(f"Hedef {hedef} dizide bulunamadı.")
