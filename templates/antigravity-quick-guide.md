# HUONG DAN NHANH ANTIGRAVITY (CLAUDE CODE)

> Tai lieu nay giup ban su dung Antigravity hieu qua trong 10 phut.

---

## ANTIGRAVITY LA GI?

Antigravity = Claude chay trong Terminal. No giup ban:
- **Research** keyword, doi thu, xu huong — nhanh gap 10 lan search Google
- **Viet content** SEO voi so lieu that, structure chuan
- **Phan tich** data GA4, ranking, performance
- **Tao** FAQ schema, structured data, meta tags

---

## CAI DAT (1 lan duy nhat)

### Buoc 1: Cai Node.js (neu chua co)
- Tai tai: https://nodejs.org
- Chon phien ban **LTS**
- Cai dat theo huong dan

### Buoc 2: Cai Antigravity
Mo Terminal (Mac) hoac Command Prompt (Windows):
```bash
npm install -g @anthropic-ai/claude-code
```

### Buoc 3: Chay lan dau
```bash
claude
```
Lam theo huong dan dang nhap tren man hinh.

---

## 10 PROMPT HAY NHAT CHO SEO

### 1. Phan tich keyword
```
Phan tich keyword "[TU KHOA]" cho website 30Shine:
- Search intent la gi? (informational/commercial/transactional/local)
- Ai dang rank top 3?
- Content cua ho co gi manh/yeu?
- 30Shine can viet gi de rank cao hon?
```

### 2. Viet outline bai blog SEO
```
Tao outline bai blog SEO cho 30Shine nham keyword "[TU KHOA]".
Yeu cau: H1 + 4-6 H2 + FAQ 5 cau hoi.
Target: nam 26-37, Viet Nam, tim dich vu grooming.
```

### 3. Viet bai blog hoan chinh
```
Viet bai blog SEO 1500-2000 tu cho 30Shine nham keyword "[TU KHOA]".
Yeu cau:
- Giong van tu nhien, nguoi Viet viet cho nguoi Viet
- Co so lieu: 150 salon, 136k khach/Tet, gia cu the
- Co internal link den 30shine.com
- Co FAQ 5 cau hoi
- KHONG dung tu hoa my kieu ChatGPT
```

### 4. Tao FAQ Schema
```
Tao FAQ Schema (JSON-LD) chuan schema.org tu cac cau hoi nay:
1. [Cau hoi 1]
2. [Cau hoi 2]
...
```

### 5. Phan tich doi thu
```
Phan tich website/content cua [DOI THU] cho keyword "[TU KHOA]":
- Ho co bao nhieu bai ve chu de nay?
- Content cua ho manh o dau?
- 30Shine co the lam gi tot hon?
```

### 6. Viet meta tags
```
Viet Title Tag (<=60 ky tu) va Meta Description (<=155 ky tu) 
cho bai viet nay: [DAN NOI DUNG]
Keyword chinh: [TU KHOA]
```

### 7. Kiem tra SEO on-page
```
Kiem tra bai viet nay co dung chuan SEO on-page khong:
- Title tag, meta description
- H1, H2 structure
- Internal links
- Keyword density
- FAQ section
[DAN BAI VIET]
```

### 8. Tao local landing page
```
Viet local landing page cho 30Shine tai [THANH PHO].
Can co: danh sach chi nhanh, bang gia, review, FAQ.
```

### 9. Research keyword cluster
```
Mo rong keyword "[TU KHOA GOC]" thanh cluster 15-20 long-tail keywords.
Phan loai theo intent: informational, commercial, transactional, local.
```

### 10. Tao progress report
```
Tu data nay, tao progress report SEO:
- Organic Sessions: [SO]
- Baseline: 44,982
- Muc tieu: 67,473
- Keywords da track: [DANH SACH]
[DAN DATA GA4 / RANKING]
```

---

## TIPS SU DUNG HIEU QUA

1. **Cu the = tot hon.** "Phan tich keyword nhuom phu bac cho 30Shine" tot hon "phan tich keyword"
2. **Dan data vao.** Antigravity lam viec tot hon khi co data that (GA4, ranking, reviews)
3. **Dung yeu cau format.** "Tra loi dang bang" hoac "Tra loi dang danh sach" giup output de dung hon
4. **Kiem chung voi Gemini.** 2 AI dong y = insight manh. 2 AI khac nhau = can research them
5. **Iterate.** Output lan 1 chua tot? Noi cu the cho can chinh gi → chay lai. Thuong lan 2-3 se tot hon nhieu

---

## KHI GAP LOI

| Van de | Cach sua |
|--------|---------|
| "command not found" | Cai lai: `npm install -g @anthropic-ai/claude-code` |
| "authentication error" | Chay `claude` va dang nhap lai |
| Output qua ngan | Them "Viet chi tiet, it nhat 1500 tu" vao prompt |
| Output generic | Them context: "cho 30Shine, 150 salon, nam 26-37 VN" |
| Output sai thong tin | Dan data that vao prompt (gia, so salon, ten dich vu) |
