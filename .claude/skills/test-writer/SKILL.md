---
name: test-writer
description: Write unit tests for any function — happy path, edge cases, and error cases. Use when the user asks for tests, wants to add test coverage, or is practicing TDD.
---

Ask the user to share the function or code they want tests for.

Then write tests covering:

## Tests for `[functionName]`

**Testing framework:** [detect from package.json — Jest, Vitest, pytest, etc. Ask if unclear]

---

### Happy path
Test the expected behavior with valid inputs. One test per meaningful variation.

```[language]
test('returns [expected] when given [input]', () => {
  // arrange
  // act
  // assert
})
```

### Edge cases
Tests for boundary conditions and unusual but valid inputs:
- Empty input (empty string, empty array, 0)
- Single item
- Maximum size or value
- Special characters (if string input)

### Error cases
Tests that verify the function fails correctly:
- Invalid input types
- Null/undefined inputs
- Inputs that should trigger error handling

### Mock requirements
List any external dependencies (API calls, database queries, file system) that need mocking, with example mock setup.

---

**Coverage target:** Aim for all branches, not just lines. Flag any branch that is difficult to test and explain why.

Write tests that read like documentation — the test name should be a sentence explaining what the function does in that scenario.
