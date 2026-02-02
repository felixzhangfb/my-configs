# Make sure scripts and non-interactive shells can find executables

## uv, ruff etc
source "$HOME/.local/bin/env"

## python as global default interpreter with default packages
case ":${PATH}:" in
    *:"/Library/Frameworks/Python.framework/Versions/3.14/bin":*)
        ;;
    *)
        export PATH="/Library/Frameworks/Python.framework/Versions/3.14/bin:$PATH"
        ;;
esac

## cargo, rustc, rustup, rustfmt etc
source "$HOME/.cargo/env"

## volta, node, npm, pnpm etc
case ":${PATH}:" in
    *:"$HOME/.volta/bin":*)
        ;;
    *)
        export PATH="$HOME/.volta/bin:$PATH"
        ;;
esac

## postgres, psql etc
case ":${PATH}:" in
    *:"/opt/homebrew/opt/postgresql@18/bin":*)
        ;;
    *)
        export PATH="/opt/homebrew/opt/postgresql@18/bin:$PATH"
        ;;
esac
