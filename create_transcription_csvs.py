import os
import csv

strip_extensions = ["wav", "mp3", "ogg"]

columns = ["id", "script", "inflection", "comment", "type", "suppress"]
default = {}
for c in columns:
    default[c] = ""


def main():
    pwd = os.getcwd()

    subfolders = [f for f in os.scandir(pwd) if f.is_dir()]

    for dir in subfolders:
        if dir.name.startswith("."):
            continue

        files = [f.path[0:-4] for f in os.scandir(dir) if f.is_file()]

        csv_filename = os.path.join(pwd, f"{os.path.basename(dir)}_transcriptions.csv")

        if os.path.exists(csv_filename):
            raise Exception(
                f"Found existing CSV which we will not overwrite:\n{csv_filename}"
            )

        with open(csv_filename, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=columns)
            w.writeheader()

            rows = [{**default, "id": os.path.basename(x)} for x in files]

            w.writerows(rows)


if __name__ == "__main__":
    main()
