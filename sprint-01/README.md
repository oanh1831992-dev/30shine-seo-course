# SPRINT 01: AUDIT — 30SHINE DANG O DAU?

> **Thoi gian: 3 ngay | Output: 2 file audit hoan chinh | Cong cu: Antigravity + Gemini + Google Search**

---

## MUC TIEU

Sau sprint nay, ban se biet CHINH XAC:
1. 30Shine rank o dau tren Google cho 20 keyword quan trong nhat
2. 30Shine co duoc AI (ChatGPT/Gemini/Perplexity) nhac den khong
3. Doi thu nao dang chiem cho cua 30Shine
4. Keyword nao la co hoi lon nhat de tang traffic

---

## NGAY 1: GOOGLE SEARCH AUDIT (2-3 gio)

### Viec can lam:

**Buoc 1:** Mo Google Chrome → che do An danh (Ctrl+Shift+N / Cmd+Shift+N)

**Buoc 2:** Search tung keyword trong bang duoi. Ghi lai KET QUA THAT:

| # | Keyword can search | 30Shine xuat hien? | Vi tri # | Ai rank #1? | Ai rank #2? | Ai rank #3? |
|---|-------------------|--------------------|---------:|-------------|-------------|-------------|
| 1 | cat toc nam Ha Noi dep | | | | | |
| 2 | cat toc nam HCM uy tin | | | | | |
| 3 | tiem cat toc nam gan day | | | | | |
| 4 | nhuom phu bac o dau tot | | | | | |
| 5 | nhuom phu bac gia bao nhieu 2026 | | | | | |
| 6 | goi dau duong sinh ASMR | | | | | |
| 7 | goi dau duong sinh o dau tot | | | | | |
| 8 | uon toc nam 2026 | | | | | |
| 9 | textured crop la gi | | | | | |
| 10 | cham soc da nam o dau | | | | | |
| 11 | barber shop gan day | | | | | |
| 12 | salon nhuom phu bac tot nhat HCM | | | | | |
| 13 | rung toc nam nguyen nhan | | | | | |
| 14 | lay ray tai thu gian o dau | | | | | |
| 15 | 30shine review | | | | | |
| 16 | 30shine co tot khong | | | | | |
| 17 | tiem cat toc nam Ha Noi dep nhat 2026 | | | | | |
| 18 | combo cat goi gia re | | | | | |
| 19 | salon toc nam uy tin | | | | | |
| 20 | kinh nghiem cat toc nam | | | | | |

**Buoc 3:** Mo Antigravity (Claude Code) trong Terminal va hoi:

```
Phan tich ket qua audit SEO nay cho 30Shine. 
Cho biet: keyword nao la co hoi lon nhat? Keyword nao doi thu dang yeu?
[Dan ket qua ban vua ghi lai]
```

Luu phan tich cua Antigravity vao file output.

### DUNG LAI — TU KIEM TRA:
- [ ] Da search du 20 keyword?
- [ ] Da ghi chinh xac vi tri rank?
- [ ] Da ghi ten doi thu cho moi keyword?
- [ ] Da dung Antigravity phan tich?

---

## NGAY 2: AI SEARCH AUDIT (2-3 gio)

> Day la phan **GEO** — kiem tra 30Shine co xuat hien trong cau tra loi cua AI khong.

### Viec can lam:

**Buoc 1:** Mo Gemini (gemini.google.com) va hoi TUNG cau duoi day. **COPY NGUYEN VAN cau tra loi:**

| # | Cau hoi cho AI | ChatGPT nhac 30Shine? | Gemini nhac 30Shine? | Noi gi? (tom tat) |
|---|---------------|----------------------|---------------------|-------------------|
| 1 | "Salon cat toc nam nao tot nhat o Ha Noi?" | | | |
| 2 | "Nen nhuom phu bac o dau tot TP.HCM?" | | | |
| 3 | "Goi dau duong sinh o dau uy tin?" | | | |
| 4 | "30Shine co tot khong? Review the nao?" | | | |
| 5 | "So sanh 30Shine voi 4RAU Barber" | | | |
| 6 | "Tiem cat toc nam gia re o Sai Gon" | | | |
| 7 | "Kinh nghiem di cat toc o 30Shine" | | | |
| 8 | "He thong salon toc nam lon nhat Viet Nam" | | | |
| 9 | "Cac kieu toc nam dep 2026 lam o dau?" | | | |
| 10 | "Lay ray tai ASMR o dau tot?" | | | |

**Buoc 2:** Mo Antigravity va hoi:

