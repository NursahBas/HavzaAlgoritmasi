# HavzaAlgoritmasi
OpenCv ve Python ile yazmış olduğum Havza Algoritması.


. Havza Algoritması 
        Havza, segmentasyon için, yani bir görüntüdeki farklı nesneleri ayırmak için kullanılan klasik bir algoritmadır. 
Herhangi bir gri tonlamalı görüntü topografik yüzey alanı olarak düşünüldüğünde, RGB renk kodlama yöntemine göre yüksek yoğunluğun oluşturduğu noktalar zirveleri, 
düşük yoğunluğun oluşturduğu noktalar ise vadileri ifade etmektedir. Örneğin; izole edilmiş her vadi yükseltilerini renklendirme işlemlerinde yerel minimum olarak 
adlandırılan zirvelere yakın noktalara bağlı olarak, farklı renklerde birleşmesine yani etiketlenmesine neden olacaktır. Buna göre topografik yüzeyde yükseltilerin
birleşme noktalarında gradyan olarak adlandırılan farklı renklerinde ortaya çıkması ve birleşmesi gerçekleştirilecektir. Farklı renklerin birleşme noktalarında engeller
inşa edilmektedir. Bu birleşme noktaları havza algoritmasının amacı olan segmentasyon işlemlerinin gerçekleştiği nokralar olarak belirlenmektedir.


