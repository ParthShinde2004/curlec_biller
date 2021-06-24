import React from 'react';
import HomePage from './HomePage';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

const Settings = ()=> {
  return (
    <div style={{ flexDirection: 'row', display: 'flex', justifyContent: 'flex-end' }}>
        <button>
            Settings
        </button>
    </div>
  );
};

export default Settings;