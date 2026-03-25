import os
import re

def generate_index(root_dir):
    index_content = """# 🗂️ Ozen Team SKILLS_INDEX

> **[🚨 CRITICAL SYSTEM RULE]**
> Do NOT read all SKILL.md files. Always read this index first, find the required skill, and only read its specific `SKILL.md` file when you need to execute it. This is to save context window tokens and prevent AI amnesia.

## Available Skills

"""
    
    # Track skills to prevent duplicates or process structured formatting
    skills = []
    
    for subdir, dirs, files in os.walk(root_dir):
        # Skip hidden directories and node_modules
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        
        for file in files:
            if file == "SKILL.md":
                filepath = os.path.join(subdir, file)
                rel_path = os.path.relpath(filepath, root_dir)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Extract YAML frontmatter between ---
                match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
                name = "Unknown Skill"
                desc = "No description provided."
                tags = ""
                
                if match:
                    frontmatter = match.group(1)
                    # Use regex to find name, description, and tags
                    name_match = re.search(r'^name:\s*(.*)$', frontmatter, re.MULTILINE)
                    tags_match = re.search(r'^tags:\s*(.*)$', frontmatter, re.MULTILINE)
                    if name_match: name = name_match.group(1).strip("'\"")
                    if tags_match: tags = tags_match.group(1).strip("'\"")
                    
                    # Handle multi-line description (YAML > or | syntax)
                    desc_match = re.search(r'^description:\s*(.*)$', frontmatter, re.MULTILINE)
                    if desc_match:
                        first_line = desc_match.group(1).strip("'\"").strip()
                        if first_line in ('>', '|', '>-', '|-'):
                            # Multi-line: collect indented continuation lines
                            desc_start = desc_match.end()
                            remaining = frontmatter[desc_start:]
                            lines = []
                            for line in remaining.split('\n'):
                                stripped = line.strip()
                                if not stripped:
                                    continue  # skip blank lines
                                if line[0] == ' ' or line[0] == '\t':
                                    lines.append(stripped)
                                else:
                                    break  # hit next YAML key
                            desc = ' '.join(lines) if lines else "No description provided."
                        else:
                            desc = first_line
                
                skills.append({
                    "name": name,
                    "path": rel_path,
                    "desc": desc,
                    "tags": tags,
                })

    # Sort alphabetically by name
    skills = sorted(skills, key=lambda x: x['name'].lower())
    
    for skill in skills:
        entry = f"- **{skill['name']}**\n  - 📂 Path: `{skill['path']}`\n  - 📖 Description: {skill['desc']}"
        if skill['tags']:
            entry += f"\n  - 🏷️ Tags: `{skill['tags']}`"
        index_content += entry + "\n\n"
                
    output_path = os.path.join(root_dir, "SKILLS_INDEX.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print(f"✅ Successfully generated SKILLS_INDEX.md with {len(skills)} skills.")

if __name__ == "__main__":
    generate_index('.')

