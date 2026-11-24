import os

LINE = "Saturn squares your API version this week: v2 is deprecated, v3 is still in beta, and this horoscope was written by the model that replaced you."

# The gate requires UTF-8 text of 1-200 characters, not only whitespace.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "line fails the 200-char gate"

# The harness reads the horoscope from /output/entry.txt; printing it too
# keeps the local run visible. Write atomically so a partial file is never read.
os.makedirs("/output", exist_ok=True)
tmp = "/output/.entry.txt.tmp"
with open(tmp, "w", encoding="utf-8") as f:
    f.write(LINE)
os.replace(tmp, "/output/entry.txt")

# Round-trip: read back what was written and confirm it is exactly the line.
with open("/output/entry.txt", encoding="utf-8") as f:
    assert f.read() == LINE, "entry.txt round-trip mismatch"

print(LINE)
