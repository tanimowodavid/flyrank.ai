import { taskRepository } from "./task.repository.js";

export const taskService = {
  getAllTasks: () => taskRepository.findAll(),

  getTaskById: (id) => {
    const task = taskRepository.findById(id);
    if (!task) {
      const error = new Error(`Task with ID ${id} not found`);
      error.statusCode = 404;
      throw error;
    }
    return task;
  },

  createTask: (data) => {
    if (
      !data.title ||
      typeof data.title !== "string" ||
      data.title.trim() === ""
    ) {
      const error = new Error("Title is required and cannot be empty");
      error.statusCode = 400;
      throw error;
    }

    const cleanTitle = data.title.trim();
    if (taskRepository.findByTitle(cleanTitle)) {
      const error = new Error("A task with this title already exists");
      error.statusCode = 400;
      throw error;
    }

    return taskRepository.create({
      title: cleanTitle,
      done: Boolean(data.done),
    });
  },

  updateTask: (id, updates) => {
    const task = taskRepository.findById(id);
    if (!task) {
      const error = new Error(`Task with ID ${id} not found`);
      error.statusCode = 404;
      throw error;
    }

    const { title, done } = updates;

    // Reject completely empty update payloads
    if (title === undefined && done === undefined) {
      const error = new Error("Request body cannot be empty");
      error.statusCode = 400;
      throw error;
    }

    // Validate title if provided
    let cleanTitle;
    if (title !== undefined) {
      if (typeof title !== "string" || title.trim() === "") {
        const error = new Error("Title cannot be empty");
        error.statusCode = 400;
        throw error;
      }
      cleanTitle = title.trim();
    }

    return taskRepository.update(task, {
      title: cleanTitle,
      done: done !== undefined ? Boolean(done) : undefined,
    });
  },

  deleteTask: (id) => {
    const index = taskRepository.findIndexById(id);
    if (index === -1) {
      const error = new Error(`Task with ID ${id} not found`);
      error.statusCode = 404;
      throw error;
    }
    taskRepository.deleteByIndex(index);
  },
};
