import React, { Component } from "react";

export class LeftForm extends Component {
  state = {
    customer: "",
    todate: "",
    fromdate: "",
    typepayment: "",
  };

  render() {
    const { customer, todate, fromdate, typepayment } = this.state;
    return (
      <div
        className="card card-body mt-4 mb-4"
        style={{ margin: "0px 0px 20px" }}
      >
        <label>Customer</label>
        <form onSubmit={this.onSubmit}>
          <select
            className="form-select form-select-sm"
            aria-label=".form-select-sm example"
          >
            <option selected>Select Customer</option>
            <option value="1">All</option>
            <option value="2">Two</option>
            <option value="3">Three</option>
          </select>

          <div className="form-group">
            <label>From</label>
            <input
              className="form-control"
              type="date"
              name="name"
              onChange={this.onChange}
              value={this.state.date}
            />
          </div>

          <div className="form-group">
            <label>To</label>
            <input
              className="form-control"
              type="date"
              name="name"
              onChange={this.onChange}
              value={this.state.date}
            />
          </div>
          <a>Type</a>
          <select
            className="form-select form-select-sm"
            aria-label=".form-select-sm example"
          >
            <option selected>Select Type</option>
            <option value="1">Mandate</option>
            <option value="2">Instant Pay (Bank)</option>
            <option value="3">Instant Pay (Credit Card)</option>
            <option value="4">Successful Pay (Bank)</option>
            <option value="4">Successful Pay (Credit Card)</option>
          </select>
          <a></a>
          <div className="form-group">
            <button
              type="submit"
              className="btn btn-primary"
              style={{ margin: "20px 0px" }}
            >
              Get Mailing List
            </button>
          </div>
          <div className="btn-group">
            <button type="button" className="btn btn-primary">
              Export to Zip
            </button>
            <button type="button" className="btn btn-success">
              Export to Excel
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default LeftForm;
/*
to do:
1. resize (left 1/3 of the screen) the menu 
2. space out each section
3. correct the functionality of the button 
*/
