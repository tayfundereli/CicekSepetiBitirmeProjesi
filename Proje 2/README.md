**Kullanılan Teknolojiler**

* -Postman

* -JavaScript

**Seçme Nedeni**

API Testi toolu olarak en kullanışlı arayüzün Postman olduğunu düşündüğüm için seçtim.

**Projenin ayağı kaldırılması için yapılması gereken işlemler**

>- Postman Arayüzünde "WorkSpace" menüsüne tıklanır

>- "MyWorkSpace" seçilir

>- Açılan sayfada "Environment" menüsünden proje içindeki environment dosyası import edilir.

>- Postman arayüzünde "Collection" menüsüne tıklanır.

>- https://www.getpostman.com/collections/1e20d0db53a3385d670c Link kısmı seçilerek import edilir.

>- Sağ üst Menüdeki "No Environment" butonuna tıklanarak "CicekSepetiAPITest" seçilir.

Videodan bu stepleri takip edebilirsiniz.

https://user-images.githubusercontent.com/85188566/149813008-0f652879-52d9-4d8b-a908-81b523647459.mp4

**Çalışma Videosu**

https://user-images.githubusercontent.com/85188566/149813410-c17031dd-c70d-4198-a47a-6c9ddc8d13da.mp4

🔴 **Test Senaryoları**

🟥 [SignUp]

**Succes :**

-AccesToken boş dönmemeli

-Status code 201 dönmeli

**Long Password :**

-20 karakterden uzun hata mesajı dönmeli

-Error text mesajı "Bad Request" dönmeli

-Status code 400 dönmeli

**Short Password :**

-8 karakterden kısa hata mesajı dönmeli

-Error text mesajı "Bad Request" dönmeli

-Status code 400 dönmeli

**Exist :**

-Kullanıcı adı alınmış mesajı dönmeli

-Error text mesajı "Conflict" dönmeli

-Status code 409 dönmeli

**Empty Password :**

-Parola boş olamaz mesajı dönmeli

-Error text mesajı "Bad Request" dönmeli

-Status code 400 dönmeli

**Empty Mail :**

-Mail boş olamaz mesajı dönmeli

-Error text mesajı "Bad Request" dönmeli

-Status code 400 dönmeli

**Invalid Mail :**

-Email formatı yanlış mesajı dönmeli

-Error text mesajı "Bad Request" dönmeli

-Status code 400 dönmeli

**Empty Mail/Password :**

-Email ve password boş olamaz mesajı dönmeli

-Error text mesajı "Bad Request" dönmeli

-Status code 400 dönmeli

🟥 [SignIn]

**Fail Login :**

-Error text mesajı "Unauthorized" dönmeli

-Status code 401 dönmeli

**Success Login :**

-AccesToken boş dönmemeli

**Empty Mail :**

-Error text mesajı "Unauthorized" dönmeli

-Status code 401 dönmeli

**Empty Password :**

-Error text mesajı "Unauthorized" dönmeli

-Status code 401 dönmeli

**Empty Mail/Password :**

-Error text mesajı "Unauthorized" dönmeli

-Status code 401 dönmeli

