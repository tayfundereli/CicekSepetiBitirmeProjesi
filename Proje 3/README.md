# **Performance Test** 

- https://www.cicek.com header da bulunan search modülüne "saat" yazılarak arama yapılır.

### Test Senaryoları 

**[SearchBox]**

-Status Response "200" olmalı

-"Page Type : search" olmalı

-"Search : Saat" olmalı

-"PageUrl : http://www.cicek.com/Arama?query=saat" olmalı 

**[Ürün Liste Sayfası]**

-Status Response "200" olmalı

-"Search : Saat" olmalı

**[Suggest]**

-Status Response "200" olmalı

-"Query : saat" olmalı

**Summary Report** 

>- Loop Count = 1

![image](https://user-images.githubusercontent.com/85188566/149821913-2e35741c-74b4-484d-8293-667850550956.png)

>- Loop Count = 50

![image](https://user-images.githubusercontent.com/85188566/149823188-9683b76d-efd4-475c-bfaa-ed9e2968e86f.png)

>- Loop Count = 200

![image](https://user-images.githubusercontent.com/85188566/149823385-3bb09f08-6b07-4442-b650-a888f36e7a45.png)


Aggregate Report

>- Loop Count = 1

![image](https://user-images.githubusercontent.com/85188566/149822088-ce8049ce-bcc4-4a24-ab3d-ca1731660b77.png)

>- Loop Count = 50

![image](https://user-images.githubusercontent.com/85188566/149823781-5eccae00-e91f-44e4-b2c4-0574ccf81fc9.png)

>- Loop Count = 200

![image](https://user-images.githubusercontent.com/85188566/149823528-db1a09f7-012b-4d9e-87cb-1d86cb674bac.png)


Graph Result

>- Loop Count = 1

![image](https://user-images.githubusercontent.com/85188566/149822254-4a87072d-03a3-4ebd-972e-c5d560597d1a.png)

>- Loop Count = 50

![image](https://user-images.githubusercontent.com/85188566/149822368-96afea46-839d-495e-9dbd-afb006f1a600.png)

>- Loop Count = 200

![image](https://user-images.githubusercontent.com/85188566/149822527-f0ecb3d9-251a-4fc2-b0b5-d17aa9e146d4.png)




