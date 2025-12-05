# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is Nick Brazeau's personal academic website built with Hugo and the Academic theme. The site showcases research publications, blog posts, projects, and CV.

**Site URL**: https://nicholasbrazeau.com/
**Framework**: Hugo 0.128.0 with Academic theme
**Deployment**: GitHub Pages via GitHub Actions
**Content**: 46+ publications, active blog, 10+ research projects

### Project Goals

**Primary Objective**: Maintain a comprehensive website highlighting research, publications, and achievements while keeping content current and accessible.

---

## Architecture Philosophy

This repository implements a multi-agent system for efficient website management:

- **Single source of truth**: Master .bib files in `/static/files/` are authoritative for all publication data
- **Automation first**: Repetitive tasks automated via scripts and CI/CD
- **Agent specialization**: Each agent has narrow, clear responsibilities with minimal overlap
- **Human-in-the-loop**: Agents stage changes; user reviews and commits manually
- **Read-heavy**: Agents prioritize exploration and recommendation over immediate changes

---

## 🧠 Behavioral Directives

- **Prioritize readability and navigation**: Content should be easy to find and consume
- **Never embellish**: Only factual information about research and achievements
- **Keep links up-to-date**: Validate DOI, PMID, and external URLs regularly
- **Maintain active blog**: Publish quality content regularly
- **Always attribute Claude.AI**: Include `*Post drafted with assistance from Claude.AI*` on all blog posts
- **Stage changes only**: Never auto-commit; user reviews all changes before committing

---

## 📁 Repository Structure

```
nickbrazeau.github.io/
├── .claude/
│   └── commands/          # Specialized agent definitions
│       ├── librarian.md
│       ├── publication-manager.md
│       ├── maestro.md
│       ├── blogger.md
│       ├── designer.md
│       ├── link-maintenance.md
│       └── deployment.md
├── .github/
│   └── workflows/
│       └── hugo.yml        # CI/CD pipeline (includes CV auto-compilation)
├── content/
│   ├── publication/        # 46+ publication folders (synced from master .bib)
│   ├── post/               # Blog posts
│   ├── project/            # Research projects
│   ├── authors/            # Author profiles
│   └── home/               # Homepage widgets
├── static/
│   ├── files/
│   │   ├── cv.tex          # CV LaTeX source (manually maintained)
│   │   ├── cv.pdf          # CV PDF (auto-compiled)
│   │   ├── brazeau_publications.bib      # MASTER: All publications
│   │   └── brazeau_first_author.bib      # SUBSET: First author pubs
│   └── img/                # Images and assets
├── layouts/                # Custom Hugo layouts (extends theme)
├── themes/
│   └── hugo-academic/      # Hugo Academic theme
├── scripts/                # Automation scripts
│   ├── sync-publications.py    # Sync Hugo from .bib (to be created)
│   └── check-links.py          # Link validation (to be created)
├── blogdrafts/             # Draft blog posts (not published)
├── config.toml             # Hugo site configuration
└── CLAUDE.md               # This file
```

---

## 🤖 Agents System

### Available Agents

1. **Librarian** (`/librarian`) - CV and master bibliography management
2. **Publication Manager** (`/publication-manager`) - Hugo publication folder synchronization
3. **Blogger** (`/blogger`) - Blog content creation and maintenance
4. **Website Designer** (`/designer`) - Layout, UX, and accessibility
5. **Link Maintenance** (`/link-maintenance`) - Link validation and monitoring
6. **Deployment Agent** (`/deployment`) - CI/CD and build automation
7. **Maestro** (`/maestro`) - Multi-agent coordination

### When to Use Each Agent

| Task | Agent | Why |
|------|-------|-----|
| Add new publication to .bib and CV | Librarian | Manages master bibliography (source of truth) |
| Sync Hugo publication folders | Publication Manager | Keeps Hugo in sync with master .bib |
| Write or update blog post | Blogger | Maintains consistent blog formatting |
| Fix website layout or styling | Designer | Handles all visual/UX changes |
| Check for broken links | Link Maintenance | Validates URLs across site |
| Fix GitHub Actions build | Deployment | Manages CI/CD pipeline |
| Complex multi-step workflow | Maestro | Coordinates multiple agents |

