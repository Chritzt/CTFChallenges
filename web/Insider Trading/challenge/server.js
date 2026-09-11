// server.js
const express = require('express');
const { createServer } = require('http');
const { WebSocketServer } = require('ws');
const { useServer } = require('graphql-ws/lib/use/ws');
const { schema } = require('./schema');
const path = require('path');

const app = express();
const httpServer = createServer(app);


app.use(express.static(path.join(__dirname, 'public')));

const { startAdminBot } = require('./admin_bot');
startAdminBot();


const wsServer = new WebSocketServer({
  server: httpServer,
  path: '/graphql',
});

global.reactiveCache = {
  mappings: {
    "marketUpdates": "public:ticker",
    "adminSecrets": "secure:flag_stream"
  },
  channels: {
    "public:ticker": [],
    "secure:flag_stream": []
  }
};

useServer(
  {
    schema,
    onConnect: async (ctx) => {
      const authHeader = ctx.connectionParams?.Authorization || '';
      
      if (authHeader === 'Bearer admin-super-secret-token-2026') {
        ctx.extra = { user: { role: 'admin', name: 'SystemAdmin' } };
        return true;
      } else if (authHeader.startsWith('Bearer user-')) {
        const username = authHeader.replace('Bearer ', '');
        ctx.extra = { user: { role: 'guest', name: username } };
        return true;
      }
      
      return false;
    },
    context: (ctx) => {
      return {
        user: ctx.extra.user
      };
    }
  },
  wsServer
);

app.get('/api/auth', (req, res) => {
  const user = req.query.user || 'guest_player';
  res.json({ token: `Bearer user-${user}` });
});

const PORT = 4000;
httpServer.listen(PORT, () => {
  console.log(`[+] Challenge running  http://localhost:${PORT}/graphql`);
  console.log(`[+] WebSocket: ws://localhost:${PORT}/graphql`);
});

