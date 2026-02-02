# Make sure scripts and non-interactive shells can find executables

## uv, ruff etc
source "$HOME/.local/bin/env"

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

# ## postgres, psql etc
# case ":${PATH}:" in
#     *:"/opt/homebrew/opt/postgresql@18/bin":*)
#         ;;
#     *)
#         export PATH="/opt/homebrew/opt/postgresql@18/bin:$PATH"
#         ;;
# esac

# ## brew managed global python alias
# alias py=/opt/homebrew/bin/python3
# alias pip=/opt/homebrew/bin/pip3
