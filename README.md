# R-Like Scripting Lexical Analyzer (Python PLY)

Repositori kolaborasi **Group Assignment - Project 1: Lexical Analyzer Development** untuk mata kuliah **Compilation Technique (Kelas LD07)**, BINUS University.

---

## Identitas Kelompok (Group 2 — R-Like Scripting)

- **Dosen Pengampu**: Dr. (cand) Johannes Simatupang, S.Kom, M.Kom, COBIT5
- **Topik Bahasa**: R-Like Scripting (Python PLY)
- **Repository GitHub**: `https://github.com/Hyphen-14/r-script-lexer`
- **Batas Pengumpulan**: 21 November 2026 (`Johannes.simatupang@binus.ac.id`)

### Anggota Kelompok & Pembagian Tugas Kolaboratif

Seluruh anggota bekerja secara setara (*flat teamwork* tanpa hierarki). Saat inisialisasi awal repositori, **Core Lexer (`src/r_lexer.py`)**, file input sampel, serta struktur instruksi proyek telah disiapkan agar setiap anggota dapat langsung mengerjakan dan melakukan *commit* pada bagian masing-masing:

| No | NIM | Nama Lengkap | Bagian Tugas & File | Status Awal Repo |
|---|---|---|---|---|
| 1 | `2802495051` | **Yasin Taryaqil Aghyar** | Core Lexer (`src/r_lexer.py`), Setup Repository & Panduan | **Selesai** |
| 2 | `2802438754` | **Nathasa Bintang Kayesa** | Kasus 1 (`src/case1_simple_statement.py`) & Laporan PDF (`docs/LAPORAN_PROJECT1_COMPTECH.md`) | Template siap diisi |
| 3 | `2802521932` | **Athallah Rafif Rijal Belvana** | Kasus 2 (`src/case2_arithmetic.py`) & CLI Runner (`run_all.py`) | Template siap diisi |
| 4 | `2802431395` | **Samuel Tristan Ryansyah** | Kasus 3 (`src/case3_conditional_if.py`) & Materi Slide / Video Presentasi | Template siap diisi |
| 5 | `2802515261` | **Early Achiril Putra** | Kasus 4 (`src/case4_looping.py`) & Unit Test / Error Check (`tests/test_r_lexer.py`) | Template siap diisi |

---

## Tujuan Proyek

Membangun **Lexical Analyzer (Lexer)** berbasis **Python PLY (`ply.lex`)** untuk membaca kode sumber bahasa **R-Like Scripting**, mengenali setiap unit token (*token stream*) secara terstruktur, serta menangani kesalahan leksikal (*lexical errors*) pada **4 kasus uji** sesuai slide tugas halaman 17–20.

> **Catatan Ketentuan Pengumpulan (Slide 2 & Slide 3):**
> - Harus ada **4 source code Python Lexical Analyzer mandiri** (1 file per kasus) yang dapat dijalankan dan dipresentasikan.
> - Source code jawaban dikumpulkan dalam format **file Python (`.py`) dan PDF**.
> - Mencantumkan **Nama Group** dan seluruh **Anggota Group (NIM & Nama)**.
> - Disertai **Video Recording Presentasi** berdurasi maksimal **10 menit**.

---

## 4 Studi Kasus Input (Slide 17–20)

### 1. Kasus 1 — Simple Statement (`sample_inputs/case1_input.R`)
```r
print("Hello, world!")
cat(“Thanks")
```
*(Perhatikan adanya tanda kutip pembuka Unicode `“` pada `cat(“Thanks")` di slide soal).*

### 2. Kasus 2 — Simple Arithmetic Expression (`sample_inputs/case2_input.R`)
```r
num1 <- 10
num2 <- 20
num3 <- 30
sum <- num1+num2+num3
avg <- sum / 3
cat("num1 is ", num1, "\n")
cat("num2 is ", num2, "\n")
cat("num3 is ", num3, "\n")
cat("Sum 3 numbers is ", sum, "\n")
cat("Average is ", avg, "\n")
```

