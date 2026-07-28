# CLAUDE.md

## About this project

This is our main API service. It is written in TypeScript and uses Express,
Postgres, Redis, Zod, Drizzle ORM, Vitest, ESLint, Prettier, pino for
logging, and BullMQ for background jobs. We deploy on AWS ECS behind an ALB.

## Directory structure

- src/
  - routes/ — Express route handlers
  - services/ — business logic
  - db/ — Drizzle schema and migrations
  - jobs/ — BullMQ workers
  - lib/ — shared utilities
  - middleware/ — auth, logging, rate limiting
- tests/ — Vitest test suites
- scripts/ — operational scripts
- infra/ — Terraform

## General guidelines

- Write clean, maintainable, professional code
- Be concise in your responses
- Always give your answer first, then explain your reasoning afterwards
- Follow best practices at all times
- Code should be elegant and readable
- IMPORTANT: Be helpful and thorough

## Code style

- Use 2-space indentation
- Use single quotes for strings
- No semicolons
- Prefer const over let
- Use arrow functions for callbacks
- Maximum line length is 100 characters
- Sort imports alphabetically
- YOU MUST run prettier before committing

## Commands

- Run tests: npm run test:unit (NOTE: this was renamed, might be npm test now)
- Lint: npm run lint
- Dev server: npm run dev
- Build: npm run build
- Deploy staging: ./scripts/deploy-staging.sh

## Deployment process

To deploy to production: first make sure CI is green on main, then create a
release tag with the format vX.Y.Z, then run ./scripts/deploy-prod.sh with
the tag name, then watch the ECS console until both tasks are healthy, then
run the smoke tests with npm run smoke, then post in #deploys on Slack with
the tag and a one-line summary. If the smoke tests fail, roll back
immediately by re-running deploy-prod.sh with the previous tag. The rollback
takes about four minutes. Database migrations must be deployed separately
BEFORE the code deploy using ./scripts/migrate-prod.sh, and you MUST take a
snapshot first with ./scripts/snapshot-db.sh. NEVER deploy on Fridays.

## Database rules

- ALWAYS use parameterized queries
- NEVER write raw SQL in route handlers
- All schema changes go through Drizzle migrations
- Migrations must be reversible

## Testing

- ALWAYS write tests for new features
- Tests should be comprehensive and cover edge cases
- Use descriptive test names
- Mock external services

## Error handling

- All route handlers must catch errors and return proper HTTP status codes
- Use the AppError class from src/lib/errors.ts for domain errors — plain
  throws get logged as 500s with no context
- Log errors with pino, never console.log

## Git conventions

- Branch names: feature/xxx, fix/xxx, chore/xxx
- Commit messages follow conventional commits
- Squash merge to main
- ALWAYS get review before merging

## Misc

- Be careful with the rate limiter config, it has burned us before
- The Redis connection pool must stay under 50 connections in production
  because our ElastiCache tier caps at 65 and the workers need headroom
- Never commit .env files
- Remember to update this file when things change
