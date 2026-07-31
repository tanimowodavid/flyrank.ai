// In-memory data store for tasks
const tasks = [
  { id: 1, title: "Task 1", done: false },
  { id: 2, title: "Task 2", done: false },
  { id: 3, title: "Task 3", done: true },
];

export const taskRepository = {
  findAll: () => tasks,

  findById: (id) => tasks.find((t) => t.id === Number(id)),

  create: (taskData) => {
    const newTask = {
      id: tasks.length + 1,
      title: taskData.title,
      done: taskData.done ?? false,
    };
    tasks.push(newTask);
    return newTask;
  },

  update: (task, updates) => {
    if (updates.title !== undefined) task.title = updates.title;
    if (updates.done !== undefined) task.done = updates.done;
    return task;
  },

  deleteByIndex: (index) => {
    tasks.splice(index, 1);
  },

  findIndexById: (id) => tasks.findIndex((t) => t.id === Number(id)),

  findByTitle: (title) =>
    tasks.find((t) => t.title.toLowerCase() === title.toLowerCase()),
};
