CONVENTIONAL_COMMITS = """
### Commit Structure:
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Elements:

1. **fix:** commits that fix a bug. Corresponds to a [`PATCH`](http://semver.org/#summary) in Semantic Versioning.
   - Example: `fix: correct load error on mobile devices`

2. **feat:** commits that introduce a new feature. Corresponds to a [`MINOR`](http://semver.org/#summary) in Semantic Versioning.
   - Example: `feat: add share button to posts`

3. **BREAKING CHANGE:** commits or footers that introduce a change that breaks compatibility. Corresponds to a [`MAJOR`](http://semver.org/#summary) in Semantic Versioning. Can be part of any commit type.
   - Footer example:
     ```
     feat: update API to support multi-users
     BREAKING CHANGE: user object structure has been modified
     ```
   - With `!` example: `feat!: remove support for old API version`

4. Other _types_ beyond `fix:` and `feat:` are allowed, like `docs:`, `style:`, `refactor:`, among others.
   - Example: `docs: update code comments for clarity`

5. _footers_ follow a format similar to [git's trailer format](https://git-scm.com/docs/git-interpret-trailers).

6. A scope can be provided to the commit type to give more contextual information.
   - Example: `feat(auth): add two-factor verification`

### Examples:

- **With description and a breaking change footer:**
  ```
  feat: allow config object to extend other configs
  BREAKING CHANGE: the `extends` key in the config file now is used for extending other config files
  ```

- **With `!` signaling a breaking change:**
  ```
  feat!: send an email to the user when a product is shipped
  ```

- **Without a body:**
  ```
  docs: fix typos in CHANGELOG
  ```

- **With scope:**
  ```
  feat(lang): add support for Portuguese language
  ```

- **With a multi-line body and multiple footers:**
  ```
  fix: prevent race conditions
  Adds a request ID and reference to the last request. Discards
  responses that are not from the last request.
  Reviewed-by: Z
  Refs: #123
  ```

### Specifications:

- Commits MUST be prefixed with a type.
- A scope CAN be provided after the type.
- A description MUST immediately follow the type/scope.
- A longer body CAN be provided after the short description.
- One or more footers CAN be provided after the body.
- BREAKING CHANGE SHOULD be in upper case.

These are the main conventions and examples for "Conventional Commits". This convention is useful for maintaining a clear and readable commit history, facilitating automatic changelog generation, and determining semantic versioning.
"""