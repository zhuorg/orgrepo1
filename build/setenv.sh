TARGET=release
DISPLAY=false

# Decode command line options.
while [[ $# -gt 0 ]]; do
    case "$1" in
        --debug)
            TARGET=debug
            ;;
        --display)
            DISPLAY=true
            ;;
    esac
    shift
done

# Build binary directory.
ROOTDIR=$(cd $(dirname "${BASH_SOURCE[0]}")/..; pwd)
ARCH=$(uname -m | sed -e 's/i.86/i386/' -e 's/^arm.*$/arm/')
HOST=$(hostname | sed -e 's/\..*//')
BINDIR="$ROOTDIR/bin/$TARGET-$ARCH-$HOST"

# Display or set path.
if $DISPLAY; then
    echo "$BINDIR"
elif [[ ":$PATH:" != *:$BINDIR:* ]]; then
    export PATH="$BINDIR:$PATH"
else
    # Make sure to exit with success status
    true
fi
