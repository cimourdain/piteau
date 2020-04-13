#!/usr/bin/env bash
. scripts/utils.sh

start_chat
sleep 2
tmux kill-session -t ${session}
