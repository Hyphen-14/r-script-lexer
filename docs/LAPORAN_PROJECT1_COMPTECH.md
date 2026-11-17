# LAPORAN PROYEK 1: LEXICAL ANALYZER DEVELOPMENT (R-LIKE SCRIPTING)

**Mata Kuliah**: Compilation Technique (Kelas LD07)  
**Dosen Pengampu**: Dr. (cand) Johannes Simatupang, S.Kom, M.Kom, COBIT5  
**Kelompok**: Group 2 — R-Like Scripting  
**Institusi**: BINUS University  
**Batas Pengumpulan**: 21 November 2026 (`Johannes.simatupang@binus.ac.id`)

> **Catatan untuk Tim (PIC Laporan: Nathasa Bintang Kayesa)**:  
> Lengkapi bagian hasil pembahasan dan tempelkan screenshot kode serta output terminal dari masing-masing anggota, lalu ekspor file ini menjadi **PDF** untuk dikumpulkan bersama 4 file `.py` dan video presentasi.

---

## 1. Identitas Anggota Kelompok & Pembagian Tugas Kolaboratif

| No | NIM | Nama Lengkap | Fokus Kontribusi |
|---|---|---|---|
| 1 | `2802495051` | **Yasin Taryaqil Aghyar** | Core Lexer (`src/r_lexer.py`), Setup Repository GitHub & Dokumentasi |
| 2 | `2802438754` | **Nathasa Bintang Kayesa** | Implementasi Kasus 1 (`src/case1_simple_statement.py`) & Penyusunan Laporan PDF |
| 3 | `2802521932` | **Athallah Rafif Rijal Belvana** | Implementasi Kasus 2 (`src/case2_arithmetic.py`) & Pembuatan CLI Runner (`run_all.py`) |
| 4 | `2802431395` | **Samuel Tristan Ryansyah** | Implementasi Kasus 3 (`src/case3_conditional_if.py`), Desain Slide & Editing Video Presentasi |
| 5 | `2802515261` | **Early Achiril Putra** | Implementasi Kasus 4 (`src/case4_looping.py`), Unit Testing (`tests/test_r_lexer.py`) & Error Handling |

---

## 2. Landasan Teori Singkat

### 2.1 Lexical Analyzer (Scanner)
*Lexical Analyzer* adalah tahap awal pada kompiler yang membaca karakter dari *source code*, mengabaikan spasi/komentar yang tidak diperlukan, dan mengelompokkannya menjadi urutan **token** (*lexeme* dan *token type*).

### 2.2 Python PLY (`ply.lex`)
**PLY (Python Lex-Yacc)** menyediakan modul `ply.lex` untuk mendefinisikan aturan token berbasis *Regular Expression* yang menghasilkan objek `LexToken` (`type`, `value`, `lineno`, `lexpos`).

---

## 3. Spesifikasi Token R-Like Scripting

| Kategori | Token Type | Pola Regex / Aturan | Keterangan |
|---|---|---|---|
| **Keywords / Built-in** | `PRINT`, `CAT`, `IF`, `ELSE`, `WHILE` | Dicocokkan dari `ID` via `reserved` | Kata kunci dan fungsi output bawaan R-Like |
| **Assignment Operator** | `ASSIGN` | `<-` | Operator penetapan nilai khas R |
| **Arithmetic Operators** | `PLUS`, `MINUS`, `TIMES`, `DIVIDE`, `MODULO` | `\+`, `-`, `\*`, `/`, `%%` | Operasi matematika dan sisa bagi (`%%`) |
| **Relational Operators** | `LE`, `GE`, `EQ`, `NE`, `LT`, `GT` | `<=`, `>=`, `==`, `!=`, `<`, `>` | Operasi perbandingan pada kondisi `if`/`while` |
| **Delimiters** | `LPAREN`, `RPAREN`, `LBRACE`, `RBRACE`, `COMMA`, `SEMICOLON` | `\(`, `\)`, `\{`, `\}`, `,`, `;` | Pembatas argumen, blok kode, dan statement |
| **Literals** | `NUMBER`, `STRING` | `\d+(?:\.\d+)?` dan literal kutip | Angka integer/float dan string (mendukung kutip standar & smart quotes) |
| **Identifier** | `ID` | `[a-zA-Z_][a-zA-Z0-9_.]*` | Nama variabel (mendukung titik sesuai konvensi R) |
| **Comments & Whitespace** | *(Ignored)* | `\#[^\n]*`, `[ \t\r]`, `\n+` | Komentar & spasi diabaikan; newline menambah `lineno` |

