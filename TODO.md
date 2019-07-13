### Work-in-progress

Construct evenstore using proto3 scaffolding

WIP
---
- [ ] fix failing tests

BACKLOG
-------
- [ ] import finite eventstore operations as Grpc methods
- [ ] support compound actions as in ptnet-eventstore repo
- [ ] use Factom Blockchain as storage provider
- [ ] derive chain ID/external refs from UUIDs
- [ ] test 0FCT->EC ratio - assume private factom used as localdb
- [ ] figure out how to avoid hacking the python path to load pb modules

DONE
------
- [x] build proper docker-compose

ICEBOX
------
- [ ] CLOUD: use bigtable as storage
- [ ] CLOUD: support broadcast to pubsub
- [ ] prototype matching WASM interface to replicate .proto state machines 
- [ ] integrate harmony-identity service
- [ ] use DIDs/VC to control roles/permissions
- [ ] https://github.com/grpc-ecosystem/grpc-gateway
- [ ] pgsql+mongo: use https://github.com/EnterpriseDB/mongo_fdw to mix pgsql driver w/ direct access to blockchain DB
