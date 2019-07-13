SRC_DIR=./proto
DST_DIR=./finite

python -m grpc_tools.protoc -I=$SRC_DIR \
  --python_out=$DST_DIR \
  --grpc_python_out=$DST_DIR \
  $SRC_DIR/event.proto

