
#!/bin/bash

ORIGINAL="grades.csv"
ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"

mkdir -p "$ARCHIVE_DIR"

if [ ! -f "$ORIGINAL" ]; then
    echo "Error: grades.csv not found."
    exit 1
fi

TIMESTAMP=$(date +%Y%m%d-%H%M%S)

BASE="${ORIGINAL%.csv}"
ARCHIVED_NAME="${BASE}_${TIMESTAMP}.csv"

mv "$ORIGINAL" "$ARCHIVE_DIR/$ARCHIVED_NAME"

touch "$ORIGINAL"

echo "$TIMESTAMP | Original: $ORIGINAL | Archived: $ARCHIVE_DIR/$ARCHIVED_NAME" >> "$LOG_FILE"

echo "File archived successfully."
echo "New grades.csv created."
