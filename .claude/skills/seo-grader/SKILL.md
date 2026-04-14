---
name: seo-grader
description: Chấm điểm bài tập SEO của nhân viên. Cho điểm 1-10 theo rubric chuẩn, nhận xét cụ thể, yêu cầu sửa nếu dưới 8.
user-invocable: true
---

# Skill: Chấm Điểm Bài Tập SEO

## Khi người dùng paste bài tập và yêu cầu chấm

### Xác định loại bài tập
1. **Keyword Audit** → dùng Rubric A
2. **Blog SEO** → dùng Rubric B
3. **Local Landing Page** → dùng Rubric C
4. **Counter-Content** → dùng Rubric D
5. **Progress Report** → dùng Rubric E

### Rubric A: Keyword Audit
| Tiêu chí | Trọng số | 9-10 | 7-8 | 5-6 | <5 |
|----------|---------|------|-----|-----|-----|
| Đủ 20 keyword | 25% | Đủ 20 + phân loại intent | 15-19 keyword | 10-14 keyword | Dưới 10 |
| Chính xác | 25% | Ghi đúng vị trí rank, tên đối thủ | Ghi vị trí nhưng thiếu chi tiết | Ghi chung chung | Không ghi |
| Phân tích | 25% | Insight cụ thể, có số liệu, có logic | Đúng nhưng chưa sâu | Mơ chung | Không phân tích |
| Sử dụng AI | 25% | Dùng Antigravity + Gemini, kiểm chứng chéo | Dùng tốt 1 AI | Chỉ copy paste | Không dùng |

### Rubric B: Blog SEO
| Tiêu chí | Trọng số | 9-10 | 7-8 | 5-6 | <5 |
|----------|---------|------|-----|-----|-----|
| SEO On-page | 25% | Đủ tất cả checklist | Thiếu 1-2 mục | Thiếu 3-4 mục | Thiếu nhiều |
| Nội dung | 30% | Số liệu thật, đặc trưng 30Shine, đọc hay | Đúng nhưng chưa nổi bật | Generic | Copy paste AI |
| GEO readiness | 25% | FAQ Schema đúng, AI trích dẫn được | Có FAQ nhưng thiếu schema | FAQ quá ít | Không có |
| Sử dụng AI | 20% | Antigravity + Gemini, kiểm chứng chéo | Dùng tốt 1 AI | Chỉ copy paste | Không dùng |

### Rubric C: Local Landing Page
| Tiêu chí | Trọng số |
|----------|---------|
| Thông tin chi nhánh đầy đủ (địa chỉ, giờ, booking) | 25% |
| Bảng giá cụ thể, cập nhật 2026 | 20% |
| FAQ ≥5 câu đặc thù cho thành phố | 20% |
| Review thật từ khách hàng | 20% |
| Internal link + local keyword | 15% |

### Rubric D: Counter-Content
| Tiêu chí | Trọng số | Lưu ý |
|----------|---------|-------|
| Thuyết phục | 30% | Có số liệu chứng minh |
| Trung thực | 25% | **NẾU CHỈ CA NGỢI MÀ KHÔNG NHẬN ĐIỂM YẾU → ĐIỂM = 3** |
| Review thật | 25% | Có chi tiết: tên, chi nhánh, dịch vụ, ngày |
| SEO + GEO | 20% | Keyword, FAQ, structured content |

### Output chấm điểm
```
## Kết quả chấm điểm

**Loại bài:** [Keyword Audit / Blog SEO / ...]
**Điểm tổng:** X/10

### Chi tiết
| Tiêu chí | Điểm | Nhận xét |
|----------|------|----------|
| ... | ... | ... |

### Điểm mạnh
- ...

### Cần cải thiện
- ...

### Yêu cầu (nếu dưới 8 điểm)
- Sửa phần [X] theo gợi ý trên
- Nộp lại sau khi sửa
```

**LUÔN viết tiếng Việt có dấu đầy đủ.**
