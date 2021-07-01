import React, { Component } from "react";

export class InvoiceForm extends Component {
  state = {
    fromdateright: "",
    todateright: "",
    islive: "",
  };

  render() {
    const { fromdateright, todateright, islive } = this.state;
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
          <label>Is Live</label>
          <select className="form-control" aria-label=".form-select-sm example">
            <option defaultValue>Yes</option>
            <option value="1">No</option>
          </select>
          <a></a>
          <div className="form-group">
            <button
              type="submit"
              className="btn btn-primary btn-block"
              style={{ margin: "10px 0px" }}
            >
              Generate Invoice
            </button>
            <div className="btn-group d-md-flex mx-auto" role="toolbar">
              <button
                type="button"
                className="btn btn-outline-primary mr-2"
                style={{ minWidth: "205.5px" }}
              >
                Live Merchants
              </button>
              <button
                type="button"
                className="btn btn-outline-primary"
                style={{ minWidth: "205.5px" }}
              >
                Non-Live Merchants
              </button>
            </div>
          </div>
        </form>
      </div>
    );
  }
}

export default InvoiceForm;
