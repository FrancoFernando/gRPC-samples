1. setup venv

calculator % python3 -m venv venv    
calculator % source venv/bin/activate
(venv) % python -m pip install -r requirements.txt

2. install gRPC

python -m grpc_tools.protoc -I ../protobufs --python_out=. \
         --grpc_python_out=. ../protobufs/calculator.proto

3. launch server

python calculator.py