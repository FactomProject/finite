# Factom Finite

Create, track, and validate tokenized event streams.

## Status

Early POC

## Development

Start factomd sim + wallet
```
./sim.py
```

Buy some EC's 
```
./test.sh buyec
```

### Docker-Compose tips

If you see an error like:
```
Creating network "finite_ptnet" with the default driver
ERROR: Pool overlaps with other one on this address spa
```

One (imperfect) way to get past this is to remove all docker networks
```
docker network ls -q | xargs docker network rm
```

