---
name: dockerfile-generator
description: Create a production-ready Dockerfile and deployment config for any project. Optimized for small image size and security. Use when the user wants to containerize their app or deploy to Fly.io, Railway, or any Docker-based platform.
---

Ask the user:
1. "What language and framework? (e.g. Python/FastAPI, Node/Next.js, Go)"
2. "What platform are you deploying to? (Fly.io, Railway, Cloud Run, self-hosted)"
3. "Any environment variables the app needs at runtime?"

Then produce:

## Dockerfile

```dockerfile
# [explanation of each stage]
```

**What this Dockerfile does:**
- Base image choice and why
- Multi-stage build explanation (if used)
- How dependencies are cached for fast rebuilds
- Non-root user setup (security)
- Health check configuration

---

## Platform config (if applicable)

**fly.toml** (for Fly.io):
```toml
# minimal fly.toml
```

**Commands to deploy:**
```bash
# step-by-step deployment commands
```

---

## .dockerignore
```
node_modules/
.env
.env.local
*.log
.git
```

---

**Security checklist:**
- [ ] App runs as non-root user
- [ ] No secrets in the image layers
- [ ] Only production dependencies installed
- [ ] Health check defined
- [ ] Image size under [target — e.g. 200MB for Node, 100MB for Python Alpine]

---

Flag any environment variable that looks like a secret — confirm it's being passed at runtime, not baked into the image.
