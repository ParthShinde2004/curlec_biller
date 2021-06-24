import React from 'react';
import { render } from "react-dom";
import Settings from "./Settings";
import HomePage from "./HomePage";


const App = ()=> {
  return (
    <div>
      <HomePage /><Settings />
    </div>
  );
};

const appDiv = document.getElementById("app");
render(<App />, appDiv);

