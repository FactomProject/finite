### Work-in-progress

Construct eventstore using proto3 scaffolding

WIP
---
- [ ] use entryhash as uuid - add lib for calculating this

BACKLOG
-------
- [ ] fix issue where exit code isn't set properly when running python -m unittest finite/tests/test_fct_store.py 
      ^ due to the '-m' flag passing on cli
- [ ] make it possible for embedded libs to set params
- [ ] tweak chain initialization chainid/chainhead to be more consistent
- [ ] support compound actions as in ptnet-eventstore repo
- [ ] add a method at boot
      that query and loads blockchain data
      create chainhead if it is missing

- [ ] function as a caching gateway to block against writing invalid blockchain events
- [ ] import finite eventstore operations as Grpc methods
- [ ] figure out how to avoid hacking the python path to load pb modules
- [ ] compose chain-ids & entryhash outside of factomd
      https://github.com/FactomProject/FactomSimpleGUI/blob/master/javaSigningAPI.java#L58
      https://github.com/FactomProject/factomd/blob/master/common/entryBlock/entry.go#L215-L237
      https://github.com/sambarnes/factom-core/blob/master/factom_core/block_elements/entry.py#L28

DONE
------
- [x] alter the storage accessor to additionally set chain + oid
- [x] build proper docker-compose
- [x] code to work with an in-memory dict as datastore
- [x] unit test loading ./finite/examples/octoe.pflow

ICEBOX
------
- [ ] evaluate all pflow files in ./examples some may not be parsed properly
- [ ] prototype matching WASM interface to replicate .proto state machines 
- [ ] integrate harmony-identity service
- [ ] use DIDs/VC to control roles/permissions
- [ ] add recuring check to fund EC address
- [ ] derive chain ID/external refs 'up front' before creating the chain
- [ ] design a way to have 'peer' events that submit compound actions at the same time
      each lists the other as a peer - the peer ID becomes the parent for subsequent events
      may mean using postgresql as a transaction server

