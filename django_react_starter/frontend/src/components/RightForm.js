import React, { Component } from "react";

export class RightForm extends Component {
  state = {
    customer: "",
    todate: "",
    fromdate: "",
    typepayment: "",
  };

  render() {
    const { customer, todate, fromdate, typepayment } = this.state;
    return (
      <div className="card card-body mt-4 mb-4">
        <form onSubmit={this.onSubmit}>
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
          <a>Is Live</a>
          <select
            className="form-select form-select-sm"
            aria-label=".form-select-sm example"
          >
            <option selected>Yes</option>
            <option value="1">No</option>
          </select>
          <a></a>
          <div className="form-group">
            <button
              type="submit"
              className="btn btn-primary"
              style={{ margin: "20px 0px" }}
            >
              Generate Invoice
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default RightForm;
/*
to do:
*/
