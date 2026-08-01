// import { dbQuery } from "../../config/database.js";

// export const taskRepository = {
//   findAll: async () => {
//     // SQLite returns done as 0 or 1, we convert 1 -> true, 0 -> false for API consistency
//     const rows = await dbQuery.all("SELECT * FROM tasks");
//     return rows.map((row) => ({ ...row, done: Boolean(row.done) }));
//   },

//   findById: async (id) => {
//     const row = await dbQuery.get("SELECT * FROM tasks WHERE id = ?", [id]);
//     if (!row) return null;
//     return { ...row, done: Boolean(row.done) };
//   },

//   findByTitle: async (title) => {
//     const row = await dbQuery.get(
//       "SELECT * FROM tasks WHERE LOWER(title) = LOWER(?)",
//       [title],
//     );
//     return row || null;
//   },

//   create: async (taskData) => {
//     const result = await dbQuery.run(
//       "INSERT INTO tasks (title, done) VALUES (?, ?)",
//       [taskData.title, taskData.done ? 1 : 0],
//     );

//     return {
//       id: result.lastID,
//       title: taskData.title,
//       done: Boolean(taskData.done),
//     };
//   },

//   update: async (id, updates) => {
//     // Fetch current state
//     const currentTask = await taskRepository.findById(id);
//     if (!currentTask) return null;

//     const newTitle =
//       updates.title !== undefined ? updates.title : currentTask.title;
//     const newDone =
//       updates.done !== undefined
//         ? updates.done
//           ? 1
//           : 0
//         : currentTask.done
//           ? 1
//           : 0;

//     await dbQuery.run("UPDATE tasks SET title = ?, done = ? WHERE id = ?", [
//       newTitle,
//       newDone,
//       id,
//     ]);

//     return {
//       id: Number(id),
//       title: newTitle,
//       done: Boolean(newDone),
//     };
//   },

//   deleteById: async (id) => {
//     const result = await dbQuery.run("DELETE FROM tasks WHERE id = ?", [id]);
//     return result.changes > 0;
//   },
// };

import { db } from "../../config/database.js";

export const taskRepository = {
  findAll: () => {
    const rows = db.prepare("SELECT * FROM tasks").all();
    return rows.map((row) => ({ ...row, done: Boolean(row.done) }));
  },

  findById: (id) => {
    const row = db.prepare("SELECT * FROM tasks WHERE id = ?").get(id);
    if (!row) return null;
    return { ...row, done: Boolean(row.done) };
  },

  findByTitle: (title) => {
    const row = db
      .prepare("SELECT * FROM tasks WHERE LOWER(title) = LOWER(?)")
      .get(title);
    return row || null;
  },

  create: (taskData) => {
    const stmt = db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)");
    const info = stmt.run(taskData.title, taskData.done ? 1 : 0);

    return {
      id: Number(info.lastInsertRowid),
      title: taskData.title,
      done: Boolean(taskData.done),
    };
  },

  update: (id, updates) => {
    const currentTask = taskRepository.findById(id);
    if (!currentTask) return null;

    const newTitle =
      updates.title !== undefined ? updates.title : currentTask.title;
    const newDone =
      updates.done !== undefined
        ? updates.done
          ? 1
          : 0
        : currentTask.done
          ? 1
          : 0;

    db.prepare("UPDATE tasks SET title = ?, done = ? WHERE id = ?").run(
      newTitle,
      newDone,
      id,
    );

    return {
      id: Number(id),
      title: newTitle,
      done: Boolean(newDone),
    };
  },

  deleteById: (id) => {
    const info = db.prepare("DELETE FROM tasks WHERE id = ?").run(id);
    return info.changes > 0;
  },
};
