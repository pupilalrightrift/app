"""
Prosta aplikacja z harmonogramem uruchamiana przez GitHub Actions.
Przy każdym wywołaniu dopisuje znacznik czasu do log.txt.
Tu możesz podłączyć własną logikę: sprawdzanie ceny produktu,
generowanie raportu Excel, wysyłkę powiadomienia itd.
"""

from datetime import datetime, timezone

LOG_FILE = "log.txt"


def run_task() -> str:
    now_utc = datetime.now(timezone.utc)
    entry = f"[{now_utc.strftime('%Y-%m-%d %H:%M:%S')} UTC] Zadanie wykonane.\n"
    return entry


def main() -> None:
    entry = run_task()
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)
    print(entry.strip())


if __name__ == "__main__":
    main()
