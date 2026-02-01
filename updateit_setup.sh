#!/bin/bash
UPDATEIT="updateit.py"
UPDATEIT_ALIAS="updateit"
chmod +x "$UPDATEIT"
cp "$UPDATEIT" "$HOME/.local/bin/$UPDATEIT_ALIAS"
mkdir -p "$HOME/.local/share/updateit"
LATEST_LOGGER="$HOME/.local/share/updateit/latest.log"
if [ ! -f "$LATEST_LOGGER" ]; then
    touch "$LATEST_LOGGER"
fi

echo "Full updateit installed"
