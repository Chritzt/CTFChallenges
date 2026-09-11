// schema.js
const { makeExecutableSchema } = require('@graphql-tools/schema'); 
const { GraphQLSchema, GraphQLObjectType, GraphQLString, GraphQLBoolean } = require('graphql');
const { PubSub } = require('graphql-subscriptions');

const pubsub = new PubSub();
global.pubsub = pubsub; 

setInterval(() => {
  const publicChannel = global.reactiveCache.mappings["marketUpdates"];
  pubsub.publish(publicChannel, { marketUpdates: `BTC/USD: $${(Math.random() * 1000 + 60000).toFixed(2)}` });
}, 2000);

const QueryType = new GraphQLObjectType({
  name: 'Query',
  fields: {
    ping: {
      type: GraphQLString,
      resolve: () => "pong"
    }
  }
});

const MutationType = new GraphQLObjectType({
  name: 'Mutation',
  fields: {
    updateCacheConfig: {
      type: GraphQLBoolean,
      args: {
        streamName: { type: GraphQLString },
        targetChannel: { type: GraphQLString }
      },
      resolve: (_, { streamName, targetChannel }, context) => {
        if (!context.user) {
          throw new Error("401 Unauthorized");
        }

        if (global.reactiveCache.mappings[streamName]) {
          global.reactiveCache.mappings[streamName] = targetChannel;
          console.log(`[!] CRITICAL: Cache Key manipuliert! ${streamName} leitet jetzt weiter an ${targetChannel}`);
          return true;
        }
        return false;
      }
    }
  }
});

const SubscriptionType = new GraphQLObjectType({
  name: 'Subscription',
  fields: {
    marketUpdates: {
      type: GraphQLString,
      resolve: (payload) => payload.marketUpdates,
      subscribe: () => {
        const targetChannel = global.reactiveCache.mappings["marketUpdates"];
        return pubsub.asyncIterator([targetChannel]);
      }
    },
    adminSecrets: {
      type: GraphQLString,
      resolve: (payload) => payload.adminSecrets,
      subscribe: (_, __, context) => {
        if (!context.user || context.user.role !== 'admin') {
          throw new Error("403 Forbidden");
        }
        const targetChannel = global.reactiveCache.mappings["adminSecrets"];
        return pubsub.asyncIterator([targetChannel]);
      }
    }
  }
});

const schema = new GraphQLSchema({
  query: QueryType,
  mutation: MutationType,
  subscription: SubscriptionType
});

module.exports = { schema };