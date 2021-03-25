# Mixpanel Profile Cleanup
Cleanup the deduplicate profile of mixpanel


### usage

#### bash

```
pip install mixpanel-api 
```

```
deduplicate_people.py
```



#### docker

```
docker run --rm -v .:/app/mixpanel mmhk/mixpanel:python python /app/mixpanel/deduplicate_people.py
```


#### config 

```
[
    {
        "name": "[your project name]",
        "secret": "[API Secret of project]",
        "token": "[Token of project]",
        "match": "[deduplicate properties of profile, eg: name]"
    }
]
```

|key|remark|
|-|-|
|name|your project name|
|secret|API Secret of project|
|token|Token of project|
|match|deduplicate properties of profile, eg: name|