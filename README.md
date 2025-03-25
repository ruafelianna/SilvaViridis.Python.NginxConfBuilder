# SilvaViridis.Exe.NginxConfBuilder

A tool to create Nginx configuration files in an OOP manner.

### Usage:

```python
from SilvaViridis.Exe.NginxConfBuilder.Defaults import get_docker_default_conf
from SilvaViridis.Exe.NginxConfBuilder.Generators import CrossplaneGenerator

conf = get_docker_default_conf()
gen = CrossplaneGenerator()

print(gen.build(conf))
```

### Documentation:

| Language | Link |
|:---:|:---:|
| English | [here](docs/en/index.md) |
