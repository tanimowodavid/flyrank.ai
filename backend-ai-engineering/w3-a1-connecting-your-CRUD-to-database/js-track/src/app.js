import fs from "fs";
import express from "express";
import swaggerUi from "swagger-ui-express";
import taskRoutes from "./features/tasks/task.routes.js";
import systemRoutes from "./features/system/system.routes.js";
import { errorHandler } from "./middlewares/error.middleware.js";

const app = express();

app.use(express.json());

// Load Swagger/OpenAPI document
const swaggerDocument = JSON.parse(
  fs.readFileSync(new URL("./config/swagger.json", import.meta.url), "utf-8"),
);

// Swagger UI Docs
app.use("/docs", swaggerUi.serve, swaggerUi.setup(swaggerDocument));

// Feature Routes
app.use("/", systemRoutes);
app.use("/tasks", taskRoutes);

// Central Error Handling Middleware (MUST BE LAST)
app.use(errorHandler);

export default app;
