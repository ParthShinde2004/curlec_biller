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
            src="https://cdn.discordapp.com/attachments/775331190093119523/859655405343735808/curlec_new_logo_new_8.png"
            alt=""
            height="auto"
            width="250"
            className="d-inline-block align-text-middle"
            // style={{
            //   margin: 10,
            // }}
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
/*
to do:
1. make text bigger [DONE]
2. resize logo? [DONE]
3. add functionalities to settings button [in progress...]
4. change background colour of navbar
*/
export default Header;
