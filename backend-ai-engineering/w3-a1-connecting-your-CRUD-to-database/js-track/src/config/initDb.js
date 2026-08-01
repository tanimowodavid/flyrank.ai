// import { dbQuery } from "./database.js";

// export const initDb = async () => {
//   try {
//     // 1. Create table if not exists
//     await dbQuery.run(`
//       CREATE TABLE IF NOT EXISTS tasks (
//         id INTEGER PRIMARY KEY AUTOINCREMENT,
//         title TEXT NOT NULL,
//         done BOOLEAN NOT NULL DEFAULT 0
//       )
//     `);

//     // 2. Check if table is empty
//     const countResult = await dbQuery.get(
//       "SELECT COUNT(*) as count FROM tasks",
//     );

//     // 3. Seed 3 tasks ONLY if count is 0
//     if (countResult.count === 0) {
//       await dbQuery.run(`
//         INSERT INTO tasks (title, done) VALUES
//         ('Learn SQLite with Express', 1),
//         ('Build Stage 0 database layer', 0),
//         ('Submit FlyRank Assignment 2', 0)
//       `);
//       console.log("Database initialized with 3 example tasks.");
//     } else {
//       console.log("Database already contains tasks. Skipping seed.");
//     }
//   } catch (error) {
//     console.error("Database initialization failed:", error.message);
//   }
// };

import { db } from "./database.js";

export const initDb = () => {
  try {
    // 1. Create table if not exists
    db.exec(`
      CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        done BOOLEAN NOT NULL DEFAULT 0
      )
    `);

    // 2. Check if table is empty
    const countResult = db.prepare("SELECT COUNT(*) as count FROM tasks").get();

    // 3. Seed 3 tasks ONLY if count is 0
    if (countResult.count === 0) {
      const insertStmt = db.prepare(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
      );

      insertStmt.run("Learn SQLite with Express", 1);
      insertStmt.run("Build Stage 0 database layer", 0);
      insertStmt.run("Submit FlyRank Assignment 2", 0);
      console.log("Database initialized with 3 example tasks.");
    } else {
      console.log("Database already contains tasks. Skipping seed.");
    }
  } catch (error) {
    console.error("Database initialization failed:", error.message);
  }
};
