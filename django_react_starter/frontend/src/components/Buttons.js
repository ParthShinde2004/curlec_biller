import React, { Component } from "react";

export class Buttons extends Component {
  render() {
    return (
      <div className="btn-group-vertical">
        <button
          className="btn btn-outline-dark"
          type="button"
          style={{
            width: "75%",
            display: "block",
            color: "#5f3285",
          }}
        >
          Export to Zip
        </button>

        <button
          className="btn btn-primary"
          type="button"
          style={{
            width: "75%",
            display: "block",
          }}
        >
          Export to Excel
        </button>

        <button
          className="btn btn-primary"
          type="button"
          style={{
            width: "75%",
            display: "block",
          }}
        >
          List of Live Merchants
        </button>

        <button
          className="btn btn-primary"
          type="button"
          style={{
            width: "75%",
            display: "block",
          }}
        >
          List of Non-Live Merchants
        </button>
      </div>
    );
  }
}
export default Buttons;

/*
to do: Change colour of buttons
*/
