import React, { Component } from "react";

export class Buttons extends Component {
  render() {
    return (
      <div className="d-grid gap-2 col-6 mx-auto">
        <button
          className="btn btn-primary"
          type="button"
          style={{ margin: "2px" }}
        >
          Export to Zip
        </button>
        <button
          className="btn btn-primary"
          type="button"
          style={{ margin: "2px" }}
        >
          Export to Excel
        </button>
        <button
          className="btn btn-primary"
          type="button"
          style={{ margin: "2px" }}
        >
          List of Live Merchants
        </button>
        <button
          className="btn btn-primary"
          type="button"
          style={{ margin: "2px" }}
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
