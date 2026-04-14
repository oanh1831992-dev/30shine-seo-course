---
name: technical-seo
description: Audit technical SEO cơ bản cho 30shine.com. Kiểm tra page speed, mobile, sitemap, robots.txt, meta tags trang dịch vụ. Output là báo cáo gửi dev team.
user-invocable: true
---

# Skill: Technical SEO Audit

## Khi người dùng gọi skill này

Kiểm tra các yếu tố technical SEO cơ bản của 30shine.com. Nhân viên MKT KHÔNG cần sửa code — chỉ cần tạo báo cáo rõ ràng gửi dev team.

### Bước 1: Kiểm tra trang dịch vụ chính

Dùng WebFetch để kiểm tra các URL sau:
- `30shine.com`
- `30shine.com/dich-vu-cat-toc`
- `30shine.com/dich-vu-goi-massage-spa-relax`
- `30shine.com/dich-vu-uon-nhuom-duong-toc`
- `30shine.com/dich-vu-uon-cao-cap`
- `30shine.com/chi-tiet-dich-vu-lay-ray-tai`

Với mỗi trang, kiểm tra:
- Có Title Tag không? Nội dung gì? Có chứa keyword không?
- Có Meta Description không? Nội dung gì? Có CTA không?
- Có H1 không? Có trùng Title Tag không?
- Có Structured Data (JSON-LD) không? Loại gì?
- Nội dung có đủ dày không? (ước lượng số từ — dưới 300 từ là quá mỏng)
- Có internal link đến trang booking không?

### Bước 2: Kiểm tra sitemap và robots.txt

- Fetch `30shine.com/sitemap.xml` — có tồn tại không? Có đầy đủ URL trang dịch vụ không?
- Fetch `30shine.com/robots.txt` — có chặn Googlebot ở trang quan trọng nào không?

### Bước 3: Hướng dẫn kiểm tra Page Speed

Hướng dẫn nhân viên tự kiểm tra (AI không fetch được PageSpeed):
1. Mở https://pagespeed.web.dev/
2. Nhập `30shine.com` → chạy test
3. Ghi lại:
   - **Performance Score** (mobile): dưới 50 = tệ, 50-89 = trung bình, 90+ = tốt
   - **LCP (Largest Contentful Paint):** dưới 2.5s = tốt
   - **CLS (Cumulative Layout Shift):** dưới 0.1 = tốt
   - **Ảnh chưa compress:** liệt kê nếu có

### Bước 4: Kiểm tra Google Business Profile

Hướng dẫn nhân viên kiểm tra GBP cho 3-5 chi nhánh trọng điểm:
1. Search trên Google: `30shine [địa chỉ chi nhánh]`
2. Kiểm tra GBP listing:
   - Tên có đúng "30Shine" (nhất quán) không?
   - Danh mục có đúng (Hair Salon / Barber Shop) không?
   - Giờ mở cửa có cập nhật không?
   - Có ảnh mới (trong 3 tháng gần nhất) không?
   - Có trả lời review gần đây không?
   - Có GBP Posts không?

### Bước 5: Tạo báo cáo

Output format:

```markdown
## Báo cáo Technical SEO — 30shine.com
Ngày kiểm tra: [ngày]
Người kiểm tra: [tên]

### 1. Trang dịch vụ
| URL | Title Tag | Meta Desc | H1 | Schema | Số từ ước lượng | Vấn đề |
|-----|-----------|-----------|----|---------| --------|-------|
| /dich-vu-cat-toc | ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... | ... |

### 2. Sitemap & Robots.txt
- Sitemap: [OK / Thiếu / Lỗi — chi tiết]
- Robots.txt: [OK / Đang chặn trang quan trọng — chi tiết]

### 3. Page Speed (từ PageSpeed Insights)
- Mobile Score: [số]/100
- LCP: [số]s
- CLS: [số]
- Vấn đề chính: [liệt kê]

### 4. Google Business Profile (3-5 chi nhánh)
| Chi nhánh | Tên đúng? | Danh mục? | Giờ cập nhật? | Ảnh mới? | Trả lời review? |
|-----------|----------|----------|-------------|---------|---------------|
| ... | ... | ... | ... | ... | ... |

### 5. Đề xuất cho Dev Team (ưu tiên cao → thấp)
1. [KHẨN CẤP] ...
2. [QUAN TRỌNG] ...
3. [CẢI THIỆN] ...

### 6. Đề xuất cho Marketing Team
1. [GBP] ...
2. [Content] ...
3. [Internal linking] ...
```

**Lưu ý quan trọng:**
- Nhân viên MKT chỉ cần tạo báo cáo, KHÔNG cần tự sửa code
- Phần "Đề xuất cho Dev Team" gửi cho dev, phần "Đề xuất cho Marketing Team" tự thực hiện
- Chạy audit này 1 lần/tháng để theo dõi cải thiện

**LUÔN viết tiếng Việt có dấu đầy đủ.**
