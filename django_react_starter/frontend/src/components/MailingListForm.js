import React, { Component } from "react";

export class MailingListForm extends Component {
  state = {
    disabled: false,
  };

  handleChange = (e, f) => {
    if (e.target.value !== "All" || f.target.value === "Mandate") {
      this.setState({
        disabled: true,
      });
    } else {
      this.setState({
        disabled: false,
      });
    }
  };

  // handleChange2 = (f) => {
  //   if (f.target.value === "Mandate") {
  //     this.setState({
  //       disabled: true,
  //     });
  //   } else {
  //     this.setState({
  //       disabled: false,
  //     });
  //   }
  // };

  render() {
    return (
      <div className="card card-body mt-4 mb-4">
        <label>Customer</label>
        <form>
          <select
            className="form-control"
            aria-label=".form-select-sm example"
            onChange={this.handleChange}
          >
            <option defaultValue>Select Customer</option>
            <option value="All">All</option>
            <option value="Two">Two</option>
            <option value="Three">Three</option>
          </select>

          <div className="form-group">
            <label style={{ margin: "8px 0px 0px" }}>From</label>
            <input className="form-control" type="date" />
          </div>

          <div className="form-group">
            <label>To</label>
            <input className="form-control" type="date" />
          </div>
          <label>Type</label>
          <select
            className="form-control"
            aria-label=".form-select-sm example"
            onChange={this.handleChange}
          >
            <option defaultValue>Select Type</option>
            <option value="Mandate">Mandate</option>
            <option value="Instant Pay (Bank)">Instant Pay (Bank)</option>
            <option value="Instant Pay (Credit Card)">
              Instant Pay (Credit Card)
            </option>
            <option value="Successful Pay (Bank)">Successful Pay (Bank)</option>
            <option value="Successful Pay (Credit Card)">
              Successful Pay (Credit Card)
            </option>
          </select>
          <a></a>
          <div className="d-grid">
            <button
              type="submit"
              className="btn btn-primary btn-block"
              style={{ margin: "10px 0px" }}
            >
              Get Mailing List
            </button>
          </div>
          <div className="btn-group d-md-flex mx-auto" role="toolbar">
            <button
              type="button"
              className="btn btn-outline-primary mr-2"
              style={{ minWidth: "205.5px" }}
              disabled={this.state.disabled}
            >
              Export to Zip
            </button>
            <button
              type="button"
              className="btn btn-outline-primary"
              style={{ minWidth: "205.5px" }}
            >
              Export to Excel
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default MailingListForm;
/*
to do:
1. resize (left 1/3 of the screen) the menu 
2. space out each section
3. correct the functionality of the button 
*/