### Quick Reference

**Single-agent tasks:**
- `/librarian` - Update CV, add publication to .bib
- `/blogger` - Write blog post, suggest topics
- `/designer` - Fix layout, improve accessibility
- `/link-maintenance` - Check links
- `/deployment` - Monitor builds, troubleshoot CI/CD

**Multi-agent tasks (use Maestro):**
- `/maestro Add publication with PMID: 12345678` - Coordinates Librarian + Publication Manager
- `/maestro Quarterly maintenance` - Coordinates all agents for comprehensive check
- `/maestro Sync everything` - Validates and syncs all systems

---

## 📚 File System Architecture

### Single Source of Truth

**Publications:**
- **Master**: `/static/files/brazeau_publications.bib` (all publications)
- **Subset**: `/static/files/brazeau_first_author.bib` (first/co-first author only)
- **Derived**: `/content/publication/*/` (Hugo folders, synced from master .bib)

**CV:**
- **Source**: `/static/files/cv.tex` (manually maintained LaTeX)
- **Generated**: `/static/files/cv.pdf` (auto-compiled from cv.tex)

**Blog:**
- **Drafts**: `/blogdrafts/*.md` (work in progress, not published)
- **Published**: `/content/post/YYYY-topic/index.md` (live on site)

### Data Flow

```
Publications:
  Master .bib → Hugo folders → Website
  (Librarian)   (Pub Manager)  (Hugo build)

CV:
  cv.tex → cv.pdf → Website download
  (Librarian) (GitHub Actions) (Static file)

Blog:
  Draft → Review → Published → Website
  (Blogger)        (Blogger)    (Hugo build)
```

---

## 🔧 Common Workflows

### Adding a New Publication

```bash
/maestro Add publication with PMID: 12345678
```

**What happens:**
1. Librarian fetches metadata from PubMed
2. Librarian adds to `brazeau_publications.bib` (and `brazeau_first_author.bib` if applicable)
3. Librarian updates CV publications section
4. Librarian compiles `cv.pdf`
5. Publication Manager creates Hugo folder in `/content/publication/`
6. GitHub Actions auto-compiles CV PDF on push
7. All changes staged for your review

**Review and commit:**
```bash
git status  # See what changed
git commit -m "Add publication: [Title] (PMID: 12345678)"
git push
```

### Writing a Blog Post

```bash
/blogger
```

**What happens:**
1. You provide initial draft or content
2. Blogger formats with proper YAML frontmatter
3. Blogger refines structure and organization (with your approval)
4. You iterate on the formatted version together
5. When approved, Blogger moves to `/content/post/YYYY-topic/index.md`
6. Changes staged for your review

**Blog post includes:**
- Standardized YAML frontmatter
- Claude AI attribution footer
- Proper categories and tags

**Note:** Blogger helps format and polish your drafts - you create the initial content.

### Quarterly Maintenance

```bash
/maestro Quarterly maintenance
```

**What happens:**
1. Librarian checks ORCID/PubMed for new publications
2. Publication Manager syncs all Hugo folders with master .bib
3. Link Maintenance validates all external links (DOI, PMID, blog URLs)
4. Website Designer audits UX and accessibility
5. Blogger suggests blog post topics
6. Deployment Agent reviews recent build status
7. Maestro generates comprehensive report

**Review report and address issues as needed.**

### Updating Your CV

```bash
/librarian Update my CV with [new position/award/etc.]
```

**What happens:**
1. Librarian reads `cv.tex`
2. Librarian makes requested changes
3. Librarian compiles `cv.pdf`
4. Changes staged for your review

**Auto-compilation:**
- GitHub Actions also compiles CV when cv.tex or .bib files are pushed
- Ensures PDF is always up-to-date with source

### Fixing a Broken Build

```bash
/deployment Why did the build fail?
```