### 3. Kasus 3 — Simple Conditional IF with Block (`sample_inputs/case3_input.R`)
```r
#R version 3.4.4 
num1 <- 10
num2 <- 20
if (num1>num2) {
bignum <- num1;
cat("Big Number is ", bignum, "\n")
} else {
bignum <- num2;
cat("Big Number is ", bignum, "\n")
}
```

### 4. Kasus 4 — Simple Looping with Conditional IF Block (`sample_inputs/case4_input.R`)
```r
#R version 3.4.4 
cat("List of Odd Number 1-100: \n")
num<-1
while (num <= 100) {
sisa <- (num %% 2) 
if (sisa != 0) {
oddnum <- num
cat(oddnum," ");
}
num <- num + 1 
}
```

---

## Spesifikasi Token Acuan (Agar Seragam Antar Anggota)

Gunakan nama token dan aturan pola berikut sebagai acuan bersama (sesuai implementasi di [`src/r_lexer.py`](src/r_lexer.py)):

| Kategori | Nama Token | Pola Regex / Aturan | Contoh |
|---|---|---|---|
| **Keywords / Built-in** | `PRINT`, `CAT`, `IF`, `ELSE`, `WHILE` | Dicocokkan via dictionary `reserved` di dalam `t_ID` | `print`, `cat`, `if`, `else`, `while` |
| **Assignment Operator** | `ASSIGN` | `<-` | `num1 <- 10` |
| **Arithmetic Operators** | `PLUS`, `MINUS`, `TIMES`, `DIVIDE`, `MODULO` | `\+`, `-`, `\*`, `/`, `%%` | `num1+num2`, `num %% 2` |
| **Relational Operators** | `LE`, `GE`, `EQ`, `NE`, `LT`, `GT` | `<=`, `>=`, `==`, `!=`, `<`, `>` | `num <= 100`, `sisa != 0`, `num1>num2` |
| **Delimiters** | `LPAREN`, `RPAREN`, `LBRACE`, `RBRACE`, `COMMA`, `SEMICOLON` | `\(`, `\)`, `\{`, `\}`, `,`, `;` | `(`, `)`, `{`, `}`, `,`, `;` |
| **Literals** | `NUMBER`, `STRING` | `\d+(?:\.\d+)?` dan literal kutip (`"..."`, `'...'`, `“..."`) | `10`, `3.14`, `"Hello, world!"` |
| **Identifier** | `ID` | `[a-zA-Z_][a-zA-Z0-9_.]*` | `num1`, `bignum`, `sisa`, `oddnum` |
| **Comments & Whitespace** | *(Ignored)* | `\#[^\n]*` dan `[ \t\r]`; `\n+` menaikkan `t.lexer.lineno` | `#R version 3.4.4` |

---

## Struktur Direktori Repository

```text
r-script-lexer/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── run_all.py                      # [Tugas Athallah] Runner CLI gabungan ke-4 kasus
├── src/
│   ├── __init__.py
│   ├── r_lexer.py                  # [Tugas Yasin - Selesai] Core Engine Lexer R-Like PLY
│   ├── case1_simple_statement.py   # [Tugas Nathasa] Template Kasus 1 siap dikerjakan
│   ├── case2_arithmetic.py         # [Tugas Athallah] Template Kasus 2 siap dikerjakan
│   ├── case3_conditional_if.py     # [Tugas Samuel] Template Kasus 3 siap dikerjakan
│   └── case4_looping.py            # [Tugas Early] Template Kasus 4 siap dikerjakan
├── sample_inputs/
│   ├── case1_input.R               # Input R Kasus 1 (Slide 17)
│   ├── case2_input.R               # Input R Kasus 2 (Slide 18)
│   ├── case3_input.R               # Input R Kasus 3 (Slide 19)
│   └── case4_input.R               # Input R Kasus 4 (Slide 20)
├── tests/
│   ├── __init__.py
│   └── test_r_lexer.py             # [Tugas Early] Template unit test unittest
└── docs/
    └── LAPORAN_PROJECT1_COMPTECH.md # [Tugas Nathasa & Tim] Kerangka laporan PDF & alur video
```

