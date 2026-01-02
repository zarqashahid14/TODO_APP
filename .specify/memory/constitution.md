<!--
Sync Impact Report
- Version change: [NONE] → 1.0.0
- Modified principles: N/A (initial ratification)
- Added sections: All sections (initial constitution)
- Removed sections: N/A
- Templates requiring updates: ✅ plan-template.md, ✅ spec-template.md, ✅ tasks-template.md (all align with principles)
- Follow-up TODOs: None
-->

# Todo Hackathon App Constitution

## Core Principles

### I. Simplicity First (NON-NEGOTIABLE)

Every solution MUST prioritize simplicity and clarity over cleverness. Complex abstractions, unnecessary layers, or over-engineering are prohibited unless explicitly justified with a measurable benefit.

**Rationale**: Hackathon projects have limited time. Complexity increases risk, maintenance burden, and reduces understandability. Simple solutions are easier to test, debug, and deliver within constraints.

**Rules**:
- Prefer explicit over implicit - code should read like prose
- Avoid premature optimization - solve the problem, then measure
- Use existing tools and libraries rather than building custom implementations
- Maximum 3 layers of abstraction for any feature
- If a solution cannot be explained in 2 sentences, it's too complex

---

### II. Testable Features

Every user story and feature MUST be independently testable with clear acceptance criteria. Integration tests are optional unless cross-service communication is involved.

**Rationale**: Independent testing enables incremental delivery, parallel development, and confidence in refactoring. Testable features have clearer boundaries and better design.

**Rules**:
- Each user story defines its own independent test path
- Acceptance scenarios must be executable (Given/When/Then format)
- Tests written first when test-driven approach is selected
- No implementation without at least one test path defined
- Edge cases must be enumerated in specifications

---

### III. MVP-First Delivery

Features MUST be delivered in smallest viable increments. Each increment should provide demonstrable user value without requiring completion of dependent features.

**Rationale**: Hackathon success is measured by delivering working software. MVP-first ensures continuous progress and reduces risk of incomplete delivery.

**Rules**:
- Features decomposed into independently deliverable slices
- P1 stories deliver complete user value on their own
- P2+ stories enhance but don't block P1 functionality
- Each checkpoint produces a working, deployable artifact
- Never implement P2 features if P1 is incomplete

---

### IV. Spec-Driven Development

All features MUST start with a specification (spec.md) before implementation. Planning (plan.md) follows spec, tasks (tasks.md) follow planning, and implementation follows tasks.

**Rationale**: Specifications prevent scope creep, enable parallel development, and document decisions. Without specs, teams build the wrong thing.

**Rules**:
- No code without spec.md (user stories, acceptance criteria)
- No code without plan.md (technical approach, architecture)
- No code without tasks.md (implementation steps)
- All artifacts versioned and linked
- Changes require spec updates first

---

## Technology Stack Constraints

**Primary Stack**: Python 3.11, JavaScript/TypeScript for web frontend
**Storage**: SQLite for MVP (upgradable to PostgreSQL)
**API**: REST/JSON for simplicity (WebSockets only if real-time required)
**Testing**: pytest for backend, appropriate framework for frontend
**Documentation**: Markdown in .specify/ structure

**Rationale**: Standard, well-documented tools reduce learning curve and debugging time during hackathon.

---

## Development Workflow

### Phase Order

1. **Specification** → `/sp.specify` - User stories, acceptance criteria, requirements
2. **Planning** → `/sp.plan` - Architecture, data model, contracts, research
3. **Tasking** → `/sp.tasks` - Concrete implementation steps
4. **Implementation** → Execute tasks in dependency order
5. **Validation** → Run quickstart.md, test acceptance scenarios

### Quality Gates

- No PR without passing tests
- No PR without spec/plan/tasks alignment
- No PR without CLAUDE.md compliance checks
- Breaking changes require ADR documentation

### Code Review Requirements

- Review checks spec.md alignment
- Review checks plan.md adherence
- Review checks complexity principle (3-layer max)
- Review checks testability principle (independent tests)

---

## Governance

**Amendment Procedure**:
- Proposals made as issues with template
- Majority approval required for principle changes
- Minor clarifications can be made via PR with review
- Version bump on ratification (MAJOR.MINOR.PATCH)

**Versioning Policy**:
- MAJOR: Principle removal or fundamental redefinition
- MINOR: New principle or section added
- PATCH: Clarifications, wording refinements

**Compliance Review**:
- All PRs must pass principle checks
- Principle violations require explicit justification in PR description
- Complexity justification requires "Simpler Alternative Rejected Because" table
- Project structure must follow .specify/ conventions

**Authority**:
- Constitution supersedes all other practices
- Conflicts resolved in favor of this document
- Guidance from CLAUDE.md and runtime docs supplements but never overrides

---

**Version**: 1.0.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2025-12-31
