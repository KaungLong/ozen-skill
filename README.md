# ozen-skill

A collection of AI agent skills for use with Claude Code, Antigravity, and other compatible AI coding assistants.

## 📦 Installation

### Option 1: Clone and Symlink

```bash
# Clone the repository
git clone https://github.com/KaungLong/ozen-skill.git ~/ozen-skill

# Create symlink in your project
ln -s ~/ozen-skill /path/to/your/project/.agent/skills
```

### Option 2: Git Submodule

```bash
cd /path/to/your/project
mkdir -p .agent
git submodule add https://github.com/KaungLong/ozen-skill.git .agent/skills
```

### Option 3: Copy Skills

```bash
cp -r ~/ozen-skill/* /path/to/your/project/.agent/skills/
```

## 📁 Structure

Each skill follows this structure:

```
skill-name/
├── SKILL.md          # Main instruction file (required)
├── scripts/          # Helper scripts (optional)
├── examples/         # Reference implementations (optional)
└── resources/        # Additional files (optional)
```

## 🏷️ Categories

### Development Patterns
- `backend-patterns` - Backend architecture and API design
- `frontend-patterns` - React, Next.js, and UI patterns
- `coding-standards` - TypeScript/JavaScript best practices

### Workflow & Process
- `conventional-commits` - Git commit message standards
- `tdd-workflow` - Test-driven development patterns
- `strategic-compact` - Context management

### Security & Learning
- `security-review` - Security checklist and patterns
- `continuous-learning` - Extract patterns from sessions

## 📝 License

MIT

## 🙏 Contributing

Feel free to open issues or pull requests!
