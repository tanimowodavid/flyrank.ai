// import sqlite3 from "sqlite3";
// import path from "path";
// import { fileURLToPath } from "url";

// const __filename = fileURLToPath(import.meta.url);
// const __dirname = path.dirname(__filename);

// // Store tasks.db at project root
// const DB_PATH = path.resolve(__dirname, "../../tasks.db");

// // Enable verbose mode for helpful debug logs
// const sqlite = sqlite3.verbose();

// export const db = new sqlite.Database(DB_PATH, (err) => {
//   if (err) {
//     console.error("Error opening SQLite database:", err.message);
//   } else {
//     console.log("Connected to SQLite database at:", DB_PATH);
//   }
// });

// // Helper function to convert callback-based db.all/db.run into Promises
// export const dbQuery = {
//   // For SELECT queries returning multiple rows
//   all: (sql, params = []) => {
//     return new Promise((resolve, reject) => {
//       db.all(sql, params, (err, rows) => {
//         if (err) reject(err);
//         else resolve(rows);
//       });
//     });
//   },

//   // For SELECT queries returning a single row
//   get: (sql, params = []) => {
//     return new Promise((resolve, reject) => {
//       db.get(sql, params, (err, row) => {
//         if (err) reject(err);
//         else resolve(row);
//       });
//     });
//   },

//   // For INSERT, UPDATE, DELETE queries
//   run: (sql, params = []) => {
//     return new Promise((resolve, reject) => {
//       db.run(sql, params, function (err) {
//         if (err) reject(err);
//         else resolve({ lastID: this.lastID, changes: this.changes });
//       });
//     });
//   },
// };

import { DatabaseSync } from "node:sqlite";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const DB_PATH = path.resolve(__dirname, "../../tasks.db");

// Synchronous SQLite connection using Node's built-in API
export const db = new DatabaseSync(DB_PATH);
