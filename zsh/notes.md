# What is the source sequence for .zprofile, .zshenv and .zshrc?

Below is the **actual source order on macOS (zsh)**, plus what each file is *meant* for.

---

## 1. The real source sequence (zsh)

### 🔑 Always first (every zsh invocation)

```text
/etc/zshenv
~/.zshenv
```

👉 **Always sourced**, even for:

* non-interactive shells
* scripts
* `zsh -c`
* subshells

⚠️ Keep this file **minimal**.

---

### 🔐 Login shells only

Triggered by:

* Terminal.app (default)
* iTerm2 (default)
* `zsh -l`

Order:

```text
/etc/zprofile
~/.zprofile
```

Use for:

* PATH
* LANG / LC_*
* toolchain env vars (JAVA_HOME, GOPATH, etc.)

---

### 💬 Interactive shells only

Triggered by:

* Terminal tabs
* `zsh` inside an existing shell

Order:

```text
/etc/zshrc
~/.zshrc
```

Use for:

* aliases
* functions
* prompt
* keybindings
* plugins (Oh My Zsh, etc.)

---

### 🚪 Logout (when exiting a login shell)

```text
/etc/zlogout
~/.zlogout
```

Rarely used.

---

## 2. Full matrix (easy mental model)

| File        | Always | Login    | Interactive | Purpose            |
| ----------- | ------ | -------- | ----------- | ------------------ |
| `.zshenv`   | ✅      | ✅        | ✅           | minimal env only   |
| `.zprofile` | ❌      | ✅        | ❌           | login env setup    |
| `.zshrc`    | ❌      | ❌        | ✅           | interactive config |
| `.zlogout`  | ❌      | ✅ (exit) | ❌           | cleanup            |

---

## 3. What macOS Terminal actually loads

Terminal.app opens:

* **login shell**
* **interactive shell**

So you get:

```text
.zshenv
.zprofile
.zshrc
```

iTerm2 does the same by default.

---

## 4. Where `.profile` fits in

`.profile` is **not** a zsh file.

It’s read by:

* `sh`
* `bash`

If you want compatibility:

```sh
# ~/.zprofile
[ -f ~/.profile ] && source ~/.profile
```

This is very common on macOS.

---

## 5. Common mistakes (and why things break)

❌ Putting aliases in `.zprofile`
→ not loaded in interactive non-login shells

❌ Heavy stuff in `.zshenv`
→ slows *every* zsh invocation (even scripts)

❌ PATH edits in `.zshrc` only
→ GUI apps won’t see them

---

## 6. Recommended clean setup (macOS)

```sh
# ~/.zshenv
# (almost empty)
export ZDOTDIR=$HOME
```

```sh
# ~/.zprofile
[ -f ~/.profile ] && source ~/.profile
export PATH="/opt/homebrew/bin:$PATH"
```

```sh
# ~/.zshrc
alias l='ls -lah'
plugins=(git docker)
```

---

## TL;DR (one screen)

```text
zshenv   → always
zprofile → login shells
zshrc   → interactive shells
```
