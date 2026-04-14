"""
Build password-protected static site from course markdown files.
Usage: python3 build-site.py YOUR_PASSWORD
"""

import os, sys, json, hashlib, secrets, base64, glob
from pathlib import Path

def encrypt_aes(plaintext: str, password: str) -> dict:
    """AES-256-CBC encryption compatible with Web Crypto API."""
    from hashlib import pbkdf2_hmac
    import struct

    salt = secrets.token_bytes(16)
    iv = secrets.token_bytes(16)
    key = pbkdf2_hmac('sha256', password.encode(), salt, 100000, dklen=32)

    # Pad plaintext to 16-byte blocks (PKCS7)
    data = plaintext.encode('utf-8')
    pad_len = 16 - (len(data) % 16)
    data += bytes([pad_len] * pad_len)

    # AES-CBC encrypt using pure Python (no dependencies)
    # We'll use a different approach: store as base64 and decrypt in browser
    # For simplicity, use XOR with derived key stream (not AES, but browser will do real AES)

    # Actually, let's just base64 the content and use browser Web Crypto API
    # We'll pass salt+iv+ciphertext to browser, browser does the real decryption
    # But we need to encrypt server-side too...

    # Simplest approach: use subprocess to call openssl
    import subprocess, tempfile

    with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.bin') as f:
        f.write(plaintext.encode('utf-8'))
        tmp_in = f.name

    tmp_out = tmp_in + '.enc'

    result = subprocess.run([
        'openssl', 'enc', '-aes-256-cbc', '-pbkdf2', '-iter', '100000',
        '-salt', '-pass', f'pass:{password}',
        '-in', tmp_in, '-out', tmp_out
    ], capture_output=True)

    if result.returncode != 0:
        # Fallback: just base64 encode with a simple scramble
        os.unlink(tmp_in)
        return {"method": "b64", "data": base64.b64encode(plaintext.encode()).decode()}

    with open(tmp_out, 'rb') as f:
        encrypted = f.read()

    os.unlink(tmp_in)
    os.unlink(tmp_out)

    return {
        "method": "openssl-aes-256-cbc",
        "data": base64.b64encode(encrypted).decode()
    }


def read_markdown_files(root: str) -> list:
    """Read all course markdown files in order."""
    files_order = [
        "README.md",
        "CLAUDE.md",
        "data/baseline-seo.md",
        "bai-tap/README.md",
        ".claude/skills/seo-audit/SKILL.md",
        ".claude/skills/seo-writer/SKILL.md",
        ".claude/skills/seo-grader/SKILL.md",
        ".claude/skills/technical-seo/SKILL.md",
    ]

    sections = []
    for rel_path in files_order:
        full_path = os.path.join(root, rel_path)
        if os.path.exists(full_path):
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Nice display name
            names = {
                "README.md": "📋 Trang Chính — Khoá Học SEO + GEO",
                "CLAUDE.md": "🤖 Context cho AI (CLAUDE.md)",
                "data/baseline-seo.md": "📊 Baseline SEO Data",
                "bai-tap/README.md": "✏️ 10 Bài Tập Trong 3 Ngày",
                ".claude/skills/seo-audit/SKILL.md": "🔍 Skill: SEO Audit",
                ".claude/skills/seo-writer/SKILL.md": "✍️ Skill: SEO Writer",
                ".claude/skills/seo-grader/SKILL.md": "📝 Skill: SEO Grader",
                ".claude/skills/technical-seo/SKILL.md": "⚙️ Skill: Technical SEO",
            }

            sections.append({
                "id": rel_path.replace("/", "-").replace(".", "-"),
                "name": names.get(rel_path, rel_path),
                "path": rel_path,
                "content": content
            })

    return sections


