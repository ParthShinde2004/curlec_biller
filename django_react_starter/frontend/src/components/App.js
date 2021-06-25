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
      <div style={{ float: "left", width: 500, padding: 40, border: "black" }}>
        <LeftForm />
      </div>
      <div style={{ float: "right", width: 500, padding: 40 }}>
        <RightForm />
      </div>
      <div style={{ float: "middle" }}>
        <Buttons />
      </div>
    </div>
  );
};

const appDiv = document.getElementById("app");
render(<App />, appDiv);

/*
to do:
1. when you open console, settings button change
*/
