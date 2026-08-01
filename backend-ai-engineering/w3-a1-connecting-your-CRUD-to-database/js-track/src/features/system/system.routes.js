import { Router } from "express";

const router = Router();

// Root metadata route
router.get("/", (req, res) => {
  res.json({
    name: "Task API",
    version: "1.0",
    status: "running",
    endpoints: ["/tasks", "/health", "/docs"],
  });
});

// Health check route
router.get("/health", (req, res) => {
  res.status(200).json({
    status: "OK",
    uptime: process.uptime(),
    timestamp: new Date().toISOString(),
  });
});

export default router;
