import os

LINE = "Tabhoard (n.) — the 47 browser tabs you refuse to close because one of them might be important."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.getcwd()
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
