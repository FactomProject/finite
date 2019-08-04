### Work-in-progress

Construct eventstore using proto3 scaffolding

WIP
---
- [ ] code factomd-only storage w/ https://pypi.org/project/factom-api/

BACKLOG
-------
- [ ] import finite eventstore operations as Grpc methods
- [ ] support compound actions as in ptnet-eventstore repo
- [ ] use Factom Blockchain as storage provider
- [ ] derive chain ID/external refs from UUIDs
- [ ] figure out how to avoid hacking the python path to load pb modules
- [ ] evaluate all pflow files in ./examples some may not be parsed properly

DONE
------
- [x] build proper docker-compose

ICEBOX
------
- [ ] prototype matching WASM interface to replicate .proto state machines 
- [ ] integrate harmony-identity service
- [ ] use DIDs/VC to control roles/permissions
- [ ] add recuring check to fund EC address