---

## 4. Pembahasan & Hasil Pengujian 4 Kasus (Diisi Setelah Implementasi Selesai)

### 4.1 Kasus 1: Simple Statement (`src/case1_simple_statement.py`)
- **Source Code Python**: *(Tempel kode `case1_simple_statement.py` di sini)*
- **Ringkasan Hasil Token & Screenshot Terminal**: *(Tempel screenshot output terminal Kasus 1 di sini)*

### 4.2 Kasus 2: Simple Arithmetic Expression (`src/case2_arithmetic.py`)
- **Source Code Python**: *(Tempel kode `case2_arithmetic.py` di sini)*
- **Ringkasan Hasil Token & Screenshot Terminal**: *(Tempel screenshot output terminal Kasus 2 di sini)*

### 4.3 Kasus 3: Simple Conditional IF with Block (`src/case3_conditional_if.py`)
- **Source Code Python**: *(Tempel kode `case3_conditional_if.py` di sini)*
- **Ringkasan Hasil Token & Screenshot Terminal**: *(Tempel screenshot output terminal Kasus 3 di sini)*

### 4.4 Kasus 4: Simple Looping with Conditional IF Block (`src/case4_looping.py`)
- **Source Code Python**: *(Tempel kode `case4_looping.py` di sini)*
- **Ringkasan Hasil Token & Screenshot Terminal**: *(Tempel screenshot output terminal Kasus 4 di sini)*

---

## 5. Panduan Alur Presentasi Video (Maksimal 10 Menit)

Video dibagi merata untuk 5 anggota (~1,5–2 menit per orang, total target ~9 menit agar aman di bawah batas maksimal 10 menit):

| Segmen | Durasi | Pembicara | Materi yang Disampaikan |
|---|---|---|---|
| **1. Pembukaan & Core Lexer** | `00:00 – 02:00` | **Yasin Taryaqil Aghyar** | Perkenalan Group 2 (5 anggota), penjelasan tujuan Lexical Analyzer dengan Python PLY, aturan regex di `r_lexer.py`, serta struktur repositori GitHub. |
| **2. Demo & Penjelasan Kasus 1** | `02:00 – 03:45` | **Nathasa Bintang Kayesa** | Penjelasan `case1_simple_statement.py`, penanganan keyword `print`/`cat`, smart quotes, dan demo output Kasus 1. |
| **3. Demo & Penjelasan Kasus 2** | `03:45 – 05:30` | **Athallah Rafif Rijal Belvana** | Penjelasan `case2_arithmetic.py`, tokenisasi operator aritmatika & assignment `<-`, serta demonstrasi CLI runner `run_all.py`. |
| **4. Demo & Penjelasan Kasus 3** | `05:30 – 07:15` | **Samuel Tristan Ryansyah** | Penjelasan `case3_conditional_if.py`, pengabaian komentar `#`, token kondisional `if`/`else`, operator `>`, delimiter `{ }`/`;`, dan demo output Kasus 3. |
| **5. Demo Kasus 4, Testing & Penutup** | `07:15 – 09:15` | **Early Achiril Putra** | Penjelasan `case4_looping.py` (`while`, `<=`, `%%`, `!=`), demonstrasi unit test otomatis & error handling, lalu penutup bersama. |

---

## 6. Checklist Sebelum Pengumpulan ke Email Dosen

- [ ] Seluruh 4 file `.py` (`src/case1_simple_statement.py` s/d `src/case4_looping.py`) berjalan tanpa error.
- [ ] Seluruh unit test (`python -m unittest discover -s tests -p "test_*.py" -v`) lulus 100%.
- [ ] File laporan PDF berisi: Identitas Group 2 + 5 NIM & Nama, Source Code lengkap 4 kasus, dan Screenshot hasil eksekusi.
- [ ] Video presentasi berdurasi <= 10 menit, suara dan layar kode terbaca jelas.
- [ ] Seluruh kontribusi anggota sudah di-push dan di-merge ke `https://github.com/Hyphen-14/r-script-lexer`.
- [ ] Email dikirim paling lambat **21 November 2026** ke `Johannes.simatupang@binus.ac.id` dengan lampiran PDF, 4 file Python, dan link/file video presentasi.
