Feature: ÇiçekSepeti Test Otomasyon Bootcamp Senaryo 1

  Scenario: Basarili Login İslemi
    Given Login sayfasina gidilir
    When  Email ve password alani doldurulur
    And   Sign in butonuna tiklanir
    And   Pop-up kapatilir
    Then  Giris yapildigi kontrol edilir

  Scenario: Flowers 60 urun kontrolu
    Given Flowers kategorisine gidilir
    When  Ilk sayfada 60 urun oldugu kontrol edilir
    Then  Sayfa 10 kez scroll edilerek her sayfada 60 urun oldugu kontrol edilir

  Scenario: Menu altindaki linklerin kirik olmadiginin kontrolu
    Given Anasayfaya gidilir
    When  Menu altindaki tum linkler gezilir
    Then  Kirik link olup olmadigi kontrol edilir