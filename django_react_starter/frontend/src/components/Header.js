import React, { Component } from "react";
import { PopUp } from "./PopUp";

export class Header extends Component {
  constructor(props) {
    super(props);

    this.state = { addPopUpShow: false };
  }

  render() {
    let addPopUpShow = () => this.setState({ addPopUpShow: false });

    return (
      <nav className="navbar navbar-expand-lg navbar-light bg-primary">
        <div className="container-fluid">
          <img
            src="	https://i.imgur.com/jQz37LB.png"
            alt=""
            height="auto"
            width="250"
            className="d-inline-block align-text-middle"
          ></img>
          <div
            className="popup-box"
            id="navbarSupportedContent"
            style={{ margin: "right" }}
          >
            <button
              className="btn btn-outline-info"
              type="button"
              onClick={() => this.setState({ addPopUpShow: true })}
            >
              Settings
            </button>
            <PopUp show={this.state.addPopUpShow} onHide={addPopUpShow} />
          </div>
        </div>
      </nav>
    );
  }
}

export default Header;
