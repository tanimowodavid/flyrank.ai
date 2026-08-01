// import app from "./src/app.js";
// import { initDb } from "./src/config/initDb.js";

// const PORT = process.env.PORT || 3000;

// // Initialize DB first, then start listening
// initDb().then(() => {
//   app.listen(PORT, () => {
//     console.log(`Server running on http://localhost:${PORT}`);
//   });
// });

import app from "./src/app.js";
import { initDb } from "./src/config/initDb.js";

const PORT = process.env.PORT || 3000;

// Initialize DB synchronously, then start server
initDb();

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
