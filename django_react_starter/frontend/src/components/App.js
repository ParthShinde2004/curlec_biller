import React from "react";
import { render } from "react-dom";
import Header from "./Header";
import LeftForm from "./LeftForm";
import RightForm from "./RightForm";

const App = () => {
  return (
    <div>
      <Header />
      <LeftForm />
      <RightForm />
    </div>
  );
};

const appDiv = document.getElementById("app");
render(<App />, appDiv);
