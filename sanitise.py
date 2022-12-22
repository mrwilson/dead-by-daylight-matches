import csv

IGNORED_FIELDS = [
    "date",
    "level",
    "survivor",
    "bloodpoints",
    "notes",
    "noteworthy?",
    "swf",
    "perk_value",
]


def clean(value):
    return value.strip().replace("N/A", "")


with open("survivor.csv", "w") as output:
    with open("survivor_raw.csv", "r") as input:
        input_csv = csv.DictReader(input)
        fields = [
            field for field in input_csv.fieldnames if field not in IGNORED_FIELDS
        ] + ["swf"]

        output_csv = csv.DictWriter(output, fieldnames=fields)
        output_csv.writeheader()

        for row in input_csv:
            columns = {field: clean(row[field]) for field in fields}
            columns["swf"] = "N" if row["swf"] == "" else "Y"

            output_csv.writerow(columns)
