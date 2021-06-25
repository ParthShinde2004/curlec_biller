import React from "react";
import { render } from "react-dom";
import Header from "./Header";
import LeftForm from "./LeftForm";

const App = () => {
  return (
    <div>
      <Header />
      <LeftForm />
    </div>
  );
};

const appDiv = document.getElementById("app");
render(<App />, appDiv);
