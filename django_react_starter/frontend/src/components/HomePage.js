import React from 'react';
import Settings from './Settings';


import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

const HomePage = ()=> {
  return (
    <Router>
      <Switch>
        <Route exact path="/">
          <p>Curlec Billing Application</p>
        </Route>
      </Switch>
    </Router>
  );
};

export default HomePage;