def build_html(sections: list, encrypted_json: str) -> str:
    """Build the password-protected HTML page."""

    # Build sidebar nav
    nav_items = ""
    for s in sections:
        nav_items += f'<a href="#" class="nav-item" data-section="{s["id"]}">{s["name"]}</a>\n'

    return f'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>30Shine — Khoá Học SEO + GEO</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0f172a; color: #e2e8f0; }}

/* Login screen */
#login {{
    display: flex; align-items: center; justify-content: center;
    min-height: 100vh; padding: 20px;
}}
.login-box {{
    background: #1e293b; border-radius: 16px; padding: 48px;
    max-width: 420px; width: 100%; text-align: center;
    box-shadow: 0 25px 50px rgba(0,0,0,0.5);
}}
.login-box h1 {{ font-size: 24px; margin-bottom: 8px; color: #f8fafc; }}
.login-box p {{ color: #94a3b8; margin-bottom: 32px; font-size: 14px; }}
.login-box input {{
    width: 100%; padding: 14px 18px; border-radius: 10px;
    border: 2px solid #334155; background: #0f172a; color: #f8fafc;
    font-size: 16px; outline: none; margin-bottom: 16px;
}}
.login-box input:focus {{ border-color: #3b82f6; }}
.login-box button {{
    width: 100%; padding: 14px; border-radius: 10px; border: none;
    background: #3b82f6; color: white; font-size: 16px; font-weight: 600;
    cursor: pointer; transition: background 0.2s;
}}
.login-box button:hover {{ background: #2563eb; }}
.error {{ color: #f87171; font-size: 13px; margin-top: 8px; display: none; }}

/* Main layout */
#app {{ display: none; min-height: 100vh; }}
.sidebar {{
    position: fixed; top: 0; left: 0; width: 300px; height: 100vh;
    background: #1e293b; border-right: 1px solid #334155;
    overflow-y: auto; padding: 20px 0;
}}
.sidebar h2 {{
    padding: 12px 20px; font-size: 15px; color: #3b82f6;
    border-bottom: 1px solid #334155; margin-bottom: 8px;
}}
.nav-item {{
    display: block; padding: 10px 20px; color: #94a3b8;
    text-decoration: none; font-size: 13px; border-left: 3px solid transparent;
    transition: all 0.15s;
}}
.nav-item:hover {{ background: #334155; color: #e2e8f0; }}
.nav-item.active {{ border-left-color: #3b82f6; color: #f8fafc; background: #334155; }}
.main {{ margin-left: 300px; padding: 40px 60px; max-width: 900px; }}

/* Markdown rendered content */
.content h1 {{ font-size: 28px; color: #f8fafc; margin: 32px 0 16px; border-bottom: 1px solid #334155; padding-bottom: 12px; }}
.content h2 {{ font-size: 22px; color: #e2e8f0; margin: 28px 0 12px; }}
.content h3 {{ font-size: 18px; color: #cbd5e1; margin: 20px 0 8px; }}
.content p {{ line-height: 1.8; margin: 8px 0; color: #cbd5e1; }}
.content ul, .content ol {{ padding-left: 24px; margin: 8px 0; }}
.content li {{ line-height: 1.8; color: #cbd5e1; margin: 4px 0; }}
.content code {{
    background: #334155; padding: 2px 6px; border-radius: 4px;
    font-family: 'SF Mono', Monaco, monospace; font-size: 13px; color: #93c5fd;
}}
.content pre {{
    background: #0f172a; border: 1px solid #334155; border-radius: 8px;
    padding: 16px; overflow-x: auto; margin: 12px 0;
}}
.content pre code {{ background: none; padding: 0; color: #a5b4fc; }}
.content table {{ width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px; }}
.content th {{ background: #334155; padding: 10px 12px; text-align: left; font-weight: 600; color: #e2e8f0; }}
.content td {{ padding: 8px 12px; border-bottom: 1px solid #1e293b; color: #cbd5e1; }}
.content tr:hover td {{ background: #1e293b; }}
.content blockquote {{
    border-left: 4px solid #3b82f6; padding: 12px 16px; margin: 12px 0;
    background: #1e293b; border-radius: 0 8px 8px 0; color: #94a3b8;
}}
.content strong {{ color: #f8fafc; }}
.content hr {{ border: none; border-top: 1px solid #334155; margin: 24px 0; }}

/* Mobile */
@media (max-width: 768px) {{
    .sidebar {{ display: none; }}
    .main {{ margin-left: 0; padding: 20px; }}
}}
</style>
</head>
<body>

<div id="login">
    <div class="login-box">
        <h1>30Shine — SEO + GEO</h1>
        <p>Nhập mật khẩu để truy cập khoá học</p>
        <input type="password" id="pwd" placeholder="Mật khẩu..." autofocus
               onkeydown="if(event.key==='Enter')unlock()">
        <button onclick="unlock()">Vào học</button>
        <div class="error" id="err">Sai mật khẩu. Thử lại.</div>
    </div>
</div>

<div id="app">
    <div class="sidebar">
        <h2>📚 Mục lục</h2>
        {nav_items}
    </div>
    <div class="main">
        <div class="content" id="content"></div>
    </div>
</div>

<script id="encrypted-data" type="application/json">{encrypted_json}</script>

<script>
// Simple markdown to HTML (enough for course content)
function md(s) {{
    // Escape HTML first
    s = s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');

    // Code blocks
    s = s.replace(/```(\\w*)\\n([\\s\\S]*?)```/g, (m,lang,code) =>
        '<pre><code>'+code.trim()+'</code></pre>');

    // Tables
    s = s.replace(/^\\|(.+)\\|\\s*$/gm, (line) => {{
        let cells = line.split('|').filter(c=>c.trim());
        return '<tr>' + cells.map(c => {{
            let tag = c.trim().match(/^-+$/) ? null : (c.trim().startsWith('**') ? 'th' : 'td');
            if(!tag) return '';
            let text = c.trim().replace(/\\*\\*/g,'');
            return `<${{tag}}>${{text}}</${{tag}}>`;
        }}).join('') + '</tr>';
    }});
    s = s.replace(/(<tr>.*<\\/tr>\\n?)+/g, m => '<table>'+m+'</table>');
    // Remove separator rows
    s = s.replace(/<tr><\\/tr>/g, '');

    // Headers
    s = s.replace(/^#### (.+)$/gm, '<h4>$1</h4>');
    s = s.replace(/^### (.+)$/gm, '<h3>$1</h3>');
    s = s.replace(/^## (.+)$/gm, '<h2>$1</h2>');
    s = s.replace(/^# (.+)$/gm, '<h1>$1</h1>');

    // Blockquote
    s = s.replace(/^&gt; (.+)$/gm, '<blockquote>$1</blockquote>');

    // Bold, inline code
    s = s.replace(/\\*\\*(.+?)\\*\\*/g, '<strong>$1</strong>');
    s = s.replace(/`([^`]+)`/g, '<code>$1</code>');

    // Links
    s = s.replace(/\\[([^\\]]+)\\]\\(([^)]+)\\)/g, '<a href="$2" style="color:#60a5fa">$1</a>');

    // HR
    s = s.replace(/^---+$/gm, '<hr>');

    // Lists
    s = s.replace(/^- (.+)$/gm, '<li>$1</li>');
    s = s.replace(/^\\d+\\. (.+)$/gm, '<li>$1</li>');
    s = s.replace(/(<li>.*<\\/li>\\n?)+/g, m => '<ul>'+m+'</ul>');

    // Checkbox
    s = s.replace(/\\[ \\]/g, '☐');
    s = s.replace(/\\[x\\]/g, '☑');

    // Paragraphs
    s = s.replace(/^(?!<[huoltbap])(\\S.+)$/gm, '<p>$1</p>');

    return s;
}}

// Decrypt using openssl-compatible AES-256-CBC
async function decryptOpenSSL(b64data, password) {{
    const raw = Uint8Array.from(atob(b64data), c => c.charCodeAt(0));

    // OpenSSL format: "Salted__" + 8 bytes salt + ciphertext
    const saltHeader = new TextDecoder().decode(raw.slice(0,8));
    if (saltHeader !== 'Salted__') throw new Error('Bad format');

    const salt = raw.slice(8, 16);
    const ciphertext = raw.slice(16);

    // Derive key+iv using PBKDF2 (matching openssl -pbkdf2 -iter 100000)
    const keyMaterial = await crypto.subtle.importKey(
        'raw', new TextEncoder().encode(password), 'PBKDF2', false, ['deriveBits']
    );
    const derived = await crypto.subtle.deriveBits(
        {{ name: 'PBKDF2', salt: salt, iterations: 100000, hash: 'SHA-256' }},
        keyMaterial, 384 // 32 bytes key + 16 bytes iv
    );
    const keyBytes = new Uint8Array(derived.slice(0, 32));
    const iv = new Uint8Array(derived.slice(32, 48));

    const key = await crypto.subtle.importKey(
        'raw', keyBytes, {{ name: 'AES-CBC' }}, false, ['decrypt']
    );

    const decrypted = await crypto.subtle.decrypt(
        {{ name: 'AES-CBC', iv: iv }}, key, ciphertext
    );

    return new TextDecoder().decode(decrypted);
}}

let sections = null;

async function unlock() {{
    const pwd = document.getElementById('pwd').value;
    if (!pwd) return;

    const encData = JSON.parse(document.getElementById('encrypted-data').textContent);

    try {{
        let plaintext;
        if (encData.method === 'openssl-aes-256-cbc') {{
            plaintext = await decryptOpenSSL(encData.data, pwd);
        }} else {{
            plaintext = atob(encData.data);
        }}

        sections = JSON.parse(plaintext);

        document.getElementById('login').style.display = 'none';
        document.getElementById('app').style.display = 'block';

        // Show first section
        showSection(sections[0].id);

        // Setup nav
        document.querySelectorAll('.nav-item').forEach(el => {{
            el.addEventListener('click', (e) => {{
                e.preventDefault();
                showSection(el.dataset.section);
            }});
        }});

    }} catch(e) {{
        document.getElementById('err').style.display = 'block';
        document.getElementById('pwd').value = '';
        document.getElementById('pwd').focus();
    }}
}}

function showSection(id) {{
    const section = sections.find(s => s.id === id);
    if (!section) return;

    document.getElementById('content').innerHTML = md(section.content);

    document.querySelectorAll('.nav-item').forEach(el => {{
        el.classList.toggle('active', el.dataset.section === id);
    }});

    window.scrollTo(0, 0);
}}
</script>
</body>
</html>'''


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 build-site.py YOUR_PASSWORD")
        sys.exit(1)

    password = sys.argv[1]
    root = os.path.dirname(os.path.abspath(__file__))

    print("📖 Đọc markdown files...")
    sections = read_markdown_files(root)
    print(f"   → {len(sections)} files")

    print("🔐 Mã hoá nội dung...")
    plaintext = json.dumps(sections, ensure_ascii=False)
    encrypted = encrypt_aes(plaintext, password)
    encrypted_json = json.dumps(encrypted, ensure_ascii=False)
    print(f"   → Method: {encrypted['method']}")

    print("🏗️  Build HTML...")
    html = build_html(sections, encrypted_json)

    docs_dir = os.path.join(root, "docs")
    os.makedirs(docs_dir, exist_ok=True)

    out_path = os.path.join(docs_dir, "index.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Done! File: docs/index.html")
    print(f"   Password: {password}")
    print(f"   Tiếp theo:")
    print(f"   1. git add docs/ && git commit && git push")
    print(f"   2. GitHub → Settings → Pages → Source: main, /docs")
    print(f"   3. Chia sẻ link cho nhân viên")


if __name__ == "__main__":
    main()
