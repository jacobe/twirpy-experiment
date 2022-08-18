gen:
	# Auto-generate code
	protoc --proto_path=rpc --python_out=rpc --twirpy_out=rpc rpc/**/*.proto

upgrade:
	# Upgrade dependencies if using modules
	go get -u
