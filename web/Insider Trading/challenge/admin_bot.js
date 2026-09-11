// admin_bot.js
const FLAG = process.env.FLAG || "CLA{fallback_local_flag_failed}";

function startAdminBot() {
  
  setInterval(() => {
    if (global.pubsub) {
      const adminChannel = global.reactiveCache.mappings["adminSecrets"];
      
      global.pubsub.publish(adminChannel, { 
        adminSecrets: `[ADMIN INFO] System Health OK. Current Flag: ${FLAG}`,
        marketUpdates: `[HIJACKED DETECTED] ${FLAG}` 
      });
    }
  }, 5000);
}

module.exports = { startAdminBot };