import { taskService } from "./task.service.js";

// Helper wrapper to catch errors automatically
const asyncHandler = (fn) => (req, res, next) =>
  Promise.resolve(fn(req, res, next)).catch(next);

export const taskController = {
  getTasks: asyncHandler((req, res) => {
    const tasks = taskService.getAllTasks();
    return res.status(200).json(tasks);
  }),

  getTaskById: asyncHandler((req, res) => {
    const task = taskService.getTaskById(req.params.id);
    return res.status(200).json(task);
  }),

  createTask: asyncHandler((req, res) => {
    const newTask = taskService.createTask(req.body);
    return res.status(201).json(newTask);
  }),

  updateTask: asyncHandler((req, res) => {
    const updatedTask = taskService.updateTask(req.params.id, req.body);
    return res.status(200).json(updatedTask);
  }),

  deleteTask: asyncHandler((req, res) => {
    taskService.deleteTask(req.params.id);
    return res.status(204).send();
  }),
};
