SRC_DIR=./proto
DST_DIR=./finite

# aggressive auto-reformat
find . -name '*.py' -exec autopep8 --in-place --aggressive --aggressive {} \;

# don't reformate generated code
python -m grpc_tools.protoc -I=$SRC_DIR \
  --python_out=$DST_DIR \
  --grpc_python_out=$DST_DIR \
  $SRC_DIR/event.proto