**What happens:**
1. Deployment Agent checks GitHub Actions logs
2. Identifies error (Hugo syntax, LaTeX issue, etc.)
3. Recommends which agent should fix it
4. Provides detailed error report

---

## 🎯 Technical Details

**Hugo:**
- Version: 0.128.0
- Theme: Hugo Academic
- Config: `/config.toml`

**LaTeX:**
- Distribution: TinyTeX (local), texlive (CI/CD)
- Compiler: pdflatex
- CV location: `/static/files/cv.tex`

**Deployment:**
- Platform: GitHub Pages
- Workflow: `.github/workflows/hugo.yml`
- Trigger: Push to main branch
- Build time: ~2-3 minutes

**Base URL:**
- Production: https://nicholasbrazeau.com/
- GitHub Pages: https://nickbrazeau.github.io/

---

## 🔒 Agent Permissions

| Agent | Can Write | Cannot Write |
|-------|-----------|--------------|
| Librarian | cv.tex, *.bib files | Hugo folders, blog posts |
| Publication Manager | Hugo publication folders | Master .bib files, blog posts |
| Blogger | Blog posts, drafts | CV, publications, layouts |
| Designer | Layouts, CSS, config | Content files (md) |
| Link Maintenance | Reports only | Any content files |
| Deployment | GitHub workflows, scripts | Content, CV, layouts |
| Maestro | Reports only | Any files (delegates to others) |

**All agents**: Stage changes only, never auto-commit.

---

## 📋 Maintenance Schedule

**Weekly:**
- Check GitHub Actions for build failures
- Review new blog post ideas

**Monthly:**
- Check for new publications (ORCID, PubMed)
- Review and update CV if needed

**Quarterly:**
- Run `/maestro Quarterly maintenance`
- Full link validation
- Accessibility audit
- Performance check
- Write at least one blog post

**Annually:**
- Major CV update
- Site design review
- Archive old projects if needed

---

## 💡 Best Practices

**For Publications:**
- Always add to master .bib first (via Librarian)
- Let Publication Manager sync Hugo folders automatically
- Don't manually edit Hugo publication folders (they'll be overwritten)

**For Blog Posts:**
- You provide initial drafts/content; Blogger formats and refines
- Always work in `/blogdrafts/` first
- Use consistent frontmatter (Blogger enforces this)
- Include Claude AI attribution
- Move to `/content/post/` only when ready to publish

**For CV:**
- Edit `cv.tex` for content changes
- Let GitHub Actions compile PDF automatically
- If urgent, Librarian can compile locally

**For Design:**
- Test Hugo builds locally before pushing
- Use custom layouts in `/layouts/` (don't modify theme directly)
- Prioritize accessibility and readability

**For Links:**
- Use DOI links (more permanent than publisher URLs)
- Include PMID/PMCID when available
- Run link checks quarterly

---

## 🚨 Troubleshooting

**Build fails after pushing:**
```bash
/deployment Why did the build fail?
```

**Publications out of sync:**
```bash
/publication-manager Sync all publications
```

**Broken links:**
```bash
/link-maintenance Check all links
```

**CV won't compile:**
```bash
/librarian  # Then report the LaTeX error
```

**Need help with complex task:**
```bash
/maestro [describe what you need]
```

---

## 📝 Notes

- This multi-agent system was implemented in December 2024
- Master .bib files are the single source of truth for publications
- CV PDF auto-compiles in GitHub Actions when source files change
- All agents follow "stage only, never commit" policy
- The system is designed to be extended - new agents can be added as needed

---

## 🔗 Quick Links

- **Live Site**: https://nicholasbrazeau.com/
- **GitHub Repo**: https://github.com/nickbrazeau/nickbrazeau.github.io
- **ORCID**: 0000-0003-3976-7965
- **Hugo Docs**: https://gohugo.io/documentation/
- **Theme Docs**: https://wowchemy.com/docs/

---

For questions about specific agents or workflows, invoke the relevant agent (e.g., `/librarian`, `/blogger`, `/maestro`) and ask!