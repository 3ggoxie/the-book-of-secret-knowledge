#!/usr/bin/env python3
"""
Convert README.md to mdbook structure.
"""

import re
import os
from pathlib import Path

def html_to_md_links(text):
    """Convert HTML link format to Markdown."""
    # Pattern: &nbsp;&nbsp; <a href="URL"><b>TITLE</b></a> - DESC<br>
    pattern = r'&nbsp;&nbsp;\s*<a href="([^"]+)"><b>([^<]+)</b></a>\s*-\s*([^<]+)<br>'
    replacement = r'- [\2](\1) - \3'
    text = re.sub(pattern, replacement, text)

    # Pattern with * marker for unavailable
    pattern = r'&nbsp;&nbsp;\s*<a href="([^"]+)"><b>([^<]+)</b></a>\s*-\s*([^<]+)<b>\*</b><br>'
    replacement = r'- [\2](\1) - \3 *'
    text = re.sub(pattern, replacement, text)

    return text

def clean_html_tags(text):
    """Remove HTML tags and convert to clean Markdown."""
    # Remove <p> tags but keep content
    text = re.sub(r'<p>\s*', '', text)
    text = re.sub(r'</p>\s*', '\n', text)

    # Remove <br> tags
    text = re.sub(r'<br>\s*', '\n', text)

    # Clean up &nbsp;
    text = re.sub(r'&nbsp;', ' ', text)

    # Clean up &lt; and &gt;
    text = re.sub(r'&lt;', '<', text)
    text = re.sub(r'&gt;', '>', text)

    # Remove TOC links
    text = re.sub(r'\s*\[<sup>\[TOC\]</sup>\]', '', text)

    return text

def convert_chapter_header(line):
    """Convert chapter header from HTML to Markdown."""
    line = re.sub(r'####\s+', '## ', line)
    line = re.sub(r'&nbsp;', ' ', line)
    line = re.sub(r'\s*\[<sup>\[TOC\]</sup>\].*', '', line)
    line = line.strip()
    return line

def convert_subchapter_header(line):
    """Convert subchapter header from HTML to Markdown."""
    line = re.sub(r'#####\s*:black_small_square:\s*', '', line)
    line = line.strip()
    return line

def slugify(name):
    """Convert name to slug for filename."""
    name = name.lower()
    name = re.sub(r'[^a-z0-9]+', '-', name)
    name = re.sub(r'^-|-$', '', name)
    return name

def parse_readme(readme_path):
    """Parse README.md and return structured data."""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    chapters = []
    current_chapter = None
    current_subchapter = None

    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Chapter header: starts with #### but not #####
        if line.startswith('#### ') and not line.startswith('#####'):
            if current_chapter and current_subchapter:
                current_chapter['subchapters'].append({
                    'name': current_subchapter['name'],
                    'content': '\n'.join(current_subchapter['content'])
                })
                current_subchapter = None
            if current_chapter:
                chapters.append(current_chapter)

            current_chapter = {
                'name': convert_chapter_header(line),
                'subchapters': []
            }
            i += 1
            continue

        # Subchapter header: starts with ##### :black_small_square:
        if line.startswith('##### :black_small_square:'):
            if current_subchapter and current_chapter:
                current_chapter['subchapters'].append({
                    'name': current_subchapter['name'],
                    'content': '\n'.join(current_subchapter['content'])
                })

            current_subchapter = {
                'name': convert_subchapter_header(line),
                'content': []
            }
            i += 1
            continue

        # Sub-subchapter header: starts with ##### Tool:
        if line.startswith('##### Tool:'):
            if current_subchapter and current_chapter:
                current_chapter['subchapters'].append({
                    'name': current_subchapter['name'],
                    'content': '\n'.join(current_subchapter['content'])
                })

            tool_match = re.search(r'##### Tool:\s*\[([^\]]+)\]', line)
            tool_name = tool_match.group(1) if tool_match else 'unknown'
            current_subchapter = {
                'name': tool_name,
                'content': []
            }
            # Add this line to content
            current_subchapter['content'].append(line)
            i += 1
            continue

        # Regular content line - add to current subchapter if exists
        if current_subchapter is not None:
            current_subchapter['content'].append(line)

        i += 1

    # Don't forget the last subchapter and chapter
    if current_subchapter and current_chapter:
        current_chapter['subchapters'].append({
            'name': current_subchapter['name'],
            'content': '\n'.join(current_subchapter['content'])
        })
    if current_chapter:
        chapters.append(current_chapter)

    return chapters

def write_files(chapters, base_dir):
    """Write chapter and subchapter files."""
    for chapter in chapters:
        chapter_slug = slugify(chapter['name'].replace('## ', ''))
        chapter_dir = base_dir / chapter_slug

        if not chapter['subchapters']:
            continue

        chapter_dir.mkdir(parents=True, exist_ok=True)

        # Write README for chapter
        readme_content = f"# {chapter['name']}\n\n"
        readme_content += f"This section contains {chapter['name']} resources.\n\n"
        readme_content += "## Contents\n\n"
        for sub in chapter['subchapters']:
            sub_slug = slugify(sub['name'])
            readme_content += f"- [{sub['name']}]({sub_slug}.md)\n"

        (chapter_dir / 'README.md').write_text(readme_content, encoding='utf-8')

        # Write each subchapter
        for sub in chapter['subchapters']:
            sub_slug = slugify(sub['name'])
            content = sub['content']

            # Convert HTML to Markdown
            content = html_to_md_links(content)
            content = clean_html_tags(content)

            # If content doesn't start with a heading, add one
            lines = content.split('\n')
            first_line = lines[0] if lines else ''
            if first_line.strip().startswith('#####'):
                # It's a Tool header that was converted, use as-is
                final_content = content
            elif first_line.strip().startswith('#'):
                final_content = content + "\n"
            else:
                final_content = f"# {sub['name']}\n\n{content}\n"

            (chapter_dir / f'{sub_slug}.md').write_text(final_content, encoding='utf-8')

def main():
    script_dir = Path(__file__).parent
    readme_path = script_dir.parent / 'README.md'
    src_dir = script_dir.parent / 'src'

    print(f"Reading {readme_path}...")
    chapters = parse_readme(readme_path)

    print(f"Found {len(chapters)} chapters:")
    for ch in chapters:
        print(f"  - {ch['name']}: {len(ch['subchapters'])} subchapters")
        for sub in ch['subchapters']:
            print(f"      - {sub['name']}: {len(sub['content'].split(chr(10)))} lines")

    print(f"\nWriting files to {src_dir}...")
    write_files(chapters, src_dir)

    print("Done!")

if __name__ == '__main__':
    main()