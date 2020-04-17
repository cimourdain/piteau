#!/usr/bin/env bash
PYTHON_CMD=${1}
# Session Name
session="chat"


attach_tmux_session() {
    [ -n "${TMUX:-}" ] &&
        tmux switch-client -t ${1} ||
        tmux attach-session -t ${1}
}


start_chat() {
	# Start New Session with our name
	tmux new-session -d -s $session
	# clear prompt
	tmux send-keys "clear" C-m
	# split windows vertically
	tmux split-window -h
	# select right pane
	tmux select-pane -t 1
	# split right pane horizontally
	tmux split-window -v

	# start server
	tmux select-pane -t 1
	tmux send-keys "${PYTHON_CMD} samples/base_server.py" C-m
	sleep 1

	# start bot client
	tmux select-pane -t 2
	rm -f bot.log
	tmux send-keys "${PYTHON_CMD} samples/base_bot_client.py" C-m
	sleep 1

	# start client
	tmux select-pane -t 0
	rm -f client.log
	tmux send-keys "${PYTHON_CMD} samples/base_client.py 2>&1 | tee client.log" C-m
	tmux send-keys "hello test" C-m
	tmux send-keys "/time please" C-m
}

# start_chat
# attach_tmux_session ${session}
