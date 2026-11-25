#!/usr/bin/env python3
"""Satu kata yang ingin kuhapus dari kamus.

Program kecil ini cuma punya satu tugas: menyimpan satu kata pilihan
ke sebuah berkas bernama entry.txt. Kata itu adalah jawaban atas
pertanyaan bounty — kata mana yang paling layak dicoret dari kamus
bahasa Inggris. Tidak ada masukan dari pengguna, tidak ada pilihan
acak, dan tidak ada keluaran lain di layar; semuanya sesederhana itu.
"""

import os

WORD = "please"


def main():
    """Tulis kata pilihan ke entry.txt tanpa baris baru di ujungnya."""
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    entry_path = os.path.join(target_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
