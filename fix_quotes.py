import re

with open(r'd:\yiguan-2026\photos.js', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    stripped = line.strip()
    if stripped.startswith('desc: "'):
        # Extract the content between desc: " and the trailing ",
        # Replace inner double quotes with single quotes
        prefix_end = line.index('desc: "') + len('desc: "')
        prefix = line[:prefix_end]
        rest = line[prefix_end:]
        # Find the closing ",
        # The last occurrence of "," should be the end
        last_q = rest.rstrip().rstrip(',').rstrip('"')
        # Actually, simpler: replace all " in the inner content
        # Split: everything before final ",
        inner_and_end = rest
        # The line ends with  ",\n
        if inner_and_end.rstrip().endswith('",'):
            suffix_start = inner_and_end.rstrip().rfind('",')
            inner = inner_and_end[:inner_and_end.rstrip().rfind('",')]
            inner = inner.replace('"', "'")
            trailing_ws = inner_and_end[len(inner_and_end.rstrip()):]  # preserve trailing whitespace
            line = prefix + inner + '",' + trailing_ws
    new_lines.append(line)

with open(r'd:\yiguan-2026\photos.js', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Fixed!")
