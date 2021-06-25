import React from 'react';
import { render } from "react-dom";
import HomePage from "./HomePage";
import Header from "./Header";

const App = ()=> {
  return (
    <div>
      <Header />
    </div>
  );
};

const appDiv = document.getElementById("app");
render(<App />, appDiv);