---

## Panduan Pengerjaan Per Anggota

1. **Yasin Taryaqil Aghyar (`2802495051`) — Selesai**
   - Sudah membangun modul inti [`src/r_lexer.py`](src/r_lexer.py) (`build_lexer`, `tokenize_code`, `format_token_table`), menyediakan input sampel `.R`, serta menyiapkan struktur repositori dan dokumentasi ini.
   - Uji cepat modul inti:
     ```bash
     python -c "from src.r_lexer import format_token_table; print(format_token_table('x <- 10'))"
     ```
2. **Nathasa Bintang Kayesa (`2802438754`)**
   - Buka [`src/case1_simple_statement.py`](src/case1_simple_statement.py) dan lengkapi implementasi lexer PLY mandiri untuk Kasus 1 sesuai panduan di dalam komentar file.
   - Lengkapi laporan dan masukkan screenshot hasil eksekusi ke [`docs/LAPORAN_PROJECT1_COMPTECH.md`](docs/LAPORAN_PROJECT1_COMPTECH.md) lalu ekspor ke PDF.
3. **Athallah Rafif Rijal Belvana (`2802521932`)**
   - Buka [`src/case2_arithmetic.py`](src/case2_arithmetic.py) dan lengkapi implementasi lexer PLY mandiri untuk Kasus 2.
   - Bangun CLI runner di [`run_all.py`](run_all.py) untuk menjalankan ke-4 kasus sekaligus dan menampilkan ringkasan token.
4. **Samuel Tristan Ryansyah (`2802431395`)**
   - Buka [`src/case3_conditional_if.py`](src/case3_conditional_if.py) dan lengkapi implementasi lexer PLY mandiri untuk Kasus 3 (komentar `#`, `if`/`else`, operator relasional, blok `{}`).
   - Siapkan slide presentasi dan koordinasikan penyuntingan Video Presentasi (durasi maksimal 10 menit).
5. **Early Achiril Putra (`2802515261`)**
   - Buka [`src/case4_looping.py`](src/case4_looping.py) dan lengkapi implementasi lexer PLY mandiri untuk Kasus 4 (`while`, `<=`, `%%`, `!=`).
   - Lengkapi unit test di [`tests/test_r_lexer.py`](tests/test_r_lexer.py) untuk menguji seluruh kasus dan penanganan lexical error.

---

## Cara Setup & Kontribusi ke GitHub

### 1. Clone Repository & Setup Environment
```bash
git clone https://github.com/Hyphen-14/r-script-lexer.git
cd r-script-lexer

python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 2. Alur Pengerjaan & Push Kontribusi (Git Workflow)
Agar tidak terjadi konflik antar file dan kontribusi setiap anggota tercatat rapi di riwayat GitHub:

1. **Pastikan repo lokal terbaru**:
   ```bash
   git pull origin main
   ```
2. **Buat branch sesuai bagian masing-masing**:
   ```bash
   # Contoh untuk Nathasa:
   git checkout -b feat/case1-nathasa
   # Contoh untuk Athallah:
   git checkout -b feat/case2-athallah
   # Contoh untuk Samuel:
   git checkout -b feat/case3-samuel
   # Contoh untuk Early:
   git checkout -b feat/case4-early
   ```
3. **Kerjakan & uji file masing-masing** (misalnya `python src/case1_simple_statement.py`).
4. **Commit & Push ke GitHub**:
   ```bash
   git add <file-yang-dikerjakan>
   git commit -m "feat(case1): implement simple statement lexical analyzer"
   git push -u origin <nama-branch>
   ```
5. **Buat Pull Request (PR)** di GitHub menuju branch `main` untuk di-merge bersama tim.
