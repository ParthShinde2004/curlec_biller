import React, { Component } from "react";
import "./styles.css";

export class Buttons extends Component {
  render() {
    return (
      <div className="d-grid gap-2 col-6 mx-auto">
        <button
          className="btn btn-primary"
          type="button"
          style={{
            margin: "auto",
            width: "25%",
            display: "block",
          }}
        >
          Export to Zip
        </button>
        <button
          className="btn btn-primary"
          type="button"
          style={{ margin: "auto", width: "25%", display: "block" }}
        >
          Export to Excel
        </button>
        <button
          className="btn btn-primary"
          type="button"
          style={{ margin: "auto", width: "25%", display: "block" }}
        >
          List of Live Merchants
        </button>
        <button
          className="btn btn-primary"
          type="button"
          style={{ margin: "auto", width: "25%", display: "block" }}
        >
          List of Non-Live Merchants
        </button>
      </div>
    );
  }
}
export default Buttons;

/*
to do:
*/
