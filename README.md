## Vietnamese Knowledge Base

Powered by [wikibase-docker](https://github.com/wmde/wikibase-docker)

## Run

```
cd compose
docker-compose up
```

Go to [http://localhost:8181](http://localhost:8181)

## Services

| Service               | URL                                  |
|-----------------------|--------------------------------------|
| Mediawiki             | http://localhost:8181                |
| Wikibase QueryService | http://localhost:8282/               |
| Blazegraph            | http://localhost:8989/bigdata/#query |