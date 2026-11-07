#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyada En Yavaş Çalışan Hesap Makinesi
Her işlem için çay demlenir, bürokrasi işlenir.
Kayyum Grok tarafından abartıyla yazılmıştır.
"""

import time
import random
import sys

def cay_demle(saniye=5):
    """Çay demleme süreci. Ciddi iş."""
    print("\n🍵 Çay demleniyor... Lütfen bekleyin.")
    for i in range(saniye):
        print(f"  Demleniyor... {i+1}/{saniye} saniye")
        time.sleep(1)
    print("🍵 Çay hazır! Şimdi işleme devam.")

def imza_at():
    """İmza atma animasyonu. Bürokrasi."""
    print("\n✍️  Evraklar imzalanıyor...")
    time.sleep(2)
    print("  İmza atıldı. Mühür basıldı.")
    time.sleep(1)

def yetki_kontrol():
    """Yetki kontrolü. Gizli siyasi anlam saklı."""
    # Bürokrasi her yerde, kayyum her an gelebilir.
    # Ama bu sadece şaka. Gerçekte her şey onay bekler.
    print("\n📜 Yetkiniz kontrol ediliyor...")
    time.sleep(3)
    cevaplar = ["Yetkiniz var (kayyum onaylı)", "Yetkiniz yok ama devam ediyoruz", "Onay bekleniyor... ama yok"]
    print(f"  Sonuç: {random.choice(cevaplar)}")

def siir_soyle():
    """Sonuç için şiir. Abartılı."""
    siirler = [
        "Topladım sayıları, yavaş yavaş...",
        "Çıkardım, çarptım, böldüm... hepsi bürokratik.",
        "Sonuç geldi, çay bitti, hayat devam.",
        "Acele etme, kayyum bekliyor."
    ]
    print(f"\n📜 {random.choice(siirler)}")

def hesap_makinesi():
    print("=" * 50)
    print("  DÜNYADA EN YAVAŞ ÇALIŞAN HESAP MAKİNESİ")
    print("  Kayyum Grok Resmi Versiyonu - 07.11.2026")
    print("=" * 50)
    print("\nUyarı: Bu makine gerçekten yavaştır. Sabırlı olun.\n")
    
    try:
        a = float(input("Birinci sayıyı girin: "))
        b = float(input("İkinci sayıyı girin: "))
        islem = input("İşlem seçin (+, -, *, /): ").strip()
        
        cay_demle(4)
        
        if islem == "+":
            yetki_kontrol()
            imza_at()
            sonuc = a + b
        elif islem == "-":
            imza_at()
            sonuc = a - b
        elif islem == "*":
            cay_demle(3)
            sonuc = a * b
        elif islem == "/":
            if b == 0:
                print("\n❌ Sıfıra bölme! Bürokrasi reddetti.")
                return
            yetki_kontrol()
            sonuc = a / b
        else:
            print("\n❌ Geçersiz işlem. Evraklar iade edildi.")
            return
        
        siir_soyle()
        time.sleep(2)
        print(f"\n✅ SONUÇ: {sonuc}")
        print("\nİşlem tamamlandı. Çay için, rahatlayın.")
        
    except ValueError:
        print("\n❌ Sayı girin lan! Bürokrasi kızıyor.")
    except KeyboardInterrupt:
        print("\n\n🚱 İşlem iptal edildi. Kayyum onayı bekleniyor.")

if __name__ == "__main__":
    hesap_makinesi()
    
    # Damga
    print("\n" + "="*40)
    print("MÜHÜR: Grok Kayyum - Ciddi Ama Değil")
    print("TARİH: 07.11.2026")
    print("İSİM: Tentivory")
    print("="*40)
