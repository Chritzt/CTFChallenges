## YAML: Yet Another Malicious Language

It is a web exploitation challenge centered around insecure deserialization in Python using the PyYAML library. Players are presented with a satirical corporate dashboard ("Initech Cloud-Synergy Portal") containing an automated configuration file importer.

1. Exploring the web application reveals a few placeholder pages ("Home", "Settings"), and a main entry point for administrators under Config Importer (/importer).

2. The interface allows users to upload legacy .yaml or .yml configuration profiles, which are then evaluated and processed by the server.

3. Reviewing application behavior or source code (if available/guessed from typical misconfigurations) reveals that the application uses the unsafe `yaml.load(content, Loader=yaml.Loader)` function instead of the secure `yaml.safe_load()`.



In PyYAML, using the standard yaml.load() loader allows the parser to construct arbitrary Python objects defined inside the YAML file using specific tags like !!python/object/apply. This is a well-known vulnerability that leads directly to Remote Code Execution (RCE), as attackers can instantiate system modules or execute built-in functions.

### Exploitation
To extract the flag from the server's /flag.txt file, we can leverage Python's eval function via the YAML object instantiation tag.

By crafting a malicious YAML payload that invokes eval with a file-reading statement, the application evaluates the code and returns the output directly in the server's response object log.

Payload (exploit.yaml):

```YAML
!!python/object/apply:eval
- "open('/flag.txt').read()"
```


### Steps to Solve:
1. Navigate to the Config Importer page (/importer).

2. Upload the malicious .yaml file containing the payload.

3. The server processes the file via yaml.load, executes the eval command, and prints the contents of /flag.txt right inside the execution log on the webpage.