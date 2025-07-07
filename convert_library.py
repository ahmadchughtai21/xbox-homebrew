#!/usr/bin/env python3
import re

# Read the current library.ini file
with open('/home/ahmad/Desktop/xbox-homebrew/library.ini', 'r') as f:
    content = f.read()

# Split into sections
sections = content.split('[GAME')

# Keep the header (first section)
new_content = sections[0]

# Process each game section
for i, section in enumerate(sections[1:], 1):
    if not section.strip():
        continue
    
    # Extract game info using regex
    lines = section.split('\n')
    game_id = f"GAME{i:03d}"
    
    name_match = re.search(r'name=(.+)', section)
    url_match = re.search(r'url=(.+)', section)
    
    if name_match and url_match:
        name = name_match.group(1).strip()
        url = url_match.group(1).strip()
        
        # Create new format
        new_section = f"""[{game_id}]
itemTitle={name}
itemVersion=1.0
itemAuthor=Central Arquivista
itemDescription={name} for Xbox 360
dataurl={url}
path=Games\\{name}\\

"""
        new_content += new_section

# Write the converted file
with open('/home/ahmad/Desktop/xbox-homebrew/library.ini', 'w') as f:
    f.write(new_content)

print("Conversion completed!")
