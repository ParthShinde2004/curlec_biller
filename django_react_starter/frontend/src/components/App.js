import React from "react";
import { render } from "react-dom";
import Header from "./Header";
import LeftForm from "./LeftForm";
import RightForm from "./RightForm";
import Buttons from "./Buttons";

const App = () => {
  return (
    <div>
      <Header />
      <LeftForm />
      <RightForm />
      <Buttons />
    </div>
  );
};

const appDiv = document.getElementById("app");
render(<App />, appDiv);

/*
to do:
1. when you open console, settings button change
*/
