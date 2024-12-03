
import React from "react";
import { createRoot } from "react-dom/client";

const App: React.FC = () => {
  return <h1>Hello, React!</h1>;
};

const container = document.getElementById("root");
if (container) {
  const root = createRoot(container);

  root.render(
      <App />
  );
} else {
  console.error("Root container not found");
}
