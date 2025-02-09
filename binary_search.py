def binary_search(liste, hedef):
    low = 0
    high = len(liste) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Ortadaki elemanı bul
        
        if liste[mid] == hedef:
            return mid  # Hedef bulundu, indeksi döndür
        elif liste[mid] < hedef:
            low = mid + 1  # Hedef sağ yarıda, sol kısmı eleyin
        else:
            high = mid - 1  # Hedef sol yarıda, sağ kısmı eleyin
    
    return -1  # Hedef bulunamazsa -1 döndür

# Örnek kullanım
liste = [1, 3, 5, 7, 9, 11, 13, 15]
hedef = 7
index = binary_search(liste, hedef)
print(f"Hedefin indeksi: {index}")
