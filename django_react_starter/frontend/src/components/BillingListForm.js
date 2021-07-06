import React, { Component } from "react";

export class BillingListForm extends Component {
  state = {
    disabled: false,
    disabled2: false,
    buttonactivated: false,
  };

  handle_customerChange = (e) => {
    if (e.target.value !== "All") {
      this.setState({
        disabled: true,
      });
    } else {
      this.setState({
        disabled: false,
      });
    }
  };

  handle_paymentChange = (f) => {
    this.props.setButton("inactive");
    this.props.setType(f.target.value);
    if (f.target.value === "Mandate") {
      this.setState({
        disabled2: true,
      });
    } else {
      this.setState({
        disabled2: false,
      });
    }
  };

  buttonfunc = () => {
    this.props.setButton("active");
  };

  render() {
    return (
      <div className="card card-body mt-4 mb-4">
        <label>Customer</label>
        <form>
          <select
            className="form-control"
            aria-label=".form-select-sm example"
            onChange={this.handle_customerChange}
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
            onChange={this.handle_paymentChange}
          >
            <option defaultValue>Select Type</option>
            <option value="Mandate">Mandate</option>
            <option value="Instant Pay (Bank)">Instant Pay (Bank)</option>
            <option value="Instant Pay (Card)">Instant Pay (Card)</option>
            <option value="Successful Pay (Bank)">Successful Pay (Bank)</option>
            <option value="Successful Pay (Card)">Successful Pay (Card)</option>
          </select>
          <div className="d-grid">
            <button
              type="button"
              className="btn btn-primary btn-block"
              style={{ margin: "10px 0px" }}
              onClick={this.buttonfunc}
            >
              Get Billing List
            </button>
          </div>

          <div className="btn-group d-md-flex mx-auto" role="toolbar">
            <button
              type="button"
              className="btn btn-outline-primary mr-2"
              style={{ minWidth: "205.5px" }}
              disabled={this.state.disabled || this.state.disabled2}
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

export default BillingListForm;
