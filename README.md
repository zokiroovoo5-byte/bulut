# Bulutli Kalkulyator (Python CI/CD Serverless Demo)

Namangan Davlat Texnika Universiteti (NamDTU) "Axborot tizimlari va texnologiyalari" kafedrasi **"Bulutli texnologiyalar"** fani doirasida talabalarga zamonaviy **PaaS**, **Serverless (FaaS)** va **CI/CD (Continuous Integration / Continuous Deployment)** tamoyillarini amalda ko'rsatish uchun tayyorlangan o'quv loyihasi.

---

## 📁 Loyiha tuzilishi

```text
bulut-kalkulyator/
├── api/
│   └── index.py         # Python 3 (Flask) Serverless API funksiyasi
├── public/
│   └── index.html       # Zamonaviy Tailwind CSS frontend interfeysi
├── requirements.txt     # Python kutubxonalari (Flask, Flask-CORS)
├── vercel.json          # Vercel Serverless routing konfiguratsiyasi
├── .gitignore           # Git uchun istisno qilingan fayllar
└── README.md            # To'liq amaliy qo'llanma
```

---

## 🚀 Talabalarga ko'rsatish bo'yicha qadamma-qadam reja

### 1-Qadam: GitHub Desktop orqali yuklash
1. **GitHub Desktop** dasturini oching.
2. Yuqori menyudan **File** -> **Add Local Repository...** ni bosing.
3. Papka yo'li sifatida ushbu papkani tanlang:
   `C:\Users\ASIOS\Desktop\All\Universitet\Fanlar\Bulutli texnologiyalar\bulut-kalkulyator`
4. Agar *"This directory does not appear to be a Git repository"* desa, **"create a repository"** tugmasini bosing va **Create repository** ni tasdiqlang.
5. Yuqoridagi **"Publish repository"** tugmasini bosing:
   - Name: `bulut-kalkulyator`
   - *Keep this code private* belgisini olib tashlang (Public qiling) yoki xohishingizga ko'ra Private qoldiring.
   - **Publish repository** ni bosing.

---

### 2-Qadam: Vercel da 1 daqiqada Deploy qilish
1. Brauzerda [vercel.com](https://vercel.com) ga kiring va GitHub akkauntingiz orqali tizimga kiring.
2. Asosiy boshqaruv panelida **"Add New..."** -> **"Project"** tugmasini bosing.
3. Yangi chiqqan ro'yxatdan `bulut-kalkulyator` repozitoriysi qarshisidagi **"Import"** tugmasini bosing.
4. **Deploy** tugmasini bosing (sozlamalarga tegmaysiz, Vercel hammasini avtomatik aniqlaydi).
5. 15-25 soniyadan so'ng sizga dunyo bo'ylab ishlaydigan havola beriladi:
   Masalan: `https://bulut-kalkulyator-xxxx.vercel.app`

---

### 3-Qadam: Darsdagi Jonli Demonstratsiya (CI/CD Mo'jizasi)
1. Vercel bergan havolani talabalarga (masalan, Telegram guruhga) bering va ular telefonlaridan kirib ko'rsinlar.
2. Endi darsda proyektor orqali `public/index.html` faylini ochib, biron joyini o'zgartiring (masalan, sarlavha matnini yoki rangini).
3. **GitHub Desktop** ga o'tib, pastda commit xabarini yozing (masalan: *"Yangi dizayn yangilandi"*) va **"Commit to main"**, so'ngra **"Push origin"** tugmasini bosing.
4. **Vercel ga kirmaysiz!** 10-15 soniyadan keyin barcha talabalar o'z telefonlarida sahifani yangilashsa (Refresh), o'zgarishlar avtomatik tarzda butun dunyoga tarqalganini ko'rishadi!
5. **Xulosa qiling:** Bu zamonaviy **Continuous Deployment (CI/CD)** bo'lib, dasturchi server sozlash bilan ovora bo'lmay, faqat kod yozishga e'tiborini qaratishiga imkon beradi.
