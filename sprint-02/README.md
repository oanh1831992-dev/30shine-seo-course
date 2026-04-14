# SPRINT 02: VIET CONTENT SEO + GEO THAT

> **Thoi gian: 3 ngay | Output: 2 bai content hoan chinh san sang publish | Cong cu: Antigravity + Gemini**

---

## MUC TIEU

Sau sprint nay, ban se co:
1. **1 bai blog SEO** nham keyword co hoi lon nhat (tu Sprint 01)
2. **1 trang FAQ** voi structured data giup AI trich dan
3. Ca 2 bai duoc Gemini cham >= 8 diem moi nop

---

## NGAY 1: RESEARCH + OUTLINE (2-3 gio)

### Buoc 1: Chon keyword tu Sprint 01

Lay 1 keyword co hoi lon nhat tu bao cao Sprint 01 cua ban. Uu tien keyword ma:
- 30Shine chua rank (gap lon)
- Doi thu rank nhung content yeu
- Co search volume (Google Trends tang)

**Vi du keyword uu tien cao (tu data nghien cuu):**
- "nhuom phu bac o dau tot" — 30Shine vang mat tren Toplist.vn
- "goi dau duong sinh" — signal manh 7/7 ngay, LRT ROAS 8.1x
- "tiem cat toc nam [thanh pho]" — KingKong dang chiem
- "uon toc nam 2026" — +96% Google Trends
- "rung toc nam nguyen nhan" — signal manh nhat 6/6 ngay

### Buoc 2: Research bang Antigravity + Gemini

**Mo Antigravity, chay:**

```
Toi dang viet bai SEO cho 30Shine nham keyword "[KEYWORD CUA BAN]".

Hay giup toi:
1. Phan tich top 3 ket qua hien tai tren Google cho keyword nay
   - Ho viet ve gi? Bao nhieu tu? Co FAQ khong? Co hinh anh khong?
2. Nguoi dung search keyword nay thuc su muon biet gi? (Search Intent)
3. 30Shine co loi the gi de viet bai tot hon ho?
4. De xuat outline bai viet (cac H2, H3) voi uoc luong so tu moi phan
```

**Mo Gemini, kiem chung:**

```
Toi muon viet bai SEO cho 30Shine nham keyword "[KEYWORD]".
Antigravity de xuat outline nhu sau: [dan outline]

Ban thay outline nay da du chua? Thieu gi?
Nguoi doc Viet Nam nam 26-37 tuoi se quan tam dieu gi nhat?
```

**Ghi lai:** Combine y tuong tu ca 2 AI → tao outline cuoi cung.

### Buoc 3: Tao outline cuoi cung

```markdown
# [H1] [Tieu de bai viet — co keyword chinh, duoi 60 ky tu]

Meta description: [155 ky tu, co keyword + CTA]

## [H2] [Cau hoi/van de chinh nguoi doc muon biet]
- Noi dung chinh: ...
- So lieu can dung: ...
- Link noi bo: ...

## [H2] [Cau hoi tiep theo]
...

## [H2] Tai 30Shine — [Keyword] Duoc Thuc Hien Nhu The Nao?
- Quy trinh cu the
- Gia ca
- Dia chi

## [H2] Cau Hoi Thuong Gap (FAQ)
- Q1: ...
- Q2: ...
- Q3: ...
- Q4: ...
- Q5: ...

## [CTA] Dat Lich Ngay
```

### DUNG LAI — TU KIEM TRA:
- [ ] Da chon keyword co data tu Sprint 01?
- [ ] Da dung Antigravity research?
- [ ] Da dung Gemini kiem chung?
- [ ] Outline co it nhat 4 H2?
- [ ] Outline co phan FAQ >= 5 cau hoi?

---

## NGAY 2: VIET BAI (3-4 gio)

### Cach viet nhanh voi Antigravity + Gemini

**KHONG copy paste tu AI.** Thay vao do:

**Buoc 1:** Viet DRAFT bang Antigravity:

```
Viet bai blog SEO cho 30Shine theo outline nay: [dan outline]

Yeu cau:
- Giong van tu nhien, nhu nguoi Viet viet cho nguoi Viet
- Co so lieu cu the (150 salon, 136,788 khach/Tet, gia cu the)
- Co internal link den 30shine.com/booking, 30shine.com/dich-vu-...
- FAQ phai tra loi TRUC TIEP, ngan gon, co so lieu
- Tong cong 1500-2000 tu
- KHONG dung tu ngu qua hoa my, KHONG viet kieu ChatGPT generic
```

**Buoc 2:** Doc lai TOAN BO bai viet. Sua nhung cho:
- Khong dung su that (gia sai? so salon sai?)
- Qua generic (nghe giong bat ky salon nao, khong phai 30Shine)
- Thieu dac trung 30Shine (app dat lich, 3 lan keo, cam ket hoan tien...)

**Buoc 3:** Dung Gemini cham bai viet:

