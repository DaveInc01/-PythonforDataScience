def main():
    import datetime as dt
    now = dt.datetime.now()
    timestamp = now.timestamp()
    scientific = f"{timestamp:.2e}"
    month = now.strftime("%B")
    day = now.strftime("%d")
    year = now.strftime("%Y")
    print(f"Seconds since January 1, 1970: {timestamp:,} or {scientific}  in scientific notation\n{month} {day} {year}")


if __name__ == "__main__":
    main()