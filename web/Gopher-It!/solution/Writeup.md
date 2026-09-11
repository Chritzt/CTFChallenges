# Gopher It! - Writeup

An SSRF (Server-Side Request Forgery) vulnerability allows us to pivot into the isolated internal network and query an internal Redis instance via the legacy `gopher://` protocol.

## Vulnerability Analysis

The web application provides an administrative "Ping" tool that fetches user-specified URLs using `curl`. 

While the application restricts external access, it fails to sanitize the URL scheme. Crucially, `curl` supports the **Gopher protocol (`gopher://`)**, which allows sending raw TCP payloads (including newlines) to arbitrary ports. This is a classic vector to communicate with non-HTTP internal services like Redis.

## Exploitation Path

1. **Target Identification**: 
   The internal Redis service is located at `gopher-it-redis:6379`.
2. **Payload Construction**:
   We need to send a `GET flag` command followed by `QUIT` to close the connection.
   * Redis commands require `\r\n` (`%0D%0A`) as line endings.
   * The raw payload: `gopher://gopher-it-redis:6379/_GET flag\r\nQUIT\r\n`
3. **Double Encoding**:
   The web application's backend automatically URL-decodes query parameters before passing them to the system shell. If we send single-encoded newlines (`%0D%0A`), they decode into actual newlines, breaking the shell execution context. 
   
   To bypass this, we apply **double URL-encoding** so the payload arrives fully intact at the internal command execution level:
   * Space (` `) $\rightarrow$ `%20` $\rightarrow$ `%2520`
   * Carriage Return (`\r`) $\rightarrow$ `%0D` $\rightarrow$ `%250D`
   * Line Feed (`\n`) $\rightarrow$ `%0A` $\rightarrow$ `%250A`

## Final Payload

```http
GET /?url=gopher://gopher-it-redis:6379/_GET%2520flag%250D%250AQUIT%250D%250A HTTP/1.1
Host: gopher-it-web:5000
```

The application executes the query, queries the Redis database via Gopher, and returns the flag within the HTML response.