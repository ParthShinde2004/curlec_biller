import React, { Component } from "react";

export class Header extends Component {
  render() {
    return (
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">
            <img
              src="https://businessfinder.ctoscredit.com.my/wp-content/uploads/job-manager-uploads/company_avatar/2020/09/Curlec-Logo-150x150.png"
              alt=""
              height="30"
              width="30"
              class="d-inline-block align-text-middle"
            ></img>
            Curlec Billing
          </a>
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
            <button className="btn btn-primary" type="button">
              Settings
            </button>
          </div>
        </div>
      </nav>
    );
  }
}
/*
improvement:
1. make text bigger
2. resize logo?
3. add functionalities to settings button
4. change background colour of navbar
*/
export default Header;