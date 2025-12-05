#!/usr/bin/env python3
"""
WRITTEN BY CLAUDE AI 
Synchronize Hugo publication folders from master bibliography.
Master .bib files in /static/files/ are the source of truth.

This script:
1. Parses brazeau_publications.bib
2. Creates/updates Hugo publication folders in /content/publication/
3. Generates index.md with proper frontmatter
4. Creates individual cite.bib files

Usage:
    python3 scripts/sync-publications.py [--dry-run]

Requirements:
    pip install bibtexparser pyyaml
"""

import bibtexparser
from bibtexparser.bparser import BibTexParser
from pathlib import Path
import yaml
import re
import argparse
from datetime import datetime

def parse_authors(author_string):
    """Parse BibTeX author string into list of names."""
    if not author_string:
        return []

    # Split by ' and '
    authors = author_string.split(' and ')

    # Clean up each author name
    cleaned_authors = []
    for author in authors:
        author = author.strip()
        if author:
            cleaned_authors.append(author)

    return cleaned_authors

def create_hugo_frontmatter(entry):
    """Generate Hugo frontmatter dictionary from BibTeX entry."""

    # Extract basic metadata
    title = entry.get('title', '').strip('{}')
    authors = parse_authors(entry.get('author', ''))
    year = entry.get('year', '2020')
    journal = entry.get('journal', '')
    doi = entry.get('doi', '')
    pmid = entry.get('pmid', '')

    # Create frontmatter
    frontmatter = {
        'title': title,
        'authors': authors,
        'date': f"{year}-01-01",  # Default to Jan 1 if no specific date
        'publication_types': ["2"],  # 2 = Journal article
        'publication': journal,
        'publication_short': journal,
        'draft': False,
    }

    # Add optional fields
    if doi:
        frontmatter['doi'] = doi

    if pmid:
        frontmatter['url_pdf'] = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"

    if 'abstract' in entry:
        frontmatter['abstract'] = entry['abstract'].strip('{}')

    # Add tags (can be customized)
    frontmatter['tags'] = []
    frontmatter['categories'] = []

    return frontmatter

def create_cite_bib(entry):
    """Generate BibTeX entry string for cite.bib."""
    entry_type = entry.get('ENTRYTYPE', 'article')
    citation_key = entry.get('ID', 'unknown')

    # Start BibTeX entry
    bib_lines = [f"@{entry_type}{{{citation_key},"]

    # Add fields in standard order
    field_order = ['author', 'title', 'journal', 'year', 'volume', 'number', 'pages', 'doi', 'pmid', 'pmcid', 'note']

    for field in field_order:
        if field in entry and entry[field]:
            value = entry[field]
            bib_lines.append(f"  {field} = {{{value}}},")

    # Close entry (remove trailing comma)
    if bib_lines[-1].endswith(','):
        bib_lines[-1] = bib_lines[-1][:-1]
    bib_lines.append("}")

    return '\n'.join(bib_lines)

def sync_publication(entry, hugo_base, dry_run=False):
    """Sync a single publication to Hugo folder."""
    citation_key = entry.get('ID', 'unknown')
    title = entry.get('title', '').strip('{}')

    folder = hugo_base / citation_key

    print(f"  Processing: {citation_key}")
    print(f"    Title: {title[:60]}...")

    # Create folder if doesn't exist
    if not dry_run:
        folder.mkdir(exist_ok=True)
    else:
        if not folder.exists():
            print(f"    Would create: {folder}")

    # Generate index.md
    index_md = folder / 'index.md'
    frontmatter = create_hugo_frontmatter(entry)

    # Check if index.md exists and preserve custom fields
    if index_md.exists():
        print(f"    Updating existing index.md")
        # Read existing frontmatter
        with open(index_md) as f:
            content = f.read()
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    existing_fm = yaml.safe_load(parts[1])
                    # Preserve custom fields (featured, projects, images, custom URLs)
                    custom_fields = ['featured', 'projects', 'image', 'url_code', 'url_dataset', 'url_poster', 'url_slides', 'url_source', 'url_video']
                    for field in custom_fields:
                        if field in existing_fm:
                            frontmatter[field] = existing_fm[field]
    else:
        print(f"    Creating new index.md")

    # Write index.md
    if not dry_run:
        with open(index_md, 'w') as f:
            f.write('---\n')
            yaml.dump(frontmatter, f, default_flow_style=False, allow_unicode=True)
            f.write('---\n')

    # Write cite.bib
    cite_bib = folder / 'cite.bib'
    bib_content = create_cite_bib(entry)

    if not dry_run:
        with open(cite_bib, 'w') as f:
            f.write(bib_content)
    else:
        if not cite_bib.exists():
            print(f"    Would create cite.bib")
        else:
            print(f"    Would update cite.bib")

def sync_all(master_bib_path, hugo_base_path, dry_run=False):
    """Main sync function."""

    print(f"Reading master bibliography: {master_bib_path}")

    # Parse master .bib file
    with open(master_bib_path) as bibtex_file:
        parser = BibTexParser(common_strings=True)
        bib_database = bibtexparser.load(bibtex_file, parser=parser)

    entries = bib_database.entries
    print(f"Found {len(entries)} publications in master .bib\n")

    # Sync each entry
    created = 0
    updated = 0

    for entry in entries:
        citation_key = entry.get('ID', 'unknown')
        folder = hugo_base_path / citation_key

        if folder.exists():
            updated += 1
        else:
            created += 1

        sync_publication(entry, hugo_base_path, dry_run=dry_run)
        print()  # Blank line between entries

    # Summary
    print("="*60)
    print("Sync Summary:")
    print(f"  Total publications: {len(entries)}")
    print(f"  New folders created: {created}")
    print(f"  Existing folders updated: {updated}")

    if dry_run:
        print("\n  DRY RUN - No changes were made")
        print("  Run without --dry-run to apply changes")
    else:
        print("\n  Changes have been written to disk")
        print("  Review with 'git status' and commit when ready")

def main():
    parser = argparse.ArgumentParser(description='Sync Hugo publication folders from master .bib file')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without making changes')
    args = parser.parse_args()

    # Paths (relative to repository root)
    repo_root = Path(__file__).parent.parent
    master_bib = repo_root / 'static' / 'files' / 'brazeau_publications.bib'
    hugo_pubs = repo_root / 'content' / 'publication'

    # Validate paths
    if not master_bib.exists():
        print(f"ERROR: Master bibliography not found: {master_bib}")
        print("This script must be run from the repository root or scripts directory")
        return 1

    if not hugo_pubs.exists():
        print(f"ERROR: Hugo publications directory not found: {hugo_pubs}")
        return 1

    # Run sync
    sync_all(master_bib, hugo_pubs, dry_run=args.dry_run)

    return 0

if __name__ == "__main__":
    exit(main())