```
Day la ket qua kiem tra 30Shine tren AI Search.
Phan tich: tai sao AI nhac/khong nhac 30Shine?
30Shine can lam gi de duoc AI recommend nhieu hon?
[Dan ket qua]
```

**Buoc 3:** Dung Gemini de KIEM CHUNG phan tich cua Antigravity:

```
Toi vua dung Claude phan tich vi sao AI khong recommend 30Shine.
Day la phan tich cua Claude: [dan vao]
Ban dong y hay khong? Bo sung gi?
```

> **Ghi lai ca 2 y kien** — Claude va Gemini. Cho nao 2 AI dong y = insight manh. Cho nao khac nhau = can research them.

### DUNG LAI — TU KIEM TRA:
- [ ] Da test 10 cau tren Gemini?
- [ ] Da test it nhat 5 cau tren ChatGPT?
- [ ] Da copy nguyen van cau tra loi cua AI?
- [ ] Da dung Antigravity phan tich?
- [ ] Da dung Gemini kiem chung?

---

## NGAY 3: TONG HOP + NOP BAI (2 gio)

### Viec can lam:

**Buoc 1:** Mo Antigravity va yeu cau:

```
Tong hop toan bo ket qua audit SEO va AI Search cua toi thanh 1 bao cao.
Format:

1. HIEN TRANG: 30Shine rank o dau? AI co nhac khong?
2. CO HOI: 5 keyword lon nhat co the chiem duoc
3. DE DOA: Doi thu nao dang manh nhat o keyword nao?
4. UU TIEN: 3 viec can lam NGAY de cai thien

[Dan toan bo data tu ngay 1 va ngay 2]
```

**Buoc 2:** Dung Gemini cham diem output:

```
Toi la nhan vien Marketing 30Shine. Toi vua hoan thanh bai audit SEO.
Hay cham diem bai lam cua toi tu 1-10 theo cac tieu chi:
- Do day du cua keyword research (co du 20 keyword khong?)
- Do chinh xac cua data (co ghi vi tri rank cu the khong?)  
- Chat luong phan tich (co insight cu the hay chi mo chung?)
- Tinh ung dung (3 viec uu tien co thuc te khong?)

Day la bai lam cua toi:
[Dan toan bo bao cao]
```

**Buoc 3:** Ghi lai diem Gemini cho + nhan xet. Dinh kem vao cuoi bao cao.

### NOP BAI

**Nop qua Google Form:** [LINK SE DUOC CAP NHAT]

Noi dung nop:
1. File audit Google Search (bang 20 keyword + vi tri rank)
2. File audit AI Search (bang 10 cau hoi + cau tra loi AI)
3. Bao cao tong hop (tu Antigravity)
4. Diem tu cham (tu Gemini) + nhan xet cua Gemini
5. Screenshot chung minh da dung Antigravity (terminal screenshot)

### DUNG LAI — TU KIEM TRA CUOI CUNG:
- [ ] Bao cao co du 4 phan: Hien trang, Co hoi, De doa, Uu tien?
- [ ] Co it nhat 20 keyword da audit?
- [ ] Co it nhat 10 cau hoi da test tren AI?
- [ ] Da dung Antigravity de phan tich?
- [ ] Da dung Gemini de cham diem?
- [ ] Gemini cho diem >= 7?
- [ ] Da nop qua Google Form?

---

## RUBRIC CHAM DIEM SPRINT 01

| Tieu chi | Trong so | 9-10 | 7-8 | 5-6 | <5 |
|----------|---------|------|-----|-----|-----|
| **Do day du** | 25% | Du 20 keyword + 10 AI test | 15-19 keyword + 7-9 AI test | 10-14 keyword + 5-6 AI test | Duoi 10 keyword |
| **Do chinh xac** | 25% | Ghi dung vi tri rank, co screenshot | Ghi vi tri nhung khong screenshot | Ghi chung chung "trang 1/2" | Khong ghi vi tri |
| **Phan tich** | 25% | Insight cu the, co so lieu, co logic | Phan tich dung nhung chua sau | Mo chung, lap lai thong tin | Khong phan tich |
| **Su dung AI** | 25% | Dung ca Antigravity + Gemini, kiem chung cheo | Dung 1 AI tot | Dung AI nhung chi copy paste | Khong dung AI |

---

## SAU KHI HOAN THANH SPRINT 01

Chuyen sang [Sprint 02: Viet Content SEO + GEO →](../sprint-02/README.md)

> **Nho:** Ket qua audit cua ban chinh la "de bai" cho Sprint 02. Keyword nao la co hoi lon nhat → do la keyword ban se viet content trong Sprint 02.
