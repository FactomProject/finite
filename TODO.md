### Work-in-progress

Construct eventstore using proto3 scaffolding

WIP
---
- [ ] code factomd-only storage w/ https://pypi.org/project/factom-api/
- [ ] use Factom Blockchain as storage provider

BACKLOG
-------
- [ ] support compound actions as in ptnet-eventstore repo
- [ ] function as a caching gateway to block against writing invalid blockchain events
- [ ] figure out how to avoid hacking the python path to load pb modules
- [ ] evaluate all pflow files in ./examples some may not be parsed properly
- [ ] import finite eventstore operations as Grpc methods
- [ ] derive chain ID/external refs from UUIDs

DONE
------
- [x] build proper docker-compose
- [x] code to work with an in-memory dict as datastore

ICEBOX
------
- [ ] prototype matching WASM interface to replicate .proto state machines 
- [ ] integrate harmony-identity service
- [ ] use DIDs/VC to control roles/permissions
- [ ] add recuring check to fund EC address
