import React, { Component } from "react";

export class Header extends Component {
  render() {
    return (
      <nav className="navbar navbar-expand-lg navbar-light bg-primary">
        <div className="container-fluid">
          <img
            src="https://curlec.com/wp-content/uploads/2021/01/CURLEC-LOGO.png"
            alt=""
            height="auto"
            width="150"
            class="d-inline-block align-text-middle"
          ></img>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0"></ul>
            <button className="btn btn-outline-info" type="button">
              Settings
            </button>
          </div>
        </div>
      </nav>
    );
  }
}
/*
to do:
1. make text bigger
2. resize logo?
3. add functionalities to settings button
4. change background colour of navbar
*/
export default Header;