```
Toi vua viet bai SEO cho 30Shine nham keyword "[KEYWORD]".
Hay cham diem bai viet tu 1-10 theo:

1. SEO On-page (co keyword trong title, H1, H2, meta? co internal link?)
2. Chat luong noi dung (co so lieu that? co chuyen biet cho 30Shine?)
3. GEO readiness (AI co the trich dan duoc khong? FAQ co ro rang?)
4. Doc duoc (giong van tu nhien? nam 26-37 VN co thich doc khong?)
5. Do chinh xac (thong tin co dung voi thuc te 30Shine?)

Bai viet:
[Dan toan bo bai]
```

**YEU CAU:** Gemini phai cho **>= 8 diem** moi chuyen sang buoc tiep. Neu duoi 8, sua theo gop y cua Gemini roi nop lai.

### DUNG LAI — TU KIEM TRA:
- [ ] Bai viet >= 1500 tu?
- [ ] Co keyword trong Title, H1, it nhat 2 H2?
- [ ] Co >= 3 internal link den 30shine.com?
- [ ] Co FAQ >= 5 cau hoi?
- [ ] Co so lieu cu the (gia, so salon, thoi gian)?
- [ ] Gemini cham >= 8 diem?

---

## NGAY 3: FAQ SCHEMA + NOP BAI (2 gio)

### Buoc 1: Tao FAQ Schema

FAQ Schema la "ma" giup Google hien thi FAQ truc tiep tren ket qua search, va giup AI extract cau tra loi.

**Dung Antigravity:**

```
Tao FAQ Schema (JSON-LD) tu phan FAQ trong bai viet cua toi.
Format chuan schema.org FAQPage.

FAQ cua toi:
[Dan phan FAQ tu bai viet]
```

Output se nhu:
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Nhuom phu bac tai 30Shine gia bao nhieu?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dich vu nhuom phu bac tai 30Shine co gia tu XXXk VND..."
      }
    }
  ]
}
```

**Dung Gemini kiem tra:**

```
Kiem tra FAQ Schema nay co dung chuan schema.org khong?
Co loi gi khong? Thieu truong nao?
[Dan JSON schema]
```

### Buoc 2: Kiem tra bai viet lan cuoi

**Checklist SEO (bat buoc tat ca):**
- [ ] Title tag <= 60 ky tu, co keyword chinh
- [ ] Meta description <= 155 ky tu, co CTA
- [ ] Chi 1 H1, co keyword chinh
- [ ] It nhat 3 H2 headers
- [ ] Noi dung >= 1500 tu
- [ ] >= 3 internal links den 30shine.com
- [ ] Co anh voi alt text co keyword
- [ ] URL slug co keyword (VD: /nhuom-phu-bac-30shine)

**Checklist GEO (bat buoc tat ca):**
- [ ] FAQ section >= 5 cau hoi
- [ ] Co FAQ Schema (JSON-LD)
- [ ] Co so lieu cu the (gia, so salon, thoi gian)
- [ ] Entity name nhat quan ("30Shine")
- [ ] Co bang so sanh / danh sach giup AI extract
- [ ] Noi dung tra loi TRUC TIEP cau hoi pho bien
- [ ] Thong tin cap nhat (co ngay thang, "2026")

### NOP BAI

**Nop qua Google Form:** [LINK SE DUOC CAP NHAT]

Noi dung nop:
1. **Bai blog SEO hoan chinh** (file .md hoac .doc)
2. **FAQ Schema** (file .json)
3. **Diem Gemini** + nhan xet cua Gemini (screenshot hoac copy)
4. **Screenshot Antigravity** chung minh da su dung
5. **Keyword da chon** + ly do chon (tu Sprint 01)

### RUBRIC CHAM DIEM SPRINT 02

| Tieu chi | Trong so | 9-10 | 7-8 | 5-6 | <5 |
|----------|---------|------|-----|-----|-----|
| **SEO On-page** | 25% | Du tat ca checklist SEO | Thieu 1-2 muc | Thieu 3-4 muc | Thieu nhieu |
| **Chat luong noi dung** | 30% | So lieu that, gion dac trung 30Shine, doc hay | Dung nhung chua noi bat | Generic, khong dac trung | Copy paste AI |
| **GEO readiness** | 25% | FAQ Schema dung, du FAQ, AI co the trich dan | Co FAQ nhung thieu schema | FAQ qua it hoac khong ro | Khong co FAQ |
| **Su dung AI** | 20% | Dung Antigravity + Gemini, kiem chung cheo, sua theo gop y | Dung tot 1 AI | Chi copy paste | Khong dung |

---

## SAU KHI HOAN THANH SPRINT 02

Ban da co:
- 1 bai blog SEO that, san sang publish tren 30shine.com
- 1 FAQ Schema co the embed vao website

**De xuat cho PO:** Review bai viet, neu dat chat luong → publish that tren website 30Shine. Day la cach **hoc di doi voi hanh** — output cua hoc vien tro thanh content that.

Chuyen sang [Sprint 03: Local SEO + Counter Content →](../sprint-03/README.md)